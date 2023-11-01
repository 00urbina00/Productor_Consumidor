# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1680, 898)
        MainWindow.setMinimumSize(QSize(1680, 894))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.gridLayout_9 = QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_1 = QFrame(self.centralwidget)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setStyleSheet(u"background-color: rgb(190, 190, 190);")
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_3 = QGroupBox(self.frame_1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(500, 250))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.groupBox_3.setFlat(True)
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame = QFrame(self.groupBox_4)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 400))
        self.frame.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.line_63 = QFrame(self.frame)
        self.line_63.setObjectName(u"line_63")
        self.line_63.setFrameShape(QFrame.HLine)
        self.line_63.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_63)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 25))
        self.label_7.setMaximumSize(QSize(16777215, 25))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_7)

        self.line_62 = QFrame(self.frame)
        self.line_62.setObjectName(u"line_62")
        self.line_62.setFrameShape(QFrame.HLine)
        self.line_62.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_62)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 25))
        self.progressBar.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_2.addWidget(self.progressBar)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.line_60 = QFrame(self.frame)
        self.line_60.setObjectName(u"line_60")
        self.line_60.setFrameShape(QFrame.HLine)
        self.line_60.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_60)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Enum_contenedor = QGroupBox(self.frame)
        self.Enum_contenedor.setObjectName(u"Enum_contenedor")
        self.Enum_contenedor.setMinimumSize(QSize(1584, 30))
        self.Enum_contenedor.setMaximumSize(QSize(1836, 35))
        self.Enum_contenedor.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.horizontalLayout_2 = QHBoxLayout(self.Enum_contenedor)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_61 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_61)

        self.taco_0_1 = QLabel(self.Enum_contenedor)
        self.taco_0_1.setObjectName(u"taco_0_1")
        self.taco_0_1.setMinimumSize(QSize(47, 10))
        self.taco_0_1.setMaximumSize(QSize(47, 20))
        self.taco_0_1.setFrameShadow(QFrame.Plain)
        self.taco_0_1.setScaledContents(True)
        self.taco_0_1.setAlignment(Qt.AlignCenter)
        self.taco_0_1.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_1)

        self.horizontalSpacer_62 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_62)

        self.line_40 = QFrame(self.Enum_contenedor)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setFrameShape(QFrame.VLine)
        self.line_40.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_40)

        self.horizontalSpacer_63 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_63)

        self.taco_0_2 = QLabel(self.Enum_contenedor)
        self.taco_0_2.setObjectName(u"taco_0_2")
        self.taco_0_2.setMinimumSize(QSize(47, 20))
        self.taco_0_2.setMaximumSize(QSize(47, 20))
        self.taco_0_2.setFrameShadow(QFrame.Plain)
        self.taco_0_2.setScaledContents(True)
        self.taco_0_2.setAlignment(Qt.AlignCenter)
        self.taco_0_2.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_2)

        self.horizontalSpacer_64 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_64)

        self.line_41 = QFrame(self.Enum_contenedor)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setFrameShape(QFrame.VLine)
        self.line_41.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_41)

        self.horizontalSpacer_65 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_65)

        self.taco_0_3 = QLabel(self.Enum_contenedor)
        self.taco_0_3.setObjectName(u"taco_0_3")
        self.taco_0_3.setMinimumSize(QSize(47, 20))
        self.taco_0_3.setMaximumSize(QSize(47, 20))
        self.taco_0_3.setFrameShadow(QFrame.Plain)
        self.taco_0_3.setScaledContents(True)
        self.taco_0_3.setAlignment(Qt.AlignCenter)
        self.taco_0_3.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_3)

        self.horizontalSpacer_66 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_66)

        self.line_42 = QFrame(self.Enum_contenedor)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setFrameShape(QFrame.VLine)
        self.line_42.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_42)

        self.horizontalSpacer_67 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_67)

        self.taco_0_4 = QLabel(self.Enum_contenedor)
        self.taco_0_4.setObjectName(u"taco_0_4")
        self.taco_0_4.setMinimumSize(QSize(47, 20))
        self.taco_0_4.setMaximumSize(QSize(47, 20))
        self.taco_0_4.setFrameShadow(QFrame.Plain)
        self.taco_0_4.setScaledContents(True)
        self.taco_0_4.setAlignment(Qt.AlignCenter)
        self.taco_0_4.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_4)

        self.horizontalSpacer_68 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_68)

        self.line_43 = QFrame(self.Enum_contenedor)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setFrameShape(QFrame.VLine)
        self.line_43.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_43)

        self.horizontalSpacer_69 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_69)

        self.taco_0_5 = QLabel(self.Enum_contenedor)
        self.taco_0_5.setObjectName(u"taco_0_5")
        self.taco_0_5.setMinimumSize(QSize(47, 20))
        self.taco_0_5.setMaximumSize(QSize(47, 20))
        self.taco_0_5.setFrameShadow(QFrame.Plain)
        self.taco_0_5.setScaledContents(True)
        self.taco_0_5.setAlignment(Qt.AlignCenter)
        self.taco_0_5.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_5)

        self.horizontalSpacer_70 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_70)

        self.line_44 = QFrame(self.Enum_contenedor)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setFrameShape(QFrame.VLine)
        self.line_44.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_44)

        self.horizontalSpacer_71 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_71)

        self.taco_0_6 = QLabel(self.Enum_contenedor)
        self.taco_0_6.setObjectName(u"taco_0_6")
        self.taco_0_6.setMinimumSize(QSize(47, 20))
        self.taco_0_6.setMaximumSize(QSize(47, 20))
        self.taco_0_6.setFrameShadow(QFrame.Plain)
        self.taco_0_6.setScaledContents(True)
        self.taco_0_6.setAlignment(Qt.AlignCenter)
        self.taco_0_6.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_6)

        self.horizontalSpacer_72 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_72)

        self.line_45 = QFrame(self.Enum_contenedor)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setFrameShape(QFrame.VLine)
        self.line_45.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_45)

        self.horizontalSpacer_73 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_73)

        self.taco_0_7 = QLabel(self.Enum_contenedor)
        self.taco_0_7.setObjectName(u"taco_0_7")
        self.taco_0_7.setMinimumSize(QSize(47, 20))
        self.taco_0_7.setMaximumSize(QSize(47, 20))
        self.taco_0_7.setFrameShadow(QFrame.Plain)
        self.taco_0_7.setScaledContents(True)
        self.taco_0_7.setAlignment(Qt.AlignCenter)
        self.taco_0_7.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_7)

        self.horizontalSpacer_74 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_74)

        self.line_46 = QFrame(self.Enum_contenedor)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setFrameShape(QFrame.VLine)
        self.line_46.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_46)

        self.horizontalSpacer_75 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_75)

        self.taco_0_8 = QLabel(self.Enum_contenedor)
        self.taco_0_8.setObjectName(u"taco_0_8")
        self.taco_0_8.setMinimumSize(QSize(47, 20))
        self.taco_0_8.setMaximumSize(QSize(47, 20))
        self.taco_0_8.setFrameShadow(QFrame.Plain)
        self.taco_0_8.setScaledContents(True)
        self.taco_0_8.setAlignment(Qt.AlignCenter)
        self.taco_0_8.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_8)

        self.horizontalSpacer_76 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_76)

        self.line_47 = QFrame(self.Enum_contenedor)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setFrameShape(QFrame.VLine)
        self.line_47.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_47)

        self.horizontalSpacer_77 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_77)

        self.taco_0_9 = QLabel(self.Enum_contenedor)
        self.taco_0_9.setObjectName(u"taco_0_9")
        self.taco_0_9.setMinimumSize(QSize(47, 20))
        self.taco_0_9.setMaximumSize(QSize(47, 20))
        self.taco_0_9.setFrameShadow(QFrame.Plain)
        self.taco_0_9.setScaledContents(True)
        self.taco_0_9.setAlignment(Qt.AlignCenter)
        self.taco_0_9.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_9)

        self.horizontalSpacer_78 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_78)

        self.line_48 = QFrame(self.Enum_contenedor)
        self.line_48.setObjectName(u"line_48")
        self.line_48.setFrameShape(QFrame.VLine)
        self.line_48.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_48)

        self.horizontalSpacer_79 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_79)

        self.taco_0_10 = QLabel(self.Enum_contenedor)
        self.taco_0_10.setObjectName(u"taco_0_10")
        self.taco_0_10.setMinimumSize(QSize(47, 20))
        self.taco_0_10.setMaximumSize(QSize(47, 20))
        self.taco_0_10.setFrameShadow(QFrame.Plain)
        self.taco_0_10.setScaledContents(True)
        self.taco_0_10.setAlignment(Qt.AlignCenter)
        self.taco_0_10.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_10)

        self.horizontalSpacer_80 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_80)

        self.line_49 = QFrame(self.Enum_contenedor)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setFrameShape(QFrame.VLine)
        self.line_49.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_49)

        self.horizontalSpacer_81 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_81)

        self.taco_0_11 = QLabel(self.Enum_contenedor)
        self.taco_0_11.setObjectName(u"taco_0_11")
        self.taco_0_11.setMinimumSize(QSize(47, 20))
        self.taco_0_11.setMaximumSize(QSize(47, 20))
        self.taco_0_11.setFrameShadow(QFrame.Plain)
        self.taco_0_11.setScaledContents(True)
        self.taco_0_11.setAlignment(Qt.AlignCenter)
        self.taco_0_11.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_11)

        self.horizontalSpacer_82 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_82)

        self.line_50 = QFrame(self.Enum_contenedor)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setFrameShape(QFrame.VLine)
        self.line_50.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_50)

        self.horizontalSpacer_83 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_83)

        self.taco_0_12 = QLabel(self.Enum_contenedor)
        self.taco_0_12.setObjectName(u"taco_0_12")
        self.taco_0_12.setMinimumSize(QSize(47, 20))
        self.taco_0_12.setMaximumSize(QSize(47, 20))
        self.taco_0_12.setFrameShadow(QFrame.Plain)
        self.taco_0_12.setScaledContents(True)
        self.taco_0_12.setAlignment(Qt.AlignCenter)
        self.taco_0_12.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_12)

        self.horizontalSpacer_84 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_84)

        self.line_51 = QFrame(self.Enum_contenedor)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setFrameShape(QFrame.VLine)
        self.line_51.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_51)

        self.horizontalSpacer_85 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_85)

        self.taco_0_13 = QLabel(self.Enum_contenedor)
        self.taco_0_13.setObjectName(u"taco_0_13")
        self.taco_0_13.setMinimumSize(QSize(47, 20))
        self.taco_0_13.setMaximumSize(QSize(47, 20))
        self.taco_0_13.setFrameShadow(QFrame.Plain)
        self.taco_0_13.setScaledContents(True)
        self.taco_0_13.setAlignment(Qt.AlignCenter)
        self.taco_0_13.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_13)

        self.horizontalSpacer_86 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_86)

        self.line_52 = QFrame(self.Enum_contenedor)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setFrameShape(QFrame.VLine)
        self.line_52.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_52)

        self.horizontalSpacer_87 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_87)

        self.taco_0_14 = QLabel(self.Enum_contenedor)
        self.taco_0_14.setObjectName(u"taco_0_14")
        self.taco_0_14.setMinimumSize(QSize(47, 20))
        self.taco_0_14.setMaximumSize(QSize(47, 20))
        self.taco_0_14.setFrameShadow(QFrame.Plain)
        self.taco_0_14.setScaledContents(True)
        self.taco_0_14.setAlignment(Qt.AlignCenter)
        self.taco_0_14.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_14)

        self.horizontalSpacer_88 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_88)

        self.line_53 = QFrame(self.Enum_contenedor)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setFrameShape(QFrame.VLine)
        self.line_53.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_53)

        self.horizontalSpacer_89 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_89)

        self.taco_0_15 = QLabel(self.Enum_contenedor)
        self.taco_0_15.setObjectName(u"taco_0_15")
        self.taco_0_15.setMinimumSize(QSize(47, 20))
        self.taco_0_15.setMaximumSize(QSize(47, 20))
        self.taco_0_15.setFrameShadow(QFrame.Plain)
        self.taco_0_15.setScaledContents(True)
        self.taco_0_15.setAlignment(Qt.AlignCenter)
        self.taco_0_15.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_15)

        self.horizontalSpacer_90 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_90)

        self.line_54 = QFrame(self.Enum_contenedor)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setFrameShape(QFrame.VLine)
        self.line_54.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_54)

        self.horizontalSpacer_91 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_91)

        self.taco_0_16 = QLabel(self.Enum_contenedor)
        self.taco_0_16.setObjectName(u"taco_0_16")
        self.taco_0_16.setMinimumSize(QSize(47, 20))
        self.taco_0_16.setMaximumSize(QSize(47, 20))
        self.taco_0_16.setFrameShadow(QFrame.Plain)
        self.taco_0_16.setScaledContents(True)
        self.taco_0_16.setAlignment(Qt.AlignCenter)
        self.taco_0_16.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_16)

        self.horizontalSpacer_92 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_92)

        self.line_55 = QFrame(self.Enum_contenedor)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setFrameShape(QFrame.VLine)
        self.line_55.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_55)

        self.horizontalSpacer_93 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_93)

        self.taco_0_17 = QLabel(self.Enum_contenedor)
        self.taco_0_17.setObjectName(u"taco_0_17")
        self.taco_0_17.setMinimumSize(QSize(47, 20))
        self.taco_0_17.setMaximumSize(QSize(47, 20))
        self.taco_0_17.setFrameShadow(QFrame.Plain)
        self.taco_0_17.setScaledContents(True)
        self.taco_0_17.setAlignment(Qt.AlignCenter)
        self.taco_0_17.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_17)

        self.horizontalSpacer_94 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_94)

        self.line_56 = QFrame(self.Enum_contenedor)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setFrameShape(QFrame.VLine)
        self.line_56.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_56)

        self.horizontalSpacer_95 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_95)

        self.taco_0_18 = QLabel(self.Enum_contenedor)
        self.taco_0_18.setObjectName(u"taco_0_18")
        self.taco_0_18.setMinimumSize(QSize(47, 20))
        self.taco_0_18.setMaximumSize(QSize(47, 20))
        self.taco_0_18.setFrameShadow(QFrame.Plain)
        self.taco_0_18.setScaledContents(True)
        self.taco_0_18.setAlignment(Qt.AlignCenter)
        self.taco_0_18.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_18)

        self.horizontalSpacer_96 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_96)

        self.line_57 = QFrame(self.Enum_contenedor)
        self.line_57.setObjectName(u"line_57")
        self.line_57.setFrameShape(QFrame.VLine)
        self.line_57.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_57)

        self.horizontalSpacer_97 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_97)

        self.taco_0_19 = QLabel(self.Enum_contenedor)
        self.taco_0_19.setObjectName(u"taco_0_19")
        self.taco_0_19.setMinimumSize(QSize(47, 20))
        self.taco_0_19.setMaximumSize(QSize(47, 20))
        self.taco_0_19.setFrameShadow(QFrame.Plain)
        self.taco_0_19.setScaledContents(True)
        self.taco_0_19.setAlignment(Qt.AlignCenter)
        self.taco_0_19.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_19)

        self.line_58 = QFrame(self.Enum_contenedor)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setFrameShape(QFrame.VLine)
        self.line_58.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_58)

        self.horizontalSpacer_98 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_98)

        self.taco_0_20 = QLabel(self.Enum_contenedor)
        self.taco_0_20.setObjectName(u"taco_0_20")
        self.taco_0_20.setMinimumSize(QSize(47, 20))
        self.taco_0_20.setMaximumSize(QSize(47, 20))
        self.taco_0_20.setFrameShadow(QFrame.Plain)
        self.taco_0_20.setScaledContents(True)
        self.taco_0_20.setAlignment(Qt.AlignCenter)
        self.taco_0_20.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.taco_0_20)

        self.horizontalSpacer_99 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_99)


        self.verticalLayout_3.addWidget(self.Enum_contenedor)

        self.line_59 = QFrame(self.frame)
        self.line_59.setObjectName(u"line_59")
        self.line_59.setFrameShape(QFrame.HLine)
        self.line_59.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_59)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.Contenedor = QGroupBox(self.frame)
        self.Contenedor.setObjectName(u"Contenedor")
        self.Contenedor.setMinimumSize(QSize(1584, 50))
        self.Contenedor.setMaximumSize(QSize(1836, 100))
        self.Contenedor.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.Contenedor.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_36 = QHBoxLayout(self.Contenedor)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_40 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_40)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tacos_0 = QLabel(self.Contenedor)
        self.tacos_0.setObjectName(u"tacos_0")
        self.tacos_0.setMinimumSize(QSize(47, 50))
        self.tacos_0.setMaximumSize(QSize(47, 50))
        self.tacos_0.setFrameShadow(QFrame.Plain)
        self.tacos_0.setPixmap(QPixmap(u"taco.png"))
        self.tacos_0.setScaledContents(True)
        self.tacos_0.setAlignment(Qt.AlignCenter)
        self.tacos_0.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_8.addWidget(self.tacos_0)

        self.line_66 = QFrame(self.Contenedor)
        self.line_66.setObjectName(u"line_66")
        self.line_66.setFrameShape(QFrame.HLine)
        self.line_66.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_66)


        self.horizontalLayout_8.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_41 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_41)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_8)

        self.line_2 = QFrame(self.Contenedor)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_2)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_42 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_42)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tacos_1 = QLabel(self.Contenedor)
        self.tacos_1.setObjectName(u"tacos_1")
        self.tacos_1.setMinimumSize(QSize(47, 50))
        self.tacos_1.setMaximumSize(QSize(47, 50))
        self.tacos_1.setFrameShadow(QFrame.Plain)
        self.tacos_1.setPixmap(QPixmap(u"taco.png"))
        self.tacos_1.setScaledContents(True)
        self.tacos_1.setAlignment(Qt.AlignCenter)
        self.tacos_1.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_9.addWidget(self.tacos_1)

        self.line_67 = QFrame(self.Contenedor)
        self.line_67.setObjectName(u"line_67")
        self.line_67.setFrameShape(QFrame.HLine)
        self.line_67.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_67)


        self.horizontalLayout_15.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_43 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_43)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_15)

        self.line_4 = QFrame(self.Contenedor)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_4)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_46 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_46)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tacos_2 = QLabel(self.Contenedor)
        self.tacos_2.setObjectName(u"tacos_2")
        self.tacos_2.setMinimumSize(QSize(47, 50))
        self.tacos_2.setMaximumSize(QSize(47, 50))
        self.tacos_2.setFrameShadow(QFrame.Plain)
        self.tacos_2.setPixmap(QPixmap(u"taco.png"))
        self.tacos_2.setScaledContents(True)
        self.tacos_2.setAlignment(Qt.AlignCenter)
        self.tacos_2.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_11.addWidget(self.tacos_2)

        self.line_69 = QFrame(self.Contenedor)
        self.line_69.setObjectName(u"line_69")
        self.line_69.setFrameShape(QFrame.HLine)
        self.line_69.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_69)


        self.horizontalLayout_18.addLayout(self.verticalLayout_11)

        self.horizontalSpacer_47 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_47)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_18)

        self.line_5 = QFrame(self.Contenedor)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_5)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_48 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_48)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.tacos_3 = QLabel(self.Contenedor)
        self.tacos_3.setObjectName(u"tacos_3")
        self.tacos_3.setMinimumSize(QSize(47, 50))
        self.tacos_3.setMaximumSize(QSize(47, 50))
        self.tacos_3.setFrameShadow(QFrame.Plain)
        self.tacos_3.setPixmap(QPixmap(u"taco.png"))
        self.tacos_3.setScaledContents(True)
        self.tacos_3.setAlignment(Qt.AlignCenter)
        self.tacos_3.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_17.addWidget(self.tacos_3)

        self.line_70 = QFrame(self.Contenedor)
        self.line_70.setObjectName(u"line_70")
        self.line_70.setFrameShape(QFrame.HLine)
        self.line_70.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.line_70)


        self.horizontalLayout_19.addLayout(self.verticalLayout_17)

        self.horizontalSpacer_49 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_49)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_19)

        self.line_6 = QFrame(self.Contenedor)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_6)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_50 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_50)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.tacos_4 = QLabel(self.Contenedor)
        self.tacos_4.setObjectName(u"tacos_4")
        self.tacos_4.setMinimumSize(QSize(47, 50))
        self.tacos_4.setMaximumSize(QSize(47, 50))
        self.tacos_4.setFrameShadow(QFrame.Plain)
        self.tacos_4.setPixmap(QPixmap(u"taco.png"))
        self.tacos_4.setScaledContents(True)
        self.tacos_4.setAlignment(Qt.AlignCenter)
        self.tacos_4.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_18.addWidget(self.tacos_4)

        self.line_71 = QFrame(self.Contenedor)
        self.line_71.setObjectName(u"line_71")
        self.line_71.setFrameShape(QFrame.HLine)
        self.line_71.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_18.addWidget(self.line_71)


        self.horizontalLayout_20.addLayout(self.verticalLayout_18)

        self.horizontalSpacer_51 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_51)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_20)

        self.line_7 = QFrame(self.Contenedor)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_7)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_52 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_52)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.tacos_5 = QLabel(self.Contenedor)
        self.tacos_5.setObjectName(u"tacos_5")
        self.tacos_5.setMinimumSize(QSize(47, 50))
        self.tacos_5.setMaximumSize(QSize(47, 50))
        self.tacos_5.setFrameShadow(QFrame.Plain)
        self.tacos_5.setPixmap(QPixmap(u"taco.png"))
        self.tacos_5.setScaledContents(True)
        self.tacos_5.setAlignment(Qt.AlignCenter)
        self.tacos_5.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_19.addWidget(self.tacos_5)

        self.line_72 = QFrame(self.Contenedor)
        self.line_72.setObjectName(u"line_72")
        self.line_72.setFrameShape(QFrame.HLine)
        self.line_72.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_72)


        self.horizontalLayout_21.addLayout(self.verticalLayout_19)

        self.horizontalSpacer_53 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_53)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_21)

        self.line_8 = QFrame(self.Contenedor)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_8)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_54 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_54)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.tacos_6 = QLabel(self.Contenedor)
        self.tacos_6.setObjectName(u"tacos_6")
        self.tacos_6.setMinimumSize(QSize(47, 50))
        self.tacos_6.setMaximumSize(QSize(47, 50))
        self.tacos_6.setFrameShadow(QFrame.Plain)
        self.tacos_6.setPixmap(QPixmap(u"taco.png"))
        self.tacos_6.setScaledContents(True)
        self.tacos_6.setAlignment(Qt.AlignCenter)
        self.tacos_6.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_20.addWidget(self.tacos_6)

        self.line_73 = QFrame(self.Contenedor)
        self.line_73.setObjectName(u"line_73")
        self.line_73.setFrameShape(QFrame.HLine)
        self.line_73.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_20.addWidget(self.line_73)


        self.horizontalLayout_22.addLayout(self.verticalLayout_20)

        self.horizontalSpacer_55 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_55)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_22)

        self.line_9 = QFrame(self.Contenedor)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_9)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_56 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_56)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.tacos_7 = QLabel(self.Contenedor)
        self.tacos_7.setObjectName(u"tacos_7")
        self.tacos_7.setMinimumSize(QSize(47, 50))
        self.tacos_7.setMaximumSize(QSize(47, 50))
        self.tacos_7.setFrameShadow(QFrame.Plain)
        self.tacos_7.setPixmap(QPixmap(u"taco.png"))
        self.tacos_7.setScaledContents(True)
        self.tacos_7.setAlignment(Qt.AlignCenter)
        self.tacos_7.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_21.addWidget(self.tacos_7)

        self.line_74 = QFrame(self.Contenedor)
        self.line_74.setObjectName(u"line_74")
        self.line_74.setFrameShape(QFrame.HLine)
        self.line_74.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_21.addWidget(self.line_74)


        self.horizontalLayout_23.addLayout(self.verticalLayout_21)

        self.horizontalSpacer_57 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_57)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_23)

        self.line_10 = QFrame(self.Contenedor)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_10)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_58 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_58)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.tacos_8 = QLabel(self.Contenedor)
        self.tacos_8.setObjectName(u"tacos_8")
        self.tacos_8.setMinimumSize(QSize(47, 50))
        self.tacos_8.setMaximumSize(QSize(47, 50))
        self.tacos_8.setFrameShadow(QFrame.Plain)
        self.tacos_8.setPixmap(QPixmap(u"taco.png"))
        self.tacos_8.setScaledContents(True)
        self.tacos_8.setAlignment(Qt.AlignCenter)
        self.tacos_8.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_22.addWidget(self.tacos_8)

        self.line_75 = QFrame(self.Contenedor)
        self.line_75.setObjectName(u"line_75")
        self.line_75.setFrameShape(QFrame.HLine)
        self.line_75.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_22.addWidget(self.line_75)


        self.horizontalLayout_24.addLayout(self.verticalLayout_22)

        self.horizontalSpacer_59 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_59)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_24)

        self.line_11 = QFrame(self.Contenedor)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_11)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_60 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_60)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.tacos_9 = QLabel(self.Contenedor)
        self.tacos_9.setObjectName(u"tacos_9")
        self.tacos_9.setMinimumSize(QSize(47, 50))
        self.tacos_9.setMaximumSize(QSize(47, 50))
        self.tacos_9.setFrameShadow(QFrame.Plain)
        self.tacos_9.setPixmap(QPixmap(u"taco.png"))
        self.tacos_9.setScaledContents(True)
        self.tacos_9.setAlignment(Qt.AlignCenter)
        self.tacos_9.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_23.addWidget(self.tacos_9)

        self.line_76 = QFrame(self.Contenedor)
        self.line_76.setObjectName(u"line_76")
        self.line_76.setFrameShape(QFrame.HLine)
        self.line_76.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_23.addWidget(self.line_76)


        self.horizontalLayout_25.addLayout(self.verticalLayout_23)

        self.horizontalSpacer_100 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_100)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_25)

        self.line_12 = QFrame(self.Contenedor)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_12)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_101 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_101)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.tacos_10 = QLabel(self.Contenedor)
        self.tacos_10.setObjectName(u"tacos_10")
        self.tacos_10.setMinimumSize(QSize(47, 50))
        self.tacos_10.setMaximumSize(QSize(47, 50))
        self.tacos_10.setFrameShadow(QFrame.Plain)
        self.tacos_10.setPixmap(QPixmap(u"taco.png"))
        self.tacos_10.setScaledContents(True)
        self.tacos_10.setAlignment(Qt.AlignCenter)
        self.tacos_10.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_24.addWidget(self.tacos_10)

        self.line_77 = QFrame(self.Contenedor)
        self.line_77.setObjectName(u"line_77")
        self.line_77.setFrameShape(QFrame.HLine)
        self.line_77.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_24.addWidget(self.line_77)


        self.horizontalLayout_26.addLayout(self.verticalLayout_24)

        self.horizontalSpacer_102 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_102)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_26)

        self.line_13 = QFrame(self.Contenedor)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_13)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_103 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_103)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.tacos_11 = QLabel(self.Contenedor)
        self.tacos_11.setObjectName(u"tacos_11")
        self.tacos_11.setMinimumSize(QSize(47, 50))
        self.tacos_11.setMaximumSize(QSize(47, 50))
        self.tacos_11.setFrameShadow(QFrame.Plain)
        self.tacos_11.setPixmap(QPixmap(u"taco.png"))
        self.tacos_11.setScaledContents(True)
        self.tacos_11.setAlignment(Qt.AlignCenter)
        self.tacos_11.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_25.addWidget(self.tacos_11)

        self.line_78 = QFrame(self.Contenedor)
        self.line_78.setObjectName(u"line_78")
        self.line_78.setFrameShape(QFrame.HLine)
        self.line_78.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_25.addWidget(self.line_78)


        self.horizontalLayout_27.addLayout(self.verticalLayout_25)

        self.horizontalSpacer_104 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_104)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_27)

        self.line_14 = QFrame(self.Contenedor)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_14)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_105 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_105)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.tacos_12 = QLabel(self.Contenedor)
        self.tacos_12.setObjectName(u"tacos_12")
        self.tacos_12.setMinimumSize(QSize(47, 50))
        self.tacos_12.setMaximumSize(QSize(47, 50))
        self.tacos_12.setFrameShadow(QFrame.Plain)
        self.tacos_12.setPixmap(QPixmap(u"taco.png"))
        self.tacos_12.setScaledContents(True)
        self.tacos_12.setAlignment(Qt.AlignCenter)
        self.tacos_12.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_26.addWidget(self.tacos_12)

        self.line_79 = QFrame(self.Contenedor)
        self.line_79.setObjectName(u"line_79")
        self.line_79.setFrameShape(QFrame.HLine)
        self.line_79.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_26.addWidget(self.line_79)


        self.horizontalLayout_28.addLayout(self.verticalLayout_26)

        self.horizontalSpacer_106 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_106)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_28)

        self.line_15 = QFrame(self.Contenedor)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.VLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_15)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_107 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_107)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.tacos_13 = QLabel(self.Contenedor)
        self.tacos_13.setObjectName(u"tacos_13")
        self.tacos_13.setMinimumSize(QSize(47, 50))
        self.tacos_13.setMaximumSize(QSize(47, 50))
        self.tacos_13.setFrameShadow(QFrame.Plain)
        self.tacos_13.setPixmap(QPixmap(u"taco.png"))
        self.tacos_13.setScaledContents(True)
        self.tacos_13.setAlignment(Qt.AlignCenter)
        self.tacos_13.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_27.addWidget(self.tacos_13)

        self.line_80 = QFrame(self.Contenedor)
        self.line_80.setObjectName(u"line_80")
        self.line_80.setFrameShape(QFrame.HLine)
        self.line_80.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line_80)


        self.horizontalLayout_29.addLayout(self.verticalLayout_27)

        self.horizontalSpacer_108 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_108)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_29)

        self.line_16 = QFrame(self.Contenedor)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.VLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_16)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_109 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_109)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.tacos_14 = QLabel(self.Contenedor)
        self.tacos_14.setObjectName(u"tacos_14")
        self.tacos_14.setMinimumSize(QSize(47, 50))
        self.tacos_14.setMaximumSize(QSize(47, 50))
        self.tacos_14.setFrameShadow(QFrame.Plain)
        self.tacos_14.setPixmap(QPixmap(u"taco.png"))
        self.tacos_14.setScaledContents(True)
        self.tacos_14.setAlignment(Qt.AlignCenter)
        self.tacos_14.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_28.addWidget(self.tacos_14)

        self.line_81 = QFrame(self.Contenedor)
        self.line_81.setObjectName(u"line_81")
        self.line_81.setFrameShape(QFrame.HLine)
        self.line_81.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_28.addWidget(self.line_81)


        self.horizontalLayout_30.addLayout(self.verticalLayout_28)

        self.horizontalSpacer_110 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_110)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_30)

        self.line_17 = QFrame(self.Contenedor)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.VLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_17)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_111 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_111)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.tacos_15 = QLabel(self.Contenedor)
        self.tacos_15.setObjectName(u"tacos_15")
        self.tacos_15.setMinimumSize(QSize(47, 50))
        self.tacos_15.setMaximumSize(QSize(47, 50))
        self.tacos_15.setFrameShadow(QFrame.Plain)
        self.tacos_15.setPixmap(QPixmap(u"taco.png"))
        self.tacos_15.setScaledContents(True)
        self.tacos_15.setAlignment(Qt.AlignCenter)
        self.tacos_15.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_29.addWidget(self.tacos_15)

        self.line_82 = QFrame(self.Contenedor)
        self.line_82.setObjectName(u"line_82")
        self.line_82.setFrameShape(QFrame.HLine)
        self.line_82.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_29.addWidget(self.line_82)


        self.horizontalLayout_31.addLayout(self.verticalLayout_29)

        self.horizontalSpacer_112 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_112)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_31)

        self.line_18 = QFrame(self.Contenedor)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.VLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_18)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalSpacer_113 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_113)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.tacos_16 = QLabel(self.Contenedor)
        self.tacos_16.setObjectName(u"tacos_16")
        self.tacos_16.setMinimumSize(QSize(47, 50))
        self.tacos_16.setMaximumSize(QSize(47, 50))
        self.tacos_16.setFrameShadow(QFrame.Plain)
        self.tacos_16.setPixmap(QPixmap(u"taco.png"))
        self.tacos_16.setScaledContents(True)
        self.tacos_16.setAlignment(Qt.AlignCenter)
        self.tacos_16.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_30.addWidget(self.tacos_16)

        self.line_83 = QFrame(self.Contenedor)
        self.line_83.setObjectName(u"line_83")
        self.line_83.setFrameShape(QFrame.HLine)
        self.line_83.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_30.addWidget(self.line_83)


        self.horizontalLayout_32.addLayout(self.verticalLayout_30)

        self.horizontalSpacer_114 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_114)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_32)

        self.line_19 = QFrame(self.Contenedor)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.VLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_19)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalSpacer_115 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_115)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.tacos_17 = QLabel(self.Contenedor)
        self.tacos_17.setObjectName(u"tacos_17")
        self.tacos_17.setMinimumSize(QSize(47, 50))
        self.tacos_17.setMaximumSize(QSize(47, 50))
        self.tacos_17.setFrameShadow(QFrame.Plain)
        self.tacos_17.setPixmap(QPixmap(u"taco.png"))
        self.tacos_17.setScaledContents(True)
        self.tacos_17.setAlignment(Qt.AlignCenter)
        self.tacos_17.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_31.addWidget(self.tacos_17)

        self.line_84 = QFrame(self.Contenedor)
        self.line_84.setObjectName(u"line_84")
        self.line_84.setFrameShape(QFrame.HLine)
        self.line_84.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_84)


        self.horizontalLayout_33.addLayout(self.verticalLayout_31)

        self.horizontalSpacer_116 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_116)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_33)

        self.line_20 = QFrame(self.Contenedor)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.VLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_20)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalSpacer_117 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_117)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.tacos_18 = QLabel(self.Contenedor)
        self.tacos_18.setObjectName(u"tacos_18")
        self.tacos_18.setMinimumSize(QSize(47, 50))
        self.tacos_18.setMaximumSize(QSize(47, 50))
        self.tacos_18.setFrameShadow(QFrame.Plain)
        self.tacos_18.setPixmap(QPixmap(u"taco.png"))
        self.tacos_18.setScaledContents(True)
        self.tacos_18.setAlignment(Qt.AlignCenter)
        self.tacos_18.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_32.addWidget(self.tacos_18)

        self.line_85 = QFrame(self.Contenedor)
        self.line_85.setObjectName(u"line_85")
        self.line_85.setFrameShape(QFrame.HLine)
        self.line_85.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_32.addWidget(self.line_85)


        self.horizontalLayout_34.addLayout(self.verticalLayout_32)

        self.horizontalSpacer_118 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_118)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_34)

        self.line_87 = QFrame(self.Contenedor)
        self.line_87.setObjectName(u"line_87")
        self.line_87.setFrameShape(QFrame.VLine)
        self.line_87.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_36.addWidget(self.line_87)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalSpacer_119 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_119)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.tacos_19 = QLabel(self.Contenedor)
        self.tacos_19.setObjectName(u"tacos_19")
        self.tacos_19.setMinimumSize(QSize(47, 50))
        self.tacos_19.setMaximumSize(QSize(47, 50))
        self.tacos_19.setFrameShadow(QFrame.Plain)
        self.tacos_19.setPixmap(QPixmap(u"taco.png"))
        self.tacos_19.setScaledContents(True)
        self.tacos_19.setAlignment(Qt.AlignCenter)
        self.tacos_19.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_33.addWidget(self.tacos_19)

        self.line_86 = QFrame(self.Contenedor)
        self.line_86.setObjectName(u"line_86")
        self.line_86.setFrameShape(QFrame.HLine)
        self.line_86.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_33.addWidget(self.line_86)


        self.horizontalLayout_35.addLayout(self.verticalLayout_33)

        self.horizontalSpacer_120 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_120)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_35)


        self.verticalLayout_5.addWidget(self.Contenedor)

        self.line_61 = QFrame(self.frame)
        self.line_61.setObjectName(u"line_61")
        self.line_61.setFrameShape(QFrame.HLine)
        self.line_61.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_61)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_start = QPushButton(self.frame_5)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMaximumSize(QSize(85, 35))
        self.btn_start.setStyleSheet(u"QPushButton{\n"
"\n"
"border:round;\n"
"\n"
"}\n"
"QPushButton:Pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(230, 230, 230);\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u"5200000.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_start.setIcon(icon)
        self.btn_start.setIconSize(QSize(80, 80))

        self.horizontalLayout_3.addWidget(self.btn_start)

        self.horizontalSpacer_2 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_16.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_43 = QLabel(self.frame_5)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(106, 30))
        self.label_43.setMaximumSize(QSize(106, 30))
        self.label_43.setFont(font)
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_43)

        self.ledt_turn = QLineEdit(self.frame_5)
        self.ledt_turn.setObjectName(u"ledt_turn")
        self.ledt_turn.setMinimumSize(QSize(106, 25))
        self.ledt_turn.setMaximumSize(QSize(106, 25))
        self.ledt_turn.setFont(font)
        self.ledt_turn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.ledt_turn.setFrame(False)
        self.ledt_turn.setAlignment(Qt.AlignCenter)
        self.ledt_turn.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.ledt_turn)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_21 = QSpacerItem(18, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_21)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_44 = QLabel(self.frame_5)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(106, 30))
        self.label_44.setMaximumSize(QSize(106, 30))
        self.label_44.setFont(font)
        self.label_44.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_44)

        self.ledt_number_products = QLineEdit(self.frame_5)
        self.ledt_number_products.setObjectName(u"ledt_number_products")
        self.ledt_number_products.setMinimumSize(QSize(106, 25))
        self.ledt_number_products.setMaximumSize(QSize(106, 25))
        self.ledt_number_products.setFont(font)
        self.ledt_number_products.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.ledt_number_products.setFrame(False)
        self.ledt_number_products.setAlignment(Qt.AlignCenter)
        self.ledt_number_products.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.ledt_number_products)


        self.horizontalLayout_4.addLayout(self.verticalLayout_10)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_16.addLayout(self.horizontalLayout_4)

        self.line_65 = QFrame(self.frame_5)
        self.line_65.setObjectName(u"line_65")
        self.line_65.setFrameShape(QFrame.HLine)
        self.line_65.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_16.addWidget(self.line_65)


        self.verticalLayout_5.addWidget(self.frame_5)


        self.gridLayout_6.addWidget(self.frame, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_4, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_3, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_1, 0, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line, 1, 0, 1, 1)

        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_9)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame_9)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(600, 0))
        self.frame_2.setMaximumSize(QSize(800, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(190, 190, 190);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(100, 50))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_6 = QFrame(self.groupBox)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(700, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_17)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(81, 61))
        self.label_5.setMaximumSize(QSize(81, 61))
        self.label_5.setPixmap(QPixmap(u"1830839.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.horizontalSpacer_5 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.gridLayout_7.addWidget(self.frame_6, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.groupBox)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(0, 81))
        self.groupBox_7.setMaximumSize(QSize(700, 100))
        self.groupBox_7.setFlat(True)
        self.gridLayout_12 = QGridLayout(self.groupBox_7)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_6 = QSpacerItem(188, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.frame_10 = QFrame(self.groupBox_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(71, 71))
        self.frame_10.setMaximumSize(QSize(71, 71))
        self.frame_10.setSizeIncrement(QSize(0, 0))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.lbl_p_sleep = QLabel(self.frame_10)
        self.lbl_p_sleep.setObjectName(u"lbl_p_sleep")
        self.lbl_p_sleep.setEnabled(True)
        self.lbl_p_sleep.setGeometry(QRect(7, 9, 51, 51))
        self.lbl_p_sleep.setMinimumSize(QSize(51, 51))
        self.lbl_p_sleep.setMaximumSize(QSize(51, 51))
        self.lbl_p_sleep.setAutoFillBackground(False)
        self.lbl_p_sleep.setFrameShape(QFrame.NoFrame)
        self.lbl_p_sleep.setPixmap(QPixmap(u"4419495.png"))
        self.lbl_p_sleep.setScaledContents(True)
        self.lbl_p_sleep.setAlignment(Qt.AlignCenter)
        self.lbl_p_work = QLabel(self.frame_10)
        self.lbl_p_work.setObjectName(u"lbl_p_work")
        self.lbl_p_work.setEnabled(True)
        self.lbl_p_work.setGeometry(QRect(7, 9, 51, 51))
        self.lbl_p_work.setMinimumSize(QSize(51, 51))
        self.lbl_p_work.setMaximumSize(QSize(51, 51))
        self.lbl_p_work.setPixmap(QPixmap(u"10277807.png"))
        self.lbl_p_work.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.frame_10)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)


        self.horizontalLayout_10.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_7 = QSpacerItem(188, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)


        self.gridLayout_12.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_7, 1, 0, 1, 1)

        self.groupBox_52 = QGroupBox(self.groupBox)
        self.groupBox_52.setObjectName(u"groupBox_52")
        self.groupBox_52.setMinimumSize(QSize(500, 81))
        self.groupBox_52.setMaximumSize(QSize(700, 16777215))
        self.groupBox_52.setFont(font)
        self.groupBox_52.setAlignment(Qt.AlignCenter)
        self.groupBox_52.setFlat(True)
        self.gridLayout_10 = QGridLayout(self.groupBox_52)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_8 = QSpacerItem(50, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_39 = QLabel(self.groupBox_52)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(300, 16777215))
        self.label_39.setFont(font)
        self.label_39.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_39)

        self.ledt_p_state = QLineEdit(self.groupBox_52)
        self.ledt_p_state.setObjectName(u"ledt_p_state")
        self.ledt_p_state.setMinimumSize(QSize(0, 30))
        self.ledt_p_state.setMaximumSize(QSize(300, 16777215))
        self.ledt_p_state.setFont(font)
        self.ledt_p_state.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ledt_p_state.setFrame(False)
        self.ledt_p_state.setAlignment(Qt.AlignCenter)
        self.ledt_p_state.setReadOnly(True)
        self.ledt_p_state.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.ledt_p_state.setClearButtonEnabled(False)

        self.verticalLayout_12.addWidget(self.ledt_p_state)


        self.horizontalLayout_5.addLayout(self.verticalLayout_12)

        self.horizontalSpacer_10 = QSpacerItem(50, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_40 = QLabel(self.groupBox_52)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(300, 16777215))
        self.label_40.setFont(font)
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_40)

        self.ledt_p_number = QLineEdit(self.groupBox_52)
        self.ledt_p_number.setObjectName(u"ledt_p_number")
        self.ledt_p_number.setMinimumSize(QSize(0, 30))
        self.ledt_p_number.setMaximumSize(QSize(300, 16777215))
        self.ledt_p_number.setFont(font)
        self.ledt_p_number.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ledt_p_number.setFrame(False)
        self.ledt_p_number.setAlignment(Qt.AlignCenter)
        self.ledt_p_number.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.ledt_p_number)


        self.horizontalLayout_5.addLayout(self.verticalLayout_13)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_9 = QSpacerItem(50, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_45 = QLabel(self.groupBox_52)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(300, 16777215))
        self.label_45.setFont(font)
        self.label_45.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_45)

        self.ledt_p_position = QLineEdit(self.groupBox_52)
        self.ledt_p_position.setObjectName(u"ledt_p_position")
        self.ledt_p_position.setEnabled(True)
        self.ledt_p_position.setMinimumSize(QSize(0, 30))
        self.ledt_p_position.setMaximumSize(QSize(300, 16777215))
        self.ledt_p_position.setFont(font)
        self.ledt_p_position.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ledt_p_position.setFrame(False)
        self.ledt_p_position.setAlignment(Qt.AlignCenter)
        self.ledt_p_position.setReadOnly(True)

        self.verticalLayout_34.addWidget(self.ledt_p_position)


        self.horizontalLayout_6.addLayout(self.verticalLayout_34)

        self.horizontalSpacer_22 = QSpacerItem(50, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_22)


        self.gridLayout_10.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_52, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame_9)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_19 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_19)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(50, 35))
        self.frame_7.setMaximumSize(QSize(50, 35))
        self.frame_7.setSizeIncrement(QSize(0, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.lbl_pausa = QLabel(self.frame_7)
        self.lbl_pausa.setObjectName(u"lbl_pausa")
        self.lbl_pausa.setGeometry(QRect(10, 10, 30, 20))
        self.lbl_pausa.setMinimumSize(QSize(30, 20))
        self.lbl_pausa.setMaximumSize(QSize(30, 20))
        self.lbl_pausa.setFrameShape(QFrame.NoFrame)
        self.lbl_pausa.setPixmap(QPixmap(u"1023047.png"))
        self.lbl_pausa.setScaledContents(True)
        self.lbl_play = QLabel(self.frame_7)
        self.lbl_play.setObjectName(u"lbl_play")
        self.lbl_play.setGeometry(QRect(10, 10, 30, 20))
        self.lbl_play.setMinimumSize(QSize(30, 20))
        self.lbl_play.setMaximumSize(QSize(30, 20))
        self.lbl_play.setPixmap(QPixmap(u"6051190.png"))
        self.lbl_play.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.frame_7)

        self.horizontalSpacer_20 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_20)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_9)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(600, 0))
        self.frame_3.setMaximumSize(QSize(800, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgb(190, 190, 190);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(100, 50))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.groupBox_2.setFlat(True)
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_8 = QFrame(self.groupBox_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 81))
        self.frame_8.setMaximumSize(QSize(700, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_11 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(81, 61))
        self.label_6.setMaximumSize(QSize(81, 61))
        self.label_6.setPixmap(QPixmap(u"6012428.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.horizontalSpacer_18 = QSpacerItem(220, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_18)


        self.gridLayout_8.addWidget(self.frame_8, 0, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.groupBox_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(0, 81))
        self.groupBox_9.setMaximumSize(QSize(700, 16777215))
        self.groupBox_9.setFlat(True)
        self.gridLayout_13 = QGridLayout(self.groupBox_9)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_12 = QSpacerItem(188, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_12)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_5 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.frame_11 = QFrame(self.groupBox_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(71, 71))
        self.frame_11.setMaximumSize(QSize(71, 71))
        self.frame_11.setSizeIncrement(QSize(0, 0))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.lbl_c_sleep = QLabel(self.frame_11)
        self.lbl_c_sleep.setObjectName(u"lbl_c_sleep")
        self.lbl_c_sleep.setEnabled(True)
        self.lbl_c_sleep.setGeometry(QRect(7, 9, 51, 51))
        self.lbl_c_sleep.setMinimumSize(QSize(51, 51))
        self.lbl_c_sleep.setMaximumSize(QSize(51, 51))
        self.lbl_c_sleep.setAutoFillBackground(False)
        self.lbl_c_sleep.setFrameShape(QFrame.NoFrame)
        self.lbl_c_sleep.setPixmap(QPixmap(u"4419495.png"))
        self.lbl_c_sleep.setScaledContents(True)
        self.lbl_c_sleep.setAlignment(Qt.AlignCenter)
        self.lbl_c_work = QLabel(self.frame_11)
        self.lbl_c_work.setObjectName(u"lbl_c_work")
        self.lbl_c_work.setEnabled(True)
        self.lbl_c_work.setGeometry(QRect(7, 9, 51, 51))
        self.lbl_c_work.setMinimumSize(QSize(51, 51))
        self.lbl_c_work.setMaximumSize(QSize(51, 51))
        self.lbl_c_work.setPixmap(QPixmap(u"10277807.png"))
        self.lbl_c_work.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.frame_11)

        self.verticalSpacer_6 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)


        self.horizontalLayout_16.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_13 = QSpacerItem(188, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_13)


        self.gridLayout_13.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_9, 1, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.groupBox_2)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(500, 81))
        self.groupBox_10.setMaximumSize(QSize(700, 16777215))
        self.groupBox_10.setAlignment(Qt.AlignCenter)
        self.groupBox_10.setFlat(True)
        self.gridLayout_14 = QGridLayout(self.groupBox_10)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_14 = QSpacerItem(50, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_14)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_41 = QLabel(self.groupBox_10)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(300, 16777215))
        self.label_41.setFont(font)
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_41)

        self.ledt_c_state = QLineEdit(self.groupBox_10)
        self.ledt_c_state.setObjectName(u"ledt_c_state")
        self.ledt_c_state.setMinimumSize(QSize(0, 30))
        self.ledt_c_state.setMaximumSize(QSize(300, 16777215))
        self.ledt_c_state.setFont(font)
        self.ledt_c_state.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ledt_c_state.setFrame(False)
        self.ledt_c_state.setAlignment(Qt.AlignCenter)
        self.ledt_c_state.setReadOnly(True)

        self.verticalLayout_14.addWidget(self.ledt_c_state)


        self.horizontalLayout_11.addLayout(self.verticalLayout_14)

        self.horizontalSpacer_15 = QSpacerItem(50, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_42 = QLabel(self.groupBox_10)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(300, 16777215))
        self.label_42.setFont(font)
        self.label_42.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_42)

        self.ledt_c_number = QLineEdit(self.groupBox_10)
        self.ledt_c_number.setObjectName(u"ledt_c_number")
        self.ledt_c_number.setMinimumSize(QSize(0, 30))
        self.ledt_c_number.setMaximumSize(QSize(300, 16777215))
        self.ledt_c_number.setFont(font)
        self.ledt_c_number.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ledt_c_number.setFrame(False)
        self.ledt_c_number.setAlignment(Qt.AlignCenter)
        self.ledt_c_number.setReadOnly(True)

        self.verticalLayout_15.addWidget(self.ledt_c_number)


        self.horizontalLayout_11.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_16 = QSpacerItem(50, 17, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_16)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_46 = QLabel(self.groupBox_10)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(300, 16777215))
        self.label_46.setFont(font)
        self.label_46.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_46)

        self.ledt_c_position = QLineEdit(self.groupBox_10)
        self.ledt_c_position.setObjectName(u"ledt_c_position")
        self.ledt_c_position.setMinimumSize(QSize(0, 30))
        self.ledt_c_position.setMaximumSize(QSize(300, 16777215))
        self.ledt_c_position.setFont(font)
        self.ledt_c_position.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ledt_c_position.setFrame(False)
        self.ledt_c_position.setAlignment(Qt.AlignCenter)
        self.ledt_c_position.setReadOnly(True)

        self.verticalLayout_35.addWidget(self.ledt_c_position)


        self.horizontalLayout_11.addLayout(self.verticalLayout_35)

        self.horizontalSpacer_23 = QSpacerItem(50, 17, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_23)


        self.gridLayout_14.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_10, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_3)


        self.gridLayout_11.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.line_64 = QFrame(self.frame_9)
        self.line_64.setObjectName(u"line_64")
        self.line_64.setFrameShape(QFrame.HLine)
        self.line_64.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_64, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_9, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1680, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Buffer", None))
        self.groupBox_4.setTitle("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Capacidad", None))
        self.Enum_contenedor.setTitle("")
        self.taco_0_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.taco_0_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.taco_0_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.taco_0_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.taco_0_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.taco_0_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.taco_0_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.taco_0_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.taco_0_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.taco_0_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.taco_0_11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.taco_0_12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.taco_0_13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.taco_0_14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.taco_0_15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.taco_0_16.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.taco_0_17.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.taco_0_18.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.taco_0_19.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.taco_0_20.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.Contenedor.setTitle("")
        self.tacos_0.setText("")
        self.tacos_1.setText("")
        self.tacos_2.setText("")
        self.tacos_3.setText("")
        self.tacos_4.setText("")
        self.tacos_5.setText("")
        self.tacos_6.setText("")
        self.tacos_7.setText("")
        self.tacos_8.setText("")
        self.tacos_9.setText("")
        self.tacos_10.setText("")
        self.tacos_11.setText("")
        self.tacos_12.setText("")
        self.tacos_13.setText("")
        self.tacos_14.setText("")
        self.tacos_15.setText("")
        self.tacos_16.setText("")
        self.tacos_17.setText("")
        self.tacos_18.setText("")
        self.tacos_19.setText("")
        self.btn_start.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Turno", None))
        self.ledt_turn.setText("")
        self.ledt_turn.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Productor", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.ledt_number_products.setText("")
        self.ledt_number_products.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Productor", None))
        self.label_5.setText("")
#if QT_CONFIG(statustip)
        self.lbl_p_sleep.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lbl_p_sleep.setText("")
        self.lbl_p_work.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.ledt_p_state.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Produciendo...", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de productos", None))
        self.ledt_p_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Posici\u00f3n", None))
        self.ledt_p_position.setText("")
        self.ledt_p_position.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lbl_pausa.setText("")
        self.lbl_play.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Consumidor", None))
        self.label_6.setText("")
#if QT_CONFIG(statustip)
        self.lbl_c_sleep.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lbl_c_sleep.setText("")
        self.lbl_c_work.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.ledt_c_state.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Durmiendo...", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de productos:", None))
        self.ledt_c_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Posici\u00f3n", None))
        self.ledt_c_position.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1", None))
    # retranslateUi

