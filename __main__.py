from PyQt4 import QtCore, QtGui
from movementWindow_ui import Ui_MainWindow
from InstsAndQt.MotorDriver import *
from InstsAndQt.customQt import *
from Control import SettingsWindow
import pyqtgraph



class MotorWindow(QtGui.QMainWindow):
    # emit a list of values to update the voltages/currents of the coils
    thMoveMotor = None

    mutex = QtCore.QMutex()

    def __init__(self, device = None, parent = None):
        super(MotorWindow, self).__init__(parent)
        self.device = TIMS0201()
        self.device.open_()
        self.initUI()
        self.currentAngle = 0
        self.currentLimit = self.device.getCurrentLimit()
        self.device.setCurrentLimit(0)
        self.settingsWindow = None


    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.buttons = [
            self.ui.bm01,
            self.ui.bm05,
            self.ui.bm10,
            self.ui.bp01,
            self.ui.bp05,
            self.ui.bp10,
            self.ui.bGo
        ]
        for button in self.buttons:
            button.clicked.connect(self.moveMotorDeg)

        self.ui.sbAngle.setOpts(bounds = (-360, 360), decimals = 1, step = 0.1)
        self.ui.bStop.clicked.connect(self.stopMove)

        self.ui.mMoreSettings.triggered.connect(self.launchSettings)





        self.show()

    def moveMotorDeg(self):
        sent = self.sender()
        moveBy = 0
        if sent in self.buttons[:-1]:
            moveBy = int(sent.text()[:-1])
        else:
            moveBy = self.ui.sbAngle.interpret() - self.currentAngle
        print moveBy


        for button in self.buttons:
            button.setEnabled(False)

        if self.settingsWindow is not None:
            self.currentLimit = self.settingsWindow.ui.sbCurrent.interpret()
        self.device.setCurrentLimit(self.currentLimit)
        self.device.moveRelative(moveBy * 400)
        self.thMoveMotor = TempThread(target = self.waitForMotor)
        # self.thMoveMotor.terminated.connect(self.finishedMove)
        self.thMoveMotor.start()


    def stopMove(self):
        try:
            # self.thMoveMotor.terminate()
            self.device.stopMotor()
        except Exception as e:
            print e

    def launchSettings(self):
        self.device.setCurrentLimit(self.currentLimit)
        self.settingsWindow = SettingsWindow(device = self.device, parent = self)




    def waitForMotor(self):
        self.mutex.lock()
        while self.device.isBusy():
            self.mutex.unlock()
            time.sleep(0.4)
            self.mutex.lock()
        self.finishedMove()
        self.mutex.unlock()

    def finishedMove(self):
        for button in self.buttons:
            button.setEnabled(True)
        # Stop it from whining when not moving
        self.device.setCurrentLimit(0)







    def closeEvent(self, QCloseEvent):
        if self.parent() == None:
            self.device.close_()
        QCloseEvent.accept()











if __name__ == "__main__":
    import sys
    e = QtGui.QApplication(sys.argv)
    win = MotorWindow(device = TIMS0201(), parent = None)
    sys.exit(e.exec_())