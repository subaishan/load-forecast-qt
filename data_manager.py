from collections import deque
from datetime import datetime
import csv
import json
from typing import List, Dict, Optional

class DataManager:
    """数据管理类：存储历史数据，支持多种格式导出"""
    
    def __init__(self, max_size=10000):
        """
        初始化数据管理器
        
        Args:
            max_size: 最大存储数据条数（FIFO，自动淘汰旧数据）
        """
        self.data_buffer = deque(maxlen=max_size)
        self.last_export_time = None
        
    def add_data(self, data: Dict) -> bool:
        """
        添加一条数据
        
        Args:
            data: 数据字典，格式如：
                {
                    'voltage': float,
                    'current': float,
                    'power': float,
                    'power_now': float,
                    'cumulative_energy': float,
                    'power_15min': float,
                    'power_60min': float
                }
        
        Returns:
            是否添加成功
        """
        if not data:
            return False
        
        # 添加时间戳
        data_with_time = data.copy()
        data_with_time['timestamp'] = datetime.now()
        
        self.data_buffer.append(data_with_time)
        return True
    
    def get_data_count(self) -> int:
        """获取当前存储的数据条数"""
        return len(self.data_buffer)
    
    def get_all_data(self) -> List[Dict]:
        """获取所有存储的数据"""
        return list(self.data_buffer)
    
    def get_latest_data(self) -> Optional[Dict]:
        """获取最新的一条数据"""
        if self.data_buffer:
            return self.data_buffer[-1]
        return None
    
    def clear(self):
        """清空所有数据"""
        self.data_buffer.clear()
    
    def export_to_csv(self, filename: str = None) -> Optional[str]:
        """
        导出为 CSV 文件
        
        Args:
            filename: 文件名，不指定则自动生成
        
        Returns:
            保存的文件路径，失败返回 None
        """
        if not self.data_buffer:
            return None
        
        if filename is None:
            filename = f"data_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        # CSV 列名
        fieldnames = ['timestamp', 'voltage', 'current', 'power', 
                      'power_now', 'cumulative_energy', 'power_15min', 'power_60min']
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                
                for data in self.data_buffer:
                    # 格式化时间戳
                    row = {
                        'timestamp': data['timestamp'].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
                        'voltage': data['voltage'],
                        'current': data['current'],
                        'power': data['power'],
                        'power_now': data['power_now'],
                        'cumulative_energy': data['cumulative_energy'],
                        'power_15min': data['power_15min'],
                        'power_60min': data['power_60min']
                    }
                    writer.writerow(row)
            
            self.last_export_time = datetime.now()
            return filename
            
        except Exception as e:
            print(f"导出 CSV 失败: {e}")
            return None
    
    def export_to_json(self, filename: str = None) -> Optional[str]:
        """
        导出为 JSON 文件
        
        Args:
            filename: 文件名，不指定则自动生成
        
        Returns:
            保存的文件路径，失败返回 None
        """
        if not self.data_buffer:
            return None
        
        if filename is None:
            filename = f"data_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        try:
            # 转换数据格式（时间戳转为字符串）
            export_data = []
            for data in self.data_buffer:
                export_data.append({
                    'timestamp': data['timestamp'].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
                    'voltage': data['voltage'],
                    'current': data['current'],
                    'power': data['power'],
                    'power_now': data['power_now'],
                    'cumulative_energy': data['cumulative_energy'],
                    'power_15min': data['power_15min'],
                    'power_60min': data['power_60min']
                })
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            self.last_export_time = datetime.now()
            return filename
            
        except Exception as e:
            print(f"导出 JSON 失败: {e}")
            return None
    
    def export_to_txt(self, filename: str = None) -> Optional[str]:
        """
        导出为 TXT 文件（可读格式，带说明）
        """
        if not self.data_buffer:
            return None

        if filename is None:
            filename = f"data_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                # 写入文件头
                f.write("=" * 60 + "\n")
                f.write("数据导出报告\n")
                f.write(f"导出时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"数据条数: {len(self.data_buffer)}\n")
                f.write("=" * 60 + "\n\n")

                # 写入每条数据
                for i, data in enumerate(self.data_buffer, 1):
                    f.write(f"[{i}] 时间: {data['timestamp'].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}\n")
                    f.write(f"    电压: {data['voltage']:.1f} V\n")
                    f.write(f"    电流: {data['current']:.2f} A\n")
                    f.write(f"    功率: {data['power']:.1f} W\n")
                    f.write(f"    实时预测: {data['power_now']:.1f} W\n")
                    f.write(f"    累计电能: {data['cumulative_energy']:.2f} kWh\n")
                    f.write(f"    15分钟预测: {data['power_15min']:.1f} W\n")
                    f.write(f"    60分钟预测: {data['power_60min']:.1f} W\n")
                    f.write("-" * 40 + "\n")

            self.last_export_time = datetime.now()
            return filename

        except Exception as e:
            print(f"导出 TXT 失败: {e}")
            return None
    
    def get_summary(self) -> Dict:
        """获取数据摘要信息"""
        if not self.data_buffer:
            return {
                'count': 0,
                'start_time': None,
                'end_time': None,
                'duration_seconds': 0
            }
        
        start_time = self.data_buffer[0]['timestamp']
        end_time = self.data_buffer[-1]['timestamp']
        duration = (end_time - start_time).total_seconds()
        
        return {
            'count': len(self.data_buffer),
            'start_time': start_time.strftime('%Y-%m-%d %H:%M:%S'),
            'end_time': end_time.strftime('%Y-%m-%d %H:%M:%S'),
            'duration_seconds': duration
        }