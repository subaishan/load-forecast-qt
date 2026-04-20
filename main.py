# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
#     pyside6-uic settings_dialog_ui.ui -o settings_dialog_ui.py
#     pyside6-uic export_data.ui -o export_data.py
#     pyside6-rcc resources.qrc -o resources_rc.py 
#     pyinstaller --onedir --windowed --name 电负荷预测上位机 --add-data "config.json;." --add-data "icons;icons" main.py

# 测试
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

