# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(389, 505)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.radio_serial = QRadioButton(self.groupBox)
        self.radio_serial.setObjectName(u"radio_serial")

        self.horizontalLayout_2.addWidget(self.radio_serial)

        self.radio_gprs = QRadioButton(self.groupBox)
        self.radio_gprs.setObjectName(u"radio_gprs")
        self.radio_gprs.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.radio_gprs)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addWidget(self.groupBox)

        self.group_serial = QGroupBox(self.frame)
        self.group_serial.setObjectName(u"group_serial")
        self.group_serial.setFont(font)
        self.gridLayout_2 = QGridLayout(self.group_serial)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, 9, -1)
        self.label_2 = QLabel(self.group_serial)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.combo_baudrate = QComboBox(self.group_serial)
        self.combo_baudrate.setObjectName(u"combo_baudrate")

        self.gridLayout_2.addWidget(self.combo_baudrate, 1, 2, 1, 1)

        self.spin_serial_timeout = QSpinBox(self.group_serial)
        self.spin_serial_timeout.setObjectName(u"spin_serial_timeout")

        self.gridLayout_2.addWidget(self.spin_serial_timeout, 2, 2, 1, 1)

        self.label_3 = QLabel(self.group_serial)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)

        self.combo_port = QComboBox(self.group_serial)
        self.combo_port.setObjectName(u"combo_port")

        self.gridLayout_2.addWidget(self.combo_port, 0, 2, 1, 1)

        self.label = QLabel(self.group_serial)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.group_serial)

        self.group_gprs = QGroupBox(self.frame)
        self.group_gprs.setObjectName(u"group_gprs")
        self.group_gprs.setFont(font)
        self.gridLayout_3 = QGridLayout(self.group_gprs)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.edit_gprs_port = QLineEdit(self.group_gprs)
        self.edit_gprs_port.setObjectName(u"edit_gprs_port")

        self.gridLayout_3.addWidget(self.edit_gprs_port, 1, 2, 1, 1)

        self.label_5 = QLabel(self.group_gprs)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_4 = QLabel(self.group_gprs)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.edit_gprs_host = QLineEdit(self.group_gprs)
        self.edit_gprs_host.setObjectName(u"edit_gprs_host")

        self.gridLayout_3.addWidget(self.edit_gprs_host, 0, 2, 1, 1)

        self.spin_gprs_timeout = QSpinBox(self.group_gprs)
        self.spin_gprs_timeout.setObjectName(u"spin_gprs_timeout")

        self.gridLayout_3.addWidget(self.spin_gprs_timeout, 2, 2, 1, 1)

        self.label_6 = QLabel(self.group_gprs)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 2, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 1, 3, 1, 1)


        self.verticalLayout.addWidget(self.group_gprs)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_save = QPushButton(self.widget)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout.addWidget(self.btn_save)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btn_cancel = QPushButton(self.widget)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout.setStretch(0, 20)
        self.verticalLayout.setStretch(1, 40)
        self.verticalLayout.setStretch(2, 40)
        self.verticalLayout.setStretch(3, 10)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8bbe\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u6570\u636e\u6e90\u7c7b\u578b", None))
        self.radio_serial.setText(QCoreApplication.translate("Dialog", u"\u4e32\u53e3", None))
        self.radio_gprs.setText(QCoreApplication.translate("Dialog", u"4G\u6a21\u5757", None))
        self.group_serial.setTitle(QCoreApplication.translate("Dialog", u"\u4e32\u53e3\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6ce2\u7279\u7387", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u8d85\u65f6\u65f6\u95f4", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u4e32\u53e3\u53f7", None))
        self.group_gprs.setTitle(QCoreApplication.translate("Dialog", u"4G\u6a21\u5757\u8bbe\u7f6e", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u7aef\u53e3", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u670d\u52a1\u5668IP", None))
        self.edit_gprs_host.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u8d85\u65f6\u65f6\u95f4", None))
        self.btn_save.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

