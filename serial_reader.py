import serial
import json
from config_manager import config
from PySide6.QtSerialPort import QSerialPortInfo

class SerialReader:
    def __init__(self):
        """从配置文件读取串口参数并初始化"""
        # 获取用户配置的端口号
        configured_port = config.get('data_source.serial.port', '')

        # 如果端口为空字符串，则自动选择第一个可用串口
        if configured_port == '':
            self.port = self._get_first_available_port()
            if self.port is None:
                self.port = None
        else:
            self.port = configured_port

        self.baudrate = config.get('data_source.serial.baudrate', 9600)
        self.timeout = config.get('data_source.serial.timeout', 1)
        self.ser = None
        self._connect()
    
    def _get_available_ports(self):
        """获取所有可用串口列表"""
        ports = QSerialPortInfo.availablePorts()
        return [port.portName() for port in ports]
    
    def _get_first_available_port(self):
        """获取第一个可用串口号"""
        ports = self._get_available_ports()
        if ports:
            return ports[0]
        return None
    
    def _is_port_valid(self, port_name):
        """检查指定的端口是否存在"""
        available_ports = self._get_available_ports()
        return port_name in available_ports
    
    def _connect(self):
        """连接串口"""
        if self.port is None:
            return False
        
        try:
            self.ser = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            return True
        except Exception as e:
            self.ser = None
            return False
    
    def read_data(self):
        """读取一行数据，返回字典，失败返回 None"""
        if self.ser and self.ser.is_open:
            try:
                line = self.ser.readline().decode('utf-8', errors='ignore').strip()
                if line:
                    data = json.loads(line)
                    return data
            except json.JSONDecodeError:
                pass
            except Exception as e:
                pass
        return None
    
    def get_power(self):
        """获取实时功率"""
        data = self.read_data()
        if data and 'power' in data:
            return float(data['power'])
        return None
    
    def get_all_data(self):
        """获取所有数据（电压、电流、功率）"""
        return self.read_data()
    
    def get_status(self):
        """获取连接状态"""
        if self.ser and self.ser.is_open:
            return f"已连接 {self.port}"
        else:
            return "未连接"

    def close(self):
        """关闭串口"""
        if self.ser and self.ser.is_open:
            self.ser.close()
    
    def reconnect(self):
        """重新连接（用于切换配置后）"""
        self.close()
        
        configured_port = config.get('data_source.serial.port', 'auto')
        
        if configured_port == 'auto' or configured_port == '':
            self.port = self._get_first_available_port()
        else:
            self.port = configured_port
        
        self.baudrate = config.get('data_source.serial.baudrate', 9600)
        self.timeout = config.get('data_source.serial.timeout', 1)
        return self._connect()