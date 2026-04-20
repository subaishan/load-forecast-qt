# widgets.py
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton, QFileDialog
from PySide6.QtCore import Signal

class PathSelector(QWidget):
    pathChanged = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("请选择目录")
        layout.addWidget(self.line_edit)
        
        self.browse_btn = QPushButton("浏览")
        self.browse_btn.clicked.connect(self._on_browse)
        layout.addWidget(self.browse_btn)
    
    def _on_browse(self):
        dir_path = QFileDialog.getExistingDirectory(
            self, "选择目录", self.line_edit.text() or ""
        )
        if dir_path:
            self.set_path(dir_path)
    
    def get_path(self):
        return self.line_edit.text()
    
    def set_path(self, path):
        self.line_edit.setText(path)
        self.pathChanged.emit(path)