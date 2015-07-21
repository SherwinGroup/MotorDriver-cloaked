from PyQt4 import QtCore, QtGui
from movementWindow_ui import Ui_MainWindow
from InstsAndQt.MotorDriver import *
from InstsAndQt.customQt import *
from Control import SettingsWindow
import numpy as np
import pyqtgraph


class MotorWindow(QtGui.QMainWindow):
    # emit a list of values to update the voltages/currents of the coils
    thMoveMotor = None
    sigUpdateDegrees = QtCore.pyqtSignal(object)


    def __init__(self, device = None, parent = None):
        super(MotorWindow, self).__init__(parent)
        self.stepsPerDeg = 28.43
        self.device = TIMS0201()
        self.device.open_()
        self.initUI()
        self.currentAngle = self.device.getSteps()/self.stepsPerDeg
        self.currentLimit = self.device.getCurrentLimit()
        if self.currentLimit == 0:
            self.currentLimit = 25
        self.device.setCurrentLimit(0)
        self.device.setSteppingMode(toHalf=True)
        self.settingsWindow = None
        self.sigUpdateDegrees.connect(self.setDegrees)

        self.finishedMove()


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
        self.ui.mMoreZero.triggered.connect(self.zeroDegrees)

        self.ui.bQuit.clicked.connect(self.close)

        self.ui.labelCosCalc.setText(u"cos<sup>4</sup>(\u03B8)")

        self.show()

    def moveMotorDeg(self):
        sent = self.sender()
        moveBy = 0
        if sent in self.buttons[:-1]:
            moveBy = int(sent.text()[:-1])
        else:
            moveBy = self.ui.sbAngle.interpret() - self.currentAngle


        for button in self.buttons:
            button.setEnabled(False)

        if self.settingsWindow is not None:
            self.currentLimit = self.settingsWindow.ui.sbCurrent.interpret()

        self.device.setCurrentLimit(self.currentLimit)
        self.device.moveRelative(moveBy * self.stepsPerDeg)
        self.thMoveMotor = TempThread(target = self.waitForMotor)
        # self.thMoveMotor.terminated.connect(self.finishedMove)
        self.thMoveMotor.start()


    def stopMove(self):
        try:
            self.device.stopMotor()
        except Exception as e:
            print "Error stopping motor", e

    def launchSettings(self):
        self.device.setCurrentLimit(self.currentLimit)
        self.settingsWindow = SettingsWindow(device = self.device, parent = self)


    def zeroDegrees(self):
        val = self.ui.sbAngle.interpret()
        self.device.setSteps(0)
        self.finishedMove()



    def waitForMotor(self):
        flg = self.device.isBusy()
        while flg:
            curSteps = self.device.getSteps()
            self.sigUpdateDegrees.emit(curSteps/self.stepsPerDeg)
            time.sleep(0.4)
            flg = self.device.isBusy()
        self.finishedMove()

    def finishedMove(self):
        for button in self.buttons:
            button.setEnabled(True)
        # Stop it from whining when not moving
        self.device.setCurrentLimit(0)

        curSteps = self.device.getSteps()
        self.sigUpdateDegrees.emit(curSteps/self.stepsPerDeg)

    def setDegrees(self, val):
        self.ui.sbAngle.setValue(val)
        self.currentAngle = val
        cos = np.cos(np.deg2rad(val))**4
        self.ui.tCosCalc.setText("{:0.4f}".format(cos))









    def closeEvent(self, QCloseEvent):
        if self.settingsWindow is not None:
            self.settingsWindow.close()
        if self.parent() is None:
            self.device.close_()
        QCloseEvent.accept()











if __name__ == "__main__":
    import sys
    e = QtGui.QApplication(sys.argv)
    win = MotorWindow(device = TIMS0201(), parent = None)
    sys.exit(e.exec_())