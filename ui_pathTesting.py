# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pathTesting.ui'
#
# Created: Sun Jan  1 17:13:58 2012
#      by: pyside-uic 0.2.13 running on PySide 1.0.7
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(370, 121)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.versionSelectionBox = QtGui.QComboBox(self.centralwidget)
        self.versionSelectionBox.setObjectName("versionSelectionBox")
        self.gridLayout.addWidget(self.versionSelectionBox, 2, 1, 1, 1)
        self.launchButton = QtGui.QPushButton(self.centralwidget)
        self.launchButton.setObjectName("launchButton")
        self.gridLayout.addWidget(self.launchButton, 2, 2, 1, 1)
        self.addNewVersionButton = QtGui.QPushButton(self.centralwidget)
        self.addNewVersionButton.setObjectName("addNewVersionButton")
        self.gridLayout.addWidget(self.addNewVersionButton, 3, 1, 1, 1)
        self.settingsButton = QtGui.QPushButton(self.centralwidget)
        self.settingsButton.setObjectName("settingsButton")
        self.gridLayout.addWidget(self.settingsButton, 3, 2, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Minecraft Version Selector", None, QtGui.QApplication.UnicodeUTF8))
        self.launchButton.setText(QtGui.QApplication.translate("mainWindow", "Launch", None, QtGui.QApplication.UnicodeUTF8))
        self.addNewVersionButton.setText(QtGui.QApplication.translate("mainWindow", "Add new", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsButton.setText(QtGui.QApplication.translate("mainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))

