# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pathInputDialogue.ui'
#
# Created: Sat Jan 14 16:12:35 2012
#      by: pyside-uic 0.2.13 running on PySide 1.0.7
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_addNewVersionDialog(object):
    def setupUi(self, addNewVersionDialog):
        addNewVersionDialog.setObjectName("addNewVersionDialog")
        addNewVersionDialog.resize(600, 116)
        addNewVersionDialog.setMinimumSize(QtCore.QSize(600, 0))
        addNewVersionDialog.setMaximumSize(QtCore.QSize(16777215, 116))
        self.gridLayout = QtGui.QGridLayout(addNewVersionDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.gameFolderLine = QtGui.QLineEdit(addNewVersionDialog)
        self.gameFolderLine.setObjectName("gameFolderLine")
        self.gridLayout.addWidget(self.gameFolderLine, 0, 1, 1, 1)
        self.gameFolderButton = QtGui.QPushButton(addNewVersionDialog)
        self.gameFolderButton.setObjectName("gameFolderButton")
        self.gridLayout.addWidget(self.gameFolderButton, 0, 2, 1, 1)
        self.versionLabel = QtGui.QLineEdit(addNewVersionDialog)
        self.versionLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.versionLabel.setObjectName("versionLabel")
        self.gridLayout.addWidget(self.versionLabel, 1, 1, 1, 1)
        self.clearTextButton = QtGui.QPushButton(addNewVersionDialog)
        self.clearTextButton.setObjectName("clearTextButton")
        self.gridLayout.addWidget(self.clearTextButton, 1, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(addNewVersionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.label = QtGui.QLabel(addNewVersionDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(addNewVersionDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.retranslateUi(addNewVersionDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), addNewVersionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), addNewVersionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(addNewVersionDialog)

    def retranslateUi(self, addNewVersionDialog):
        addNewVersionDialog.setWindowTitle(QtGui.QApplication.translate("addNewVersionDialog", "Add new version", None, QtGui.QApplication.UnicodeUTF8))
        self.gameFolderLine.setText(QtGui.QApplication.translate("addNewVersionDialog", "Path to desired .jar file", None, QtGui.QApplication.UnicodeUTF8))
        self.gameFolderButton.setText(QtGui.QApplication.translate("addNewVersionDialog", "Choose path", None, QtGui.QApplication.UnicodeUTF8))
        self.versionLabel.setText(QtGui.QApplication.translate("addNewVersionDialog", "Label to use for this version", None, QtGui.QApplication.UnicodeUTF8))
        self.clearTextButton.setText(QtGui.QApplication.translate("addNewVersionDialog", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("addNewVersionDialog", "Path to .jar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("addNewVersionDialog", "Version name", None, QtGui.QApplication.UnicodeUTF8))

