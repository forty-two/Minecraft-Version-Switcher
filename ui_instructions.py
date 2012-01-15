# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instructions.ui'
#
# Created: Sat Jan 14 16:14:12 2012
#      by: pyside-uic 0.2.13 running on PySide 1.0.7
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_instructionsWindow(object):
    def setupUi(self, instructionsWindow):
        instructionsWindow.setObjectName("instructionsWindow")
        instructionsWindow.resize(574, 458)
        self.gridLayout = QtGui.QGridLayout(instructionsWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.instructionsTitle = QtGui.QLabel(instructionsWindow)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.instructionsTitle.setFont(font)
        self.instructionsTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.instructionsTitle.setObjectName("instructionsTitle")
        self.gridLayout.addWidget(self.instructionsTitle, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(instructionsWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.instructionsText = QtGui.QTextBrowser(instructionsWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setItalic(False)
        self.instructionsText.setFont(font)
        self.instructionsText.setObjectName("instructionsText")
        self.gridLayout.addWidget(self.instructionsText, 1, 0, 1, 1)

        self.retranslateUi(instructionsWindow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), instructionsWindow.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), instructionsWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(instructionsWindow)

    def retranslateUi(self, instructionsWindow):
        instructionsWindow.setWindowTitle(QtGui.QApplication.translate("instructionsWindow", "Instructions", None, QtGui.QApplication.UnicodeUTF8))
        self.instructionsTitle.setText(QtGui.QApplication.translate("instructionsWindow", "How to use the Version Switcher", None, QtGui.QApplication.UnicodeUTF8))
        self.instructionsText.setHtml(QtGui.QApplication.translate("instructionsWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lucida Grande\';\">This program is intended to store a list of Minecraft game .jars and switch them into the main Minecraft folder on command. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lucida Grande\';\">I recommend that you store your various .jars in a single location to aid with remembering where they are, but this is not necessary.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Lucida Grande\';\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lucida Grande\';\">To begin, click the \'Add New\' button on the main screen. This brings up a dialog window that enables you to enter the path to your desired .jar and to give it a descriptive label. This label will be used to identify the file. Click \'OK\' to add this version to the combo box in the main window.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Lucida Grande\';\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lucida Grande\';\">You can now either click \'Load\' to copy the selected file version into your Minecraft folder, or click \'Remove\' to delete the selected entry from the list. Note that the remove function does not touch the actual file.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Lucida Grande\';\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lucida Grande\';\">The settings (or Preferences on Mac) menu option allows you to select the path to your .minecraft folder. This should be automatically set to the default for your OS, but I can\'t guarantee that to always work.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Lucida Grande\';\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lucida Grande\';\">As always, keep copies of your .jars in case of unforseen circumstances (this program should never delete stuff, but it will overwrite the minecraft.jar file present in the Minecraft folder you have told it to use). Never set the \'default\' minecraft.jar path to anything you don\'t want overwritten by your .jars.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Lucida Grande\';\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

