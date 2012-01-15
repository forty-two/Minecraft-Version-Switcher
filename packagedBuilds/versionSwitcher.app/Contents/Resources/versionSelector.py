from PySide.QtCore import SIGNAL, QThread
from PySide.QtGui import QMainWindow, QDialog, QApplication, QFileDialog, QDialogButtonBox
import sys
import json
import os
import threading
import shutil
import time
import platform

from ui_versionSelector import Ui_mainWindow
from ui_pathInputDialogue import Ui_addNewVersionDialog
from ui_settingsWindow import Ui_settingsWindow
from ui_instructions import Ui_instructionsWindow
from ui_about import Ui_aboutWindow


    
class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.addNewVersionButton.clicked.connect(self.newButtonPressed)
        self.removeButton.clicked.connect(self.removeVersionPressed)
        self.loadButton.clicked.connect(self.loadButtonPressed)
        self.actionExit.triggered.connect(self.exit)
        self.actionSettings.triggered.connect(self.settingsPressed)
        self.actionInstructions.triggered.connect(self.showInstructions)
        self.actionAbout.triggered.connect(self.showAboutInfo)
        self.path = ''
        self.data = {}
        self.defaultStatus()
        
        self.loadData()
        if 'versions' not in self.data.keys():
            self.data['versions'] = {}
            
        if 'minecraftPath' not in self.data.keys():
            self.minecraftPath = self.osMinecraftPath()
        else:
            self.minecraftPath = self.data['minecraftPath']
            
        self.refreshVersionBox()        
        
    def osMinecraftPath(self):
        osType = sys.platform.lower()
        if 'darwin' in osType:
            return os.path.expanduser(os.path.join("~", "Library", "Application Support", "minecraft",
                                                    "bin", "minecraft.jar"))
        elif 'linux' in osType:
            return os.path.expanduser(os.path.join("~", ".minecraft", "bin", "minecraft.jar"))
        elif 'win32' in osType or "win64" in osType:
            return os.path.join(os.environ['APPDATA'], ".minecraft", "bin", "minecraft.jar")
        else:
            return "Your system type is unknown, please add path manually"
        
        
    def newButtonPressed(self):
        d = DialogueBox(self)
        d.show()
        if d.exec_():
             self.makeNewVersion(d.versionLabel.displayText(),
                                 d.gameFolderLine.displayText())
             
    def settingsPressed(self):
        settings = settingsWindow(self)
        settings.show()
        if settings.exec_():
            self.minecraftPath = settings.minecraftPathLine.displayText()
            self.data['minecraftPath'] = self.minecraftPath
            self.saveData()
        
    def loadButtonPressed(self):
        version = self.versionSelectionBox.currentText()
        if version in self.data['versions'].keys():
            thread = copyThread(self.data['versions'][version], self.minecraftPath, self)
            self.connect(thread, SIGNAL("updateStatusBar(QString)"), self.statusChange)
            self.connect(thread, SIGNAL("defaultStatusBar()"), self.defaultStatus)
            thread.start()

    def makeNewVersion(self, label, minecraftPath):
        d = minecraftPath
        self.data['versions'][label] = d
        self.refreshVersionBox()
        self.saveData()
        
    def refreshVersionBox(self):
        self.versionSelectionBox.clear()
        for key in self.data['versions'].keys():
            self.versionSelectionBox.addItem(key)
            
    def saveData(self):
        outputFile = open("versionSelectorData.json", 'w')
        outputFile.write(json.dumps(self.data, indent = 4))
        
    def loadData(self):
        if os.path.isfile("versionSelectorData.json"):
            self.data = json.loads(open("versionSelectorData.json").read())
            
    def removeVersionPressed(self):
        version = self.versionSelectionBox.currentText()
        if version in self.data['versions'].keys():
            self.data['versions'].pop(version)
        self.saveData()
        self.refreshVersionBox()
        
    def showInstructions(self):
        instructions = instructionsWindow()
        instructions.show()
        instructions.exec_()
        
    def showAboutInfo(self):
        about = aboutWindow()
        about.show()
        about.exec_()
        
    def statusChange(self, newStatus):
        self.statusbar.showMessage(newStatus)
    
    def defaultStatus(self):
        self.statusbar.showMessage("-Remember to backup your .jar files before using this program-")
        
        
    def exit(self):
        sys.exit()
     

class DialogueBox(QDialog, Ui_addNewVersionDialog):
    def __init__(self, parent):
        super(DialogueBox, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.gameFolderButton.clicked.connect(self.choosePath)
        self.clearTextButton.clicked.connect(self.clearInputBoxes)
        
    def choosePath(self):
        self.binPath = QFileDialog.getOpenFileName()[0]
        self.gameFolderLine.setText(self.binPath)
        
    def clearInputBoxes(self):
        self.gameFolderLine.setText('')
        self.versionLabel.setText('')

        
class settingsWindow(QDialog, Ui_settingsWindow):
    def __init__(self, parent):
        super(settingsWindow, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.button(QDialogButtonBox.RestoreDefaults).clicked.connect(self.restoreDefaults)
        self.minecraftPathButton.clicked.connect(self.loadMinecraftPath)
        self.parent = parent
        self.minecraftPathLine.setText(self.parent.minecraftPath)
        self.minecraftPath = self.parent.minecraftPath
        
    def restoreDefaults(self):
        self.parent.data['minecraftPath'] = self.parent.osMinecraftPath()
        self.minecraftPathLine.setText(self.parent.osMinecraftPath())

    def loadMinecraftPath(self):
        self.parent.minecraftPath = QFileDialog.getOpenFileName()[0]
        self.parent.data['minecraftPath'] = self.parent.minecraftPath
        self.parent.saveData()
        self.minecraftPathLine.setText(self.parent.minecraftPath)

        
class instructionsWindow(QDialog, Ui_instructionsWindow):
    def __init__(self, parent = None):
        super(instructionsWindow, self).__init__(parent)
        self.setupUi(self)

      
class aboutWindow(QDialog, Ui_aboutWindow):
    def __init__(self, parent = None):
        super(aboutWindow, self).__init__(parent)
        self.setupUi(self)        


class copyThread(QThread):
    def __init__(self, source, destination, parent = None):
        QThread.__init__(self, parent)
        self.source = source
        self.destination = destination       
        
    def run(self):
        try:
            self.emit(SIGNAL("updateStatusBar(QString)"), "Copying to minecraft directory")
            shutil.copyfile(self.source, self.destination)
            self.emit(SIGNAL("updateStatusBar(QString)"), "Copied successfully")
            time.sleep(5)
        except IOError:
            self.emit(SIGNAL("updateStatusBar(QString)"), "Error occurred, please check the file paths used")
            time.sleep(5)
        self.emit(SIGNAL("defaultStatusBar()"))    
        self.quit()        


if __name__ == '__main__':        
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()