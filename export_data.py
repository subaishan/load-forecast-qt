# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_data.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

from widgets import PathSelector

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(366, 363)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.line_edit_directory = PathSelector(self.widget_2)
        self.line_edit_directory.setObjectName(u"line_edit_directory")
        self.line_edit_directory.setMaximumSize(QSize(16777215, 40))
        self.line_edit_directory.setFont(font)

        self.gridLayout.addWidget(self.line_edit_directory, 0, 1, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.line_edit_filename = QTextEdit(self.widget_2)
        self.line_edit_filename.setObjectName(u"line_edit_filename")
        self.line_edit_filename.setMaximumSize(QSize(16777215, 40))
        self.line_edit_filename.setFont(font)

        self.gridLayout.addWidget(self.line_edit_filename, 1, 1, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.combox_format = QComboBox(self.widget_2)
        self.combox_format.addItem("")
        self.combox_format.addItem("")
        self.combox_format.addItem("")
        self.combox_format.setObjectName(u"combox_format")
        self.combox_format.setMaximumSize(QSize(16777215, 40))
        self.combox_format.setFont(font)

        self.gridLayout.addWidget(self.combox_format, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_export = QPushButton(self.widget)
        self.btn_export.setObjectName(u"btn_export")
        self.btn_export.setFont(font)

        self.horizontalLayout.addWidget(self.btn_export)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btn_cancel = QPushButton(self.widget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setFont(font)

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout.setStretch(0, 7)
        self.verticalLayout.setStretch(1, 3)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u8f93\u51fa\u76ee\u5f55", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u8f93\u51fa\u6587\u4ef6\u540d\u79f0", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u8f93\u51fa\u6587\u4ef6\u683c\u5f0f", None))
        self.combox_format.setItemText(0, QCoreApplication.translate("Dialog", u"csv", None))
        self.combox_format.setItemText(1, QCoreApplication.translate("Dialog", u"json", None))
        self.combox_format.setItemText(2, QCoreApplication.translate("Dialog", u"txt", None))

        self.btn_export.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

