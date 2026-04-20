import json
import paho.mqtt.client as mqtt
from config_manager import config

class GprsReader:
    def __init__(self):
        """从配置文件读取MQTT参数并初始化"""
        self.host = config.get('data_source.gprs.host', '39.105.18.152')
        self.port = config.get('data_source.gprs.port', 1883)
        self.username = config.get('data_source.gprs.username', 'QtAppUser')
        self.password = config.get('data_source.gprs.password', '3774691Cjjdf') 
        self.topic = config.get('data_source.gprs.topic', 'stm32/sensor')
        self.timeout = config.get('data_source.gprs.timeout', 1)
        
        self.client = None
        self.latest_data = None
        self._connect()
    
    def _connect(self):
        """连接MQTT服务器"""
        try:
            self.client = mqtt.Client()
            
            # 设置用户名和密码
            self.client.username_pw_set(self.username, self.password)
            
            # 设置回调函数
            self.client.on_connect = self._on_connect
            self.client.on_message = self._on_message
            
            # 连接服务器
            self.client.connect(self.host, self.port, self.timeout)
            
            # 启动网络循环（非阻塞）
            self.client.loop_start()
            
            print(f"MQTT连接成功: {self.host}:{self.port}")
            return True
        except Exception as e:
            print(f"MQTT连接失败: {e}")
            self.client = None
            return False
    
    def _on_connect(self, client, userdata, flags, rc):
        """连接成功回调"""
        if rc == 0:
            print(f"MQTT连接成功，订阅主题: {self.topic}")
            # 订阅主题
            self.client.subscribe(self.topic)
        else:
            print(f"MQTT连接失败，返回码: {rc}")
    
    def _on_message(self, client, userdata, msg):
        """收到消息回调"""
        try:
            payload = msg.payload.decode('utf-8')
            print(f"收到消息: {payload}")
            self.latest_data = json.loads(payload)
        except Exception as e:
            print(f"消息解析失败: {e}")
    
    def read_data(self):
        """读取最新数据，返回字典，失败返回 None"""
        if self.client is None:
            return None
        
        # 返回最新收到的数据
        data = self.latest_data

        # 清空，等待新数据
        self.latest_data = None
        return data
    
    def get_power(self):
        """获取实时功率"""
        data = self.read_data()
        if data and 'power' in data:
            return float(data['power'])
        return None
    
    def get_all_data(self):
        """获取所有数据（电压、电流、功率）"""
        return self.read_data()
    
    def close(self):
        """关闭MQTT连接"""
        if self.client:
            self.client.loop_stop()
            self.client.disconnect()
            print("MQTT连接已关闭")
    
    def reconnect(self):
        """重新连接（用于切换配置后）"""
        self.close()
        
        # 重新读取配置
        self.host = config.get('data_source.gprs.host', '39.105.18.152')
        self.port = config.get('data_source.gprs.port', 1883)
        self.username = config.get('data_source.gprs.username', 'QtAppUser')
        self.password = config.get('data_source.gprs.password', 'xxxxx')
        self.topic = config.get('data_source.gprs.topic', 'stm32/sensor')
        self.timeout = config.get('data_source.gprs.timeout', 1)
        
        return self._connect()
    
    def get_status(self):
        """获取连接状态"""
        if self.client and self.client.is_connected():
            return f"已连接 {self.host}:{self.port}"
        else:
            return "未连接"