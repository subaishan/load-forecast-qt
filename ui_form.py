# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QSizePolicy,
    QStatusBar, QToolButton, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1093, 666)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, -1, 3)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.label_title, 0, 1, 1, 1)

        self.btn_settings = QToolButton(self.frame)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/setting.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_settings.setIcon(icon)
        self.btn_settings.setIconSize(QSize(32, 32))

        self.gridLayout_9.addWidget(self.btn_settings, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setSizeIncrement(QSize(0, 0))
        self.widget.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rightGroupBox = QGroupBox(self.frame_2)
        self.rightGroupBox.setObjectName(u"rightGroupBox")
        font1 = QFont()
        font1.setPointSize(12)
        self.rightGroupBox.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.rightGroupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.plotWidget = PlotWidget(self.rightGroupBox)
        self.plotWidget.setObjectName(u"plotWidget")

        self.gridLayout_3.addWidget(self.plotWidget, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.rightGroupBox, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.leftGroupBox = QGroupBox(self.frame_3)
        self.leftGroupBox.setObjectName(u"leftGroupBox")
        self.leftGroupBox.setFont(font1)
        self.verticalLayout_3 = QVBoxLayout(self.leftGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(self.leftGroupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(258, 81))
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"image: url(:/icons/V.png);")

        self.gridLayout.addWidget(self.label_2, 0, 3, 3, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_voltage = QLabel(self.groupBox_2)
        self.label_voltage.setObjectName(u"label_voltage")

        self.gridLayout.addWidget(self.label_voltage, 2, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.leftGroupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(258, 81))
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 0, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"image: url(:/icons/A.png);")

        self.gridLayout_4.addWidget(self.label_6, 0, 4, 2, 1)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 1, 2, 1, 1)

        self.label_current = QLabel(self.groupBox_3)
        self.label_current.setObjectName(u"label_current")

        self.gridLayout_4.addWidget(self.label_current, 1, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.leftGroupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(258, 80))
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"image: url(:/icons/S_W.png);")

        self.gridLayout_6.addWidget(self.label_10, 0, 5, 4, 1)

        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_6.addWidget(self.label_11, 0, 4, 1, 1)

        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 2, 3, 1, 1)

        self.label_power = QLabel(self.groupBox_4)
        self.label_power.setObjectName(u"label_power")

        self.gridLayout_6.addWidget(self.label_power, 2, 4, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.leftGroupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(258, 81))
        self.gridLayout_7 = QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_17 = QLabel(self.groupBox_6)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_7.addWidget(self.label_17, 2, 2, 1, 1)

        self.label_energy = QLabel(self.groupBox_6)
        self.label_energy.setObjectName(u"label_energy")

        self.gridLayout_7.addWidget(self.label_energy, 2, 3, 1, 1)

        self.label_15 = QLabel(self.groupBox_6)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_7.addWidget(self.label_15, 1, 3, 1, 1)

        self.label_14 = QLabel(self.groupBox_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"image: url(:/icons/H_W.png);")

        self.gridLayout_7.addWidget(self.label_14, 1, 4, 2, 1)


        self.verticalLayout_3.addWidget(self.groupBox_6)

        self.groupBox = QGroupBox(self.leftGroupBox)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(258, 81))
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_power_15min = QLabel(self.groupBox)
        self.label_power_15min.setObjectName(u"label_power_15min")

        self.gridLayout_5.addWidget(self.label_power_15min, 2, 4, 1, 1)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.gridLayout_5.addWidget(self.label_19, 1, 4, 1, 1)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"image: url(:/icons/D_W_15.png);")

        self.gridLayout_5.addWidget(self.label_18, 1, 5, 2, 1)

        self.label_21 = QLabel(self.groupBox)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_5.addWidget(self.label_21, 2, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_5 = QGroupBox(self.leftGroupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(258, 81))
        self.gridLayout_8 = QGridLayout(self.groupBox_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_22 = QLabel(self.groupBox_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"image: url(:/icons/D_W_60.png);")

        self.gridLayout_8.addWidget(self.label_22, 0, 4, 2, 1)

        self.label_25 = QLabel(self.groupBox_5)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_8.addWidget(self.label_25, 1, 2, 1, 1)

        self.label_power_60min = QLabel(self.groupBox_5)
        self.label_power_60min.setObjectName(u"label_power_60min")

        self.gridLayout_8.addWidget(self.label_power_60min, 1, 3, 1, 1)

        self.label_23 = QLabel(self.groupBox_5)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_8.addWidget(self.label_23, 0, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_5)


        self.verticalLayout_2.addWidget(self.leftGroupBox)


        self.horizontalLayout.addWidget(self.frame_3)

        self.horizontalLayout.setStretch(0, 56)
        self.horizontalLayout.setStretch(1, 22)

        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout.setStretch(1, 92)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7535\u8d1f\u8377\u9884\u6d4b\u7cfb\u7edf1", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"\u7535\u8d1f\u8377\u9884\u6d4b\u7cfb\u7edf", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.rightGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u7535\u8d1f\u8377\u66f2\u7ebf", None))
        self.leftGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u7528\u7535\u53c2\u6570", None))
        self.groupBox_2.setTitle("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7535\u538b", None))
        self.label_voltage.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.groupBox_3.setTitle("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u7535\u6d41", None))
        self.label_6.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_current.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_4.setTitle("")
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u529f\u7387", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.label_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_6.setTitle("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"kWh", None))
        self.label_energy.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u7d2f\u79ef\u7528\u7535\u91cf", None))
        self.label_14.setText("")
        self.groupBox.setTitle("")
        self.label_power_15min.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"15\u5206\u949f\u540e\u529f\u7387", None))
        self.label_18.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.groupBox_5.setTitle("")
        self.label_22.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.label_power_60min.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"1\u5c0f\u65f6\u540e\u529f\u7387", None))
    # retranslateUi

