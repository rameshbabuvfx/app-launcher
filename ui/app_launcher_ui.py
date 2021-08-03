# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_launcher_ui.ui'
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
        MainWindow.resize(677, 149)
        MainWindow.setStyleSheet(u"background-color: rgb(49, 48, 51);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(125, 125))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(62, 61, 64);\n"
"	border-style: solid;\n"
"	border-color: white;\n"
"	border-width: 1px;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(43, 43, 45);\n"
"}")
        icon = QIcon()
        icon.addFile(u"../icons/nuke.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(100, 100))
        self.pushButton.setCheckable(False)
        self.pushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(125, 125))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(62, 61, 64);\n"
"	border-style: solid;\n"
"	border-color: white;\n"
"	border-width: 1px;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(43, 43, 45);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../icons/blender.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(100, 100))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(125, 125))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(62, 61, 64);\n"
"	border-style: solid;\n"
"	border-color: white;\n"
"	border-width: 1px;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(43, 43, 45);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../icons/houdini.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(150, 150))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(125, 125))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(62, 61, 64);\n"
"	border-style: solid;\n"
"	border-color: white;\n"
"	border-width: 1px;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(43, 43, 45);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../icons/aftereffects.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(100, 100))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(125, 125))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(62, 61, 64);\n"
"	border-style: solid;\n"
"	border-color: white;\n"
"	border-width: 1px;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(43, 43, 45);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../icons/maya.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(100, 100))

        self.horizontalLayout.addWidget(self.pushButton_5)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AppLauncher", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
    # retranslateUi

