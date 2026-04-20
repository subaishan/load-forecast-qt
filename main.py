# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

# 重要:
# 你需要先使用以下命令生成 UI 文件对应的 Python 代码：
#     pyside6-uic form.ui -o ui_form.py
#     pyside6-uic settings_dialog_ui.ui -o settings_dialog_ui.py
#     pyside6-uic export_data.ui -o export_data.py
#     pyside6-rcc resources.qrc -o resources_rc.py 


#     window下运行以下命令生成带目录的可执行文件 
#     pyinstaller --onedir --windowed --name 电负荷预测上位机 --add-data "config.json;." --add-data "icons;icons" main.py
#     window下运行以下命令生成单文件的可执行文件 
#     pyinstaller --onedir --windowed --name 电负荷预测上位机 --add-data "config.json;." --add-data "icons;icons" main.py
#     linux下运行以下命令生成带目录的可执行文件
#     pyinstaller --onedir --windowed --name 电负荷预测上位机 --add-data "config.json:." --add-data "icons:icons" main.py
#     linux下运行以下命令生成单文件的可执行文件     
#     pyinstaller --onefile --windowed --name 电负荷预测上位机 --add-data "config.json:." --add-data "icons:icons" main.py


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

