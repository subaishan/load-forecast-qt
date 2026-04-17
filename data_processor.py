import time
import json
import os
import random
from config_manager import config
from serial_reader import SerialReader
from gprs_reader import GprsReader

class DataProcessor:
    def __init__(self):
        """初始化数据处理器，根据配置选择数据源"""
        self.source_type = config.get('data_source.type', 'serial')
        self.reader = None
        self._init_reader()
        
        # 累积电量 (kWh)
        self.cumulative_energy = 0.0
        self.last_power = 0.0
        self.last_time = time.time()
        
        # 加载保存的累积电量
        self._load_energy()
        
        # 历史功率数据（用于预测）
        self.power_history = []  # 存储最近N个功率值
        self.max_history = 3600  # 最多保存1小时（3600秒）
        
        # 趋势方向
        self.trend_direction = 0  # -1:下降, 0:平稳, 1:上升
        self.trend_strength = 0   # 趋势强度（0-1）
    
    def _init_reader(self):
        """根据配置初始化数据源"""
        if self.source_type == 'serial':
            self.reader = SerialReader()
        else:
            self.reader = GprsReader()
    
    def _load_energy(self):
        """加载保存的累积电量"""
        energy_file = 'energy_cache.json'
        if os.path.exists(energy_file):
            try:
                with open(energy_file, 'r') as f:
                    data = json.load(f)
                    self.cumulative_energy = data.get('cumulative_energy', 0.0)
            except Exception as e:
                pass
    
    def _save_energy(self):
        """保存累积电量"""
        energy_file = 'energy_cache.json'
        try:
            with open(energy_file, 'w') as f:
                json.dump({'cumulative_energy': self.cumulative_energy}, f)
        except Exception as e:
            pass
    
    def _update_energy(self, power_watts):
        """更新累积电量 (kWh)"""
        current_time = time.time()
        delta_hours = (current_time - self.last_time) / 3600.0
        
        if delta_hours > 0 and delta_hours < 10:
            avg_power = (self.last_power + power_watts) / 2.0
            energy_kwh = avg_power * delta_hours / 1000.0
            self.cumulative_energy += energy_kwh
            self._save_energy()
        
        self.last_power = power_watts
        self.last_time = current_time
    
    def _update_trend(self, current_power):
        """更新趋势方向和强度"""
        # 保存到历史记录
        self.power_history.append(current_power)
        if len(self.power_history) > self.max_history:
            self.power_history.pop(0)
        
        # 需要足够的数据才能判断趋势
        if len(self.power_history) < 30:
            self.trend_direction = 0
            self.trend_strength = 0
            return
        
        # 计算最近1分钟的趋势（60个点）
        recent = self.power_history[-60:] if len(self.power_history) >= 60 else self.power_history
        change = recent[-1] - recent[0]
        
        # 判断方向
        if change > 1.0:
            self.trend_direction = 1  # 上升
            self.trend_strength = min(1.0, change / 10.0)  # 强度0-1
        elif change < -1.0:
            self.trend_direction = -1  # 下降
            self.trend_strength = min(1.0, abs(change) / 10.0)
        else:
            self.trend_direction = 0  # 平稳
            self.trend_strength = 0
    
    def _calculate_offset(self, minutes, current_power):
        """计算预测偏移量（基于趋势方向和强度）"""
        if self.trend_direction == 1:
            # 上升趋势：偏移量为正
            if minutes <= 1:
                # 实时预测：2-4W
                base_offset = random.uniform(2, 4)
            elif minutes == 15:
                # 15分钟：5-8W
                base_offset = random.uniform(5, 8)
            else:  # 60分钟
                # 1小时：8-12W
                base_offset = random.uniform(8, 12)
            
            # 趋势强度微调（最多影响 ±10%）
            strength_factor = 0.9 + self.trend_strength * 0.2  # 0.9 ~ 1.1
            offset = base_offset * strength_factor
            return offset
            
        elif self.trend_direction == -1:
            # 下降趋势：偏移量为负
            if minutes <= 1:
                base_offset = random.uniform(-4, -2)
            elif minutes == 15:
                base_offset = random.uniform(-8, -5)
            else:
                base_offset = random.uniform(-12, -8)
            
            strength_factor = 0.9 + self.trend_strength * 0.2  # 0.9 ~ 1.1
            offset = base_offset * strength_factor
            return offset
            
        else:
            # 平稳趋势：小范围波动
            if minutes <= 1:
                return random.uniform(-2, 2)
            elif minutes == 15:
                return random.uniform(-4, 4)
            else:
                return random.uniform(-6, 6)
    
    def _predict_power(self, minutes, current_power):
        """预测指定分钟后的功率
        
        参数:
            minutes: 预测多少分钟后（1, 15, 60）
            current_power: 当前实时功率
        
        返回:
            预测功率值
        """
        offset = self._calculate_offset(minutes, current_power)
        predicted = current_power + offset
        
        # 功率不能为负
        return max(0, predicted)
    
    def get_all_data(self):
        """获取所有数据，返回字典"""
        # 从硬件读取原始数据
        raw_data = None
        if self.reader:
            raw_data = self.reader.get_all_data()

        # 如果读取失败，返回 None
        if raw_data is None:
            return None

        # 提取数值
        voltage = raw_data.get('voltage', 0.0)
        current = raw_data.get('current', 0.0)
        power = raw_data.get('power', 0.0)

        # 更新趋势（基于历史数据）
        self._update_trend(power)

        # 更新累积电量
        self._update_energy(power)

        # 计算预测功率
        power_now = self._predict_power(1, power)      # 实时预测（1秒后）
        power_15min = self._predict_power(15, power)   # 15分钟后
        power_60min = self._predict_power(60, power)   # 1小时后

        return {
            'voltage': voltage,
            'current': current,
            'power': power,
            'power_now': power_now,
            'cumulative_energy': self.cumulative_energy,
            'power_15min': power_15min,
            'power_60min': power_60min
        }
    
    def get_reader_status(self):
        """获取当前数据源的连接状态"""
        if self.reader:
            if hasattr(self.reader, 'get_status'):
                return self.reader.get_status()
            else:
                if hasattr(self.reader, 'ser') and self.reader.ser and self.reader.ser.is_open:
                    return f"已连接 {self.reader.port}"
                return "未连接"
        return "未初始化"
    
    def switch_source(self):
        """切换数据源（热切换用）"""
        if self.reader:
            self.reader.close()
        
        self.source_type = config.get('data_source.type', 'serial')
        self._init_reader()
        
        # 重置历史数据
        self.power_history = []
        self.trend_direction = 0
        self.trend_strength = 0
        
    
    def close(self):
        """关闭数据源连接"""
        if self.reader:
            self.reader.close()