import json
import os

class ConfigManager:
    """配置管理器（单例模式）"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_config()
        return cls._instance
    
    def _init_config(self):
        """初始化配置"""
        self._config_file = os.path.join(os.path.dirname(__file__), 'config.json')
        self._config = self._load_config()
    
    def _load_config(self):
        """加载配置文件，如果不存在则创建默认配置"""
        if os.path.exists(self._config_file):
            try:
                with open(self._config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                return self._get_default_config()
        else:
            default_config = self._get_default_config()
            self._save_config(default_config)
            return default_config
    
    def _get_default_config(self):
        """返回默认配置"""
        return {
            "data_source": {
                "type": "serial",
                "serial": {
                    "port": "COM3",
                    "baudrate": 9600,
                    "timeout": 1
                },
                "gprs": {
                    "host": "39.105.18.152",
                    "port": 1883,
                    "username": "QtAppUser",
                    "password": "xxxxx",
                    "topic": "stm32/sensor",
                    "timeout": 1
                }
            },
            "display": {
                "update_interval_ms": 1000,
                "plot_data_length": 60,
                "plot_y_auto_range": True,
                "plot_y_min": 0,
                "plot_y_max": 200
            }
        }
    
    def _save_config(self, config):
        """保存配置到文件"""
        try:
            with open(self._config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            return False
    
    def get(self, key_path, default=None):
        """根据点分隔的路径获取配置值
        例如: get('data_source.serial.port') 返回 'COM3'
        """
        keys = key_path.split('.')
        value = self._config
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key)
                if value is None:
                    return default
            else:
                return default
        return value
    
    def set(self, key_path, value):
        """根据点分隔的路径设置配置值
        例如: set('data_source.serial.port', 'COM4')
        """
        keys = key_path.split('.')
        config = self._config
        for key in keys[:-1]:
            if key not in config:
                config[key] = {}
            config = config[key]
        config[keys[-1]] = value
    
    def save(self):
        """保存当前配置到文件"""
        return self._save_config(self._config)
    
    def reload(self):
        """重新加载配置文件"""
        self._config = self._load_config()
    
    @property
    def all_config(self):
        """获取整个配置字典"""
        return self._config.copy()


# 全局单例实例
config = ConfigManager()


# 测试代码（运行时取消注释）
# if __name__ == "__main__":
#     print("=== 测试配置管理器 ===")
#     print(f"数据源类型: {config.get('data_source.type')}")
#     print(f"串口号: {config.get('data_source.serial.port')}")
#     print(f"4G IP: {config.get('data_source.gprs.host')}")
#     print(f"刷新间隔: {config.get('display.update_interval_ms')} ms")
    
#     print("\n=== 测试设置值 ===")
#     config.set('data_source.serial.port', 'COM5')
#     print(f"修改后串口号: {config.get('data_source.serial.port')}")
    
#     print("\n=== 测试保存 ===")
#     config.save()
#     print("配置已保存到 config.json")