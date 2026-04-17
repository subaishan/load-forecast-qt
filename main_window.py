import sys
import time
from datetime import datetime
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer, Qt
import pyqtgraph as pg
from ui_form import Ui_MainWindow
from settings_dialog import SettingsDialog
from data_processor import DataProcessor
import resources_rc

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setWindowTitle("电负荷预测系统")
        
        # 创建数据处理器
        self.data_proc = DataProcessor()
        
        # 初始化曲线图
        self.init_plot()
        
        # 连接设置按钮
        if hasattr(self.ui, 'btn_settings'):
            self.ui.btn_settings.clicked.connect(self.open_settings)
        
        # 数据存储
        self.max_points = 3600  # 最多存储1小时（3600秒）
        self.time_data = []     # 存储时间戳（秒）
        self.power_real = []    # 实时功率
        self.power_predict = [] # 预测功率
        
        # 最后收到数据的时间
        self.last_data_time = None
        self.data_timeout = 5   # 5秒没收到数据视为超时
        
        # 定时器：1秒刷新一次（用于更新时间轴）
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)
        
        # 添加状态栏
        self.statusBar = self.statusBar()
        self.statusBar.showMessage("系统启动")
        
        # 串口状态检查定时器（每2秒）
        self.check_timer = QTimer()
        self.check_timer.timeout.connect(self.check_serial_status)
        self.check_timer.start(2000)
    
    def init_plot(self):
        """初始化曲线图"""
        self.plot_widget = self.ui.plotWidget
        self.plot_widget.setBackground('w')
        self.plot_widget.setLabel('bottom','时间')
        self.plot_widget.setLabel('left', '功率', units='W')
        self.plot_widget.setTitle("功率监测曲线")
        self.plot_widget.showGrid(x=True, y=True, alpha=0.5)

        # 启用鼠标交互
        self.plot_widget.setMouseEnabled(x=True, y=True)

        # 关闭 X 轴单位
        self.plot_widget.getAxis('bottom').enableAutoSIPrefix(False)

        # 固定 Y 轴范围（0 到 500W）
        self.plot_widget.setYRange(0, 500)

        # 禁用自动范围调整
        self.plot_widget.disableAutoRange(axis='y')

        # 添加图例
        self.plot_widget.addLegend()

        # 曲线1：实时功率（红色实线）
        self.curve_real = self.plot_widget.plot(
            pen=pg.mkPen(color='r', width=2),
            name='实时功率'
        )

        # 曲线2：预测功率（蓝色虚线）
        self.curve_predict = self.plot_widget.plot(
            pen=pg.mkPen(color='b', width=2, style=Qt.DashLine),
            name='预测功率'
        )

        # 设置 X 轴时间格式化（显示 时:分:秒）
        current_time = time.time()
        self.plot_widget.setXRange(current_time - 60, current_time)

        # 自定义刻度标签格式
        def tickStrings(values, scale, spacing):
            return [datetime.fromtimestamp(v).strftime("%H:%M:%S") for v in values]

        self.plot_widget.getAxis('bottom').tickStrings = tickStrings
    
    def update_timer(self):
        """每秒更新（时间轴前进）"""
        current_time = time.time()
        
        # 检查是否有新数据
        data = self.data_proc.get_all_data()
        
        if data is not None:
            # 收到新数据
            self.last_data_time = current_time
            power = data['power']
            predict = data['power_15min']
            
            # 添加数据点
            self.time_data.append(current_time)
            self.power_real.append(power)
            self.power_predict.append(predict)
            
            # 限制数据量
            if len(self.time_data) > self.max_points:
                self.time_data = self.time_data[-self.max_points:]
                self.power_real = self.power_real[-self.max_points:]
                self.power_predict = self.power_predict[-self.max_points:]
            
            # 更新状态栏
            self.statusBar.showMessage(f"正在接收数据 | 功率: {power:.1f} W")
            
            # 更新左侧标签
            self.update_labels(data)
        else:
            # 没有新数据
            if self.last_data_time is None:
                self.statusBar.showMessage("等待数据...")
            else:
                elapsed = current_time - self.last_data_time
                if elapsed > self.data_timeout:
                    self.statusBar.showMessage(f"数据超时 ({elapsed:.0f}秒未收到数据)")
                else:
                    self.statusBar.showMessage("等待数据...")
        
        # 更新曲线（始终显示所有数据点）
        if len(self.time_data) > 0:
            self.curve_real.setData(self.time_data, self.power_real)
            self.curve_predict.setData(self.time_data, self.power_predict)
            
            # 设置X轴范围（显示最近60秒）
            max_time = time.time()
            min_time = max_time - 60
            self.plot_widget.setXRange(min_time, max_time)
    
    def update_labels(self, data):
        """更新左侧标签"""
        if hasattr(self.ui, 'label_voltage'):
            self.ui.label_voltage.setText(f"{data['voltage']:.1f} V")
        if hasattr(self.ui, 'label_current'):
            self.ui.label_current.setText(f"{data['current']:.2f} A")
        if hasattr(self.ui, 'label_power'):
            self.ui.label_power.setText(f"{data['power']:.1f} W")
        if hasattr(self.ui, 'label_energy'):
            self.ui.label_energy.setText(f"{data['cumulative_energy']:.2f} kWh")
        if hasattr(self.ui, 'label_power_15min'):
            self.ui.label_power_15min.setText(f"{data['power_15min']:.1f} W")
        if hasattr(self.ui, 'label_power_60min'):
            self.ui.label_power_60min.setText(f"{data['power_60min']:.1f} W")
    
    def check_serial_status(self):
        """检查串口状态（每2秒）"""
        status = self.data_proc.get_reader_status()
        # 可以在控制台打印，或者更新状态栏
        # print(f"串口状态: {status}")
        
        # 如果需要更新状态栏
        if "未连接" in status or "未初始化" in status:
            self.statusBar.showMessage(f"串口状态: {status}")
        else:
            # 正常状态已经在 update_timer 中更新了
            pass
    
    def open_settings(self):
        """打开设置对话框"""
        dialog = SettingsDialog(self)
        dialog.config_saved.connect(self.on_config_saved)
        dialog.exec()
    
    def on_config_saved(self):
        """配置保存后的回调"""
        self.data_proc.switch_source()
        # 清空历史数据
        self.time_data.clear()
        self.power_real.clear()
        self.power_predict.clear()
        self.last_data_time = None
        self.curve_real.setData([], [])
        self.curve_predict.setData([], [])
    
    def closeEvent(self, event):
        """关闭窗口"""
        self.timer.stop()
        self.check_timer.stop()
        self.data_proc.close()
        event.accept()