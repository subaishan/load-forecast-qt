from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog
from PySide6.QtCore import Signal
from export_data import Ui_Dialog
import os
from datetime import datetime


class ExportDialog(QDialog):
    """导出数据对话框"""
    
    # 定义信号：导出完成
    export_completed = Signal(str)
    
    def __init__(self, data_manager, parent=None):
        super().__init__(parent)
        self.data_manager = data_manager
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.setWindowTitle("导出数据")
        
        self.init_ui()
        self.load_default_values()
        self.connect_signals()
    
    def init_ui(self):
        """初始化界面"""
        # 设置文件格式下拉框的默认值
        self.ui.combox_format.clear()
        self.ui.combox_format.addItems(["csv", "json", "txt"])
    
    def load_default_values(self):
        """加载默认值"""
        # 默认输出目录：当前用户目录下的导出文件夹
        default_dir = os.path.expanduser("~/export_data")
        os.makedirs(default_dir, exist_ok=True)
        self.ui.line_edit_directory.set_path(default_dir)
        
        # 默认文件名：data_当前日期时间
        default_filename = f"data_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.ui.line_edit_filename.setPlainText(default_filename)
    
    def connect_signals(self):
        """连接信号槽"""
        self.ui.btn_export.clicked.connect(self.on_export)
        self.ui.btn_cancel.clicked.connect(self.reject)
    
    def on_export(self):
        """导出按钮点击事件"""
        # 检查是否有数据
        if self.data_manager.get_data_count() == 0:
            QMessageBox.warning(self, "提示", "没有数据可导出")
            return
        
        # 获取用户输入
        directory = self.ui.line_edit_directory.get_path()
        filename = self.ui.line_edit_filename.toPlainText().strip()
        file_format = self.ui.combox_format.currentText()
        
        # 验证目录
        if not directory:
            QMessageBox.warning(self, "提示", "请选择输出目录")
            return
        
        # 确保目录存在
        os.makedirs(directory, exist_ok=True)
        
        # 验证文件名
        if not filename:
            filename = f"data_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # 构建完整文件路径
        file_path = os.path.join(directory, f"{filename}.{file_format}")
        
        # 根据格式导出
        success = False
        if file_format == "csv":
            success = self.data_manager.export_to_csv(file_path)
        elif file_format == "json":
            success = self.data_manager.export_to_json(file_path)
        elif file_format == "txt":
            success = self.data_manager.export_to_txt(file_path)
        
        if success:
            QMessageBox.information(self, "成功", f"数据已导出到:\n{file_path}")
            self.export_completed.emit(file_path)
            self.accept()
        else:
            QMessageBox.critical(self, "错误", "导出失败，请检查数据或权限")