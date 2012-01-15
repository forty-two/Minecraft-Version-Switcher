# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsWindow.ui'
#
# Created: Sat Jan 14 16:12:31 2012
#      by: pyside-uic 0.2.13 running on PySide 1.0.7
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_settingsWindow(object):
    def setupUi(self, settingsWindow):
        settingsWindow.setObjectName("settingsWindow")
        settingsWindow.resize(620, 80)
        settingsWindow.setMaximumSize(QtCore.QSize(16777215, 80))
        self.gridLayout = QtGui.QGridLayout(settingsWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.minecraftLabel = QtGui.QLabel(settingsWindow)
        self.minecraftLabel.setObjectName("minecraftLabel")
        self.gridLayout.addWidget(self.minecraftLabel, 0, 0, 1, 1)
        self.minecraftPathLine = QtGui.QLineEdit(settingsWindow)
        self.minecraftPathLine.setObjectName("minecraftPathLine")
        self.gridLayout.addWidget(self.minecraftPathLine, 0, 1, 1, 1)
        self.minecraftPathButton = QtGui.QPushButton(settingsWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minecraftPathButton.sizePolicy().hasHeightForWidth())
        self.minecraftPathButton.setSizePolicy(sizePolicy)
        self.minecraftPathButton.setObjectName("minecraftPathButton")
        self.gridLayout.addWidget(self.minecraftPathButton, 0, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(settingsWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.retranslateUi(settingsWindow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), settingsWindow.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), settingsWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(settingsWindow)

    def retranslateUi(self, settingsWindow):
        settingsWindow.setWindowTitle(QtGui.QApplication.translate("settingsWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.minecraftLabel.setText(QtGui.QApplication.translate("settingsWindow", "minecraft.jar path", None, QtGui.QApplication.UnicodeUTF8))
        self.minecraftPathLine.setText(QtGui.QApplication.translate("settingsWindow", "Insert minecraft.jar file path", None, QtGui.QApplication.UnicodeUTF8))
        self.minecraftPathButton.setText(QtGui.QApplication.translate("settingsWindow", "Choose", None, QtGui.QApplication.UnicodeUTF8))

