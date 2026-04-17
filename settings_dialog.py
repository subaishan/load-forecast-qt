from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Signal
from PySide6.QtSerialPort import QSerialPortInfo
from settings_dialog_ui import Ui_Dialog
from config_manager import config

class SettingsDialog(QDialog):
    # 定义信号：配置已保存，需要切换数据源
    config_saved = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.setWindowTitle("设置")
        
        self.init_serial_ports()
        self.init_baudrate()
        self.load_config()
        self.connect_signals()
        self.on_data_source_changed()
    
    def init_serial_ports(self):
        """初始化串口号下拉框，自动获取可用串口"""
        # 清空现有项
        self.ui.combo_port.clear()
        
        # 获取所有可用串口
        ports = QSerialPortInfo.availablePorts()
        port_names = [port.portName() for port in ports]
        
        if port_names:
            # 添加所有可用串口
            self.ui.combo_port.addItems(port_names)
        
        self.ui.combo_port.setEditable(True)
    
    def init_baudrate(self):
        """初始化波特率下拉框"""
        baudrates = ["9600", "19200", "38400", "57600", "115200", "230400"]
        self.ui.combo_baudrate.addItems(baudrates)
        self.ui.combo_baudrate.setEditable(True)
    
    def connect_signals(self):
        """连接信号槽"""
        self.ui.radio_serial.toggled.connect(self.on_data_source_changed)
        self.ui.radio_gprs.toggled.connect(self.on_data_source_changed)
        self.ui.btn_save.clicked.connect(self.on_save)
        self.ui.btn_cancel.clicked.connect(self.reject)
    
    def on_data_source_changed(self):
        """数据源类型切换时，显示/隐藏对应的设置区域"""
        if self.ui.radio_serial.isChecked():
            self.ui.group_serial.setVisible(True)
            self.ui.group_gprs.setVisible(False)
        else:
            self.ui.group_serial.setVisible(False)
            self.ui.group_gprs.setVisible(True)
    
    def load_config(self):
        """从配置文件加载数据到界面"""
        # 数据源类型
        source_type = config.get('data_source.type', 'serial')
        if source_type == 'serial':
            self.ui.radio_serial.setChecked(True)
        else:
            self.ui.radio_gprs.setChecked(True)
        
        # 串口配置
        port = config.get('data_source.serial.port', '')
        baudrate = config.get('data_source.serial.baudrate', 9600)
        serial_timeout = config.get('data_source.serial.timeout', 1)
        
        # 设置串口控件的值（空字符串表示自动模式）
        if port:
            index = self.ui.combo_port.findText(port)
            if index >= 0:
                self.ui.combo_port.setCurrentIndex(index)
            else:
                self.ui.combo_port.setEditText(port)
        else:
            # 自动模式：清空显示
            self.ui.combo_port.setEditText("")
        
        index = self.ui.combo_baudrate.findText(str(baudrate))
        if index >= 0:
            self.ui.combo_baudrate.setCurrentIndex(index)
        else:
            self.ui.combo_baudrate.setEditText(str(baudrate))
        
        self.ui.spin_serial_timeout.setValue(serial_timeout)
        
        # 4G配置
        gprs_host = config.get('data_source.gprs.host', '192.168.1.100')
        gprs_port = config.get('data_source.gprs.port', 8080)
        gprs_timeout = config.get('data_source.gprs.timeout', 1)
        
        self.ui.edit_gprs_host.setText(gprs_host)
        self.ui.edit_gprs_port.setText(str(gprs_port))
        self.ui.spin_gprs_timeout.setValue(gprs_timeout)
    
    def on_save(self):
        """保存设置"""
        # 保存数据源类型
        if self.ui.radio_serial.isChecked():
            config.set('data_source.type', 'serial')
        else:
            config.set('data_source.type', 'gprs')
        
        # 保存串口配置
        port = self.ui.combo_port.currentText().strip()
        baudrate = int(self.ui.combo_baudrate.currentText().strip())
        serial_timeout = self.ui.spin_serial_timeout.value()
        
        config.set('data_source.serial.port', port)
        config.set('data_source.serial.baudrate', baudrate)
        config.set('data_source.serial.timeout', serial_timeout)
        
        # 保存4G配置
        gprs_host = self.ui.edit_gprs_host.text().strip()
        gprs_port = int(self.ui.edit_gprs_port.text().strip())
        gprs_timeout = self.ui.spin_gprs_timeout.value()
        
        config.set('data_source.gprs.host', gprs_host)
        config.set('data_source.gprs.port', gprs_port)
        config.set('data_source.gprs.timeout', gprs_timeout)
        
        # 保存到文件
        if config.save():
            QMessageBox.information(self, "提示", "设置已保存，程序将重启生效。")
            self.accept()
            
            # 重启程序
            import sys
            import subprocess
            subprocess.Popen([sys.executable, sys.argv[0]])
            sys.exit(0)
        else:
            QMessageBox.warning(self, "错误", "保存设置失败，请检查配置文件权限。")