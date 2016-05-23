from scopeCollect import Win as ScopeViewWidget
from motorMain import MotorWindow
from PyQt4 import QtGui, QtCore
from InstsAndQt.customQt import TempThread
import time
import numpy as np
import glob
import os
from scipy.interpolate import interp1d as i1d

tkTrans = np.array(
    [
    [000, 1.0],
    [100, 0.975],
    [200, 0.95],
    [300, 0.91],
    [400, 0.9],
    [500, 0.88],
    [600, 0.86],
    [700, 0.84],
    [800, 0.81],
    [900, 0.78],
    [1000, 0.75],
    [1100, 0.73],
    [1200, 0.7],
    [1300, 0.68],
    [1400, 0.66],
    [1500, 0.64],
    [1600, 0.63],
    [1700, 0.6],
    [1800, 0.59],
    [1900, 0.58],
    [2000, 0.56],
    [2100, 0.55],
    [2200, 0.54],
    [2300, 0.53],
    [2400, 0.528],
    [2500, 0.53],
    [2600, 0.529],
    [2700, 0.534],
    [2800, 0.535],
    [2900, 0.537],
    [3000, 0.534],
    [3100, 0.531],
    [3200, 0.519],
    [3300, 0.516],
    [3400, 0.514],
    [3500, 0.512],
    [3600, 0.507],
    [3700, 0.503],
    [3800, 0.498],
    [3900, 0.491],
    [4000, 0.478],
    [4100, 0.461],
    [4200, 0.444],
    [4300, 0.434],
    [4400, 0.437],
    [4500, 0.444],
    [4600, 0.447],
    [4700, 0.449],
    [4800, 0.45],
    [4900, 0.452],
    [5000, 0.452],
    [5100, 0.45],
    [5200, 0.444],
    [5300, 0.435],
    [5400, 0.424],
    [5500, 0.412],
    [5600, 0.399],
    [5700, 0.386],
    [5800, 0.371],
    [5900, 0.352],
    [6000, 0.328],
    [6100, 0.311],
    [6200, 0.293],
    [6300, 0.275],
    [6400, 0.255],
    [6500, 0.236],
    [6600, 0.215],
    [6700, 0.195],
    [6800, 0.179],
    [6900, 0.167],
    [7000, 0.16],
    [7100, 0.157],
    [7200, 0.155],
    [7300, 0.153],
    [7400, 0.149],
    [7500, 0.146],
    [7600, 0.146],
    [7700, 0.152],
    [7800, 0.155],
    [7900, 0.154],
    [8000, 0.152],
    [8100, 0.151],
    [8200, 0.147],
    [8300, 0.139],
    [8400, 0.13],
    [8500, 0.121],
    [8600, 0.108],
    [8700, 0.096],
    [8800, 0.091],
    [8900, 0.089],
    [9000, 0.095],
    [9100, 0.111],
    [9200, 0.127],
    [9300, 0.144],
    [9400, 0.157],
    [9500, 0.159],
    [9600, 0.168],
    [9700, 0.168],
    [9800, 0.175],
    [9900, 0.17],
    [10000, 0.174]]
)
tkTrans = i1d(tkTrans[:,0], tkTrans[:,1])

tkCalFactor = 0.00502

class UI(object): pass

class TKCalibrator(QtGui.QMainWindow):


    thWaitForScope = None
    thDoTKSweep = TempThread()
    sigDoGui = QtCore.pyqtSignal(object, object)
    def __init__(self):
        super(TKCalibrator, self).__init__()
        self.ui = UI()
        layout = QtGui.QVBoxLayout()
        self.motorWid = MotorWindow()
        self.scopeWid = ScopeViewWidget()
        layout.addWidget(self.motorWid)
        layout.addWidget(self.scopeWid)

        buttons = QtGui.QHBoxLayout()
        self.ui.bSaveDir = QtGui.QPushButton("Choose Save Dir")
        self.ui.bSaveDir.clicked.connect(self.pickSaveDir)
        self.ui.bStartSweep = QtGui.QPushButton("Start TK Cal")
        self.ui.bStartSweep.setCheckable(True)
        self.ui.bStartSweep.clicked.connect(self.startSweep)
        buttons.addSpacing(2)
        buttons.addWidget(self.ui.bSaveDir)
        buttons.addWidget(self.ui.bStartSweep)

        wid = QtGui.QWidget()
        layout.addLayout(buttons)
        wid.setLayout(layout)
        self.setCentralWidget(wid)

        self.scopeWid.ui.cbSettingsCH3.setChecked(True)
        self.scopeWid.ui.tSettingsCH1.setText("TK")
        self.scopeWid.ui.tSettingsCH3.setText("Pyro")

        self.thDoTKSweep.target = self.doTKSweep
        self.sigDoGui.connect(self.makeGuiThings)


        self.settings = {
            "saveDir": '',
            "numAve": 4,
            "thzSweepPoints": [],
            "saveData": [],
            "thzFreq": 435
        }






        self.show()


    def pickSaveDir(self):
        path = QtGui.QFileDialog.getSaveFileName(self,
                                                 "Save File",
                                                 self.settings["saveDir"],
                                                 "Text files (*.txt)")
        if not path:
            return
        self.settings["saveDir"] = str(path)

    def startSweep(self, val):
        if not val:
            return
        st, ok = QtGui.QInputDialog.getText(self,
                    "Desired Angles",
                    "Enter angles in deg separated by commas",
                    text=",".join(map(str, self.settings["thzSweepPoints"])))
        if not ok:
            return
        self.settings["thzSweepPoints"] = [float(i) for i in st.split(',')]
        self.settings["saveData"] = []
        self.thDoTKSweep.start()

    def doTKSweep(self):
        for angle in self.settings["thzSweepPoints"]:
            if not self.ui.bStartSweep.isChecked(): break
            print "at angle", angle
            self.sigDoGui.emit(
                self.motorWid.ui.sbAngle.setValue, angle
            )
            self.motorWid.ui.bGo.clicked.emit(False)
            time.sleep(0.1)
            self.motorWid.thMoveMotor.wait()
            angleData = []
            for i in range(self.settings["numAve"]):
                print "\t num", i
                waiter = QtCore.QEventLoop()
                self.scopeWid.ch1View.sigUpdateData.connect(waiter.exit)
                waiter.exec_()
                waveformData = self.scopeWid.ch1View.data.copy()
                try:
                    angleData = np.column_stack((angleData, waveformData[:,1]))
                except:
                    angleData = waveformData[:, 1]

            tkVal = self.processTKWaveform(angleData.mean(axis=1))
            print "\n\tmeasured {}\n\n".format(tkVal)


            self.settings["saveData"].append([angle, tkVal])

        self.sigDoGui.emit(
            self.ui.bStartSweep.setChecked, False
        )
        self.saveData()

    def processTKWaveform(self, data):
        minSt, minEn = np.argmin(data[:]) + np.array([-200, 350])

        maxSt, maxEn = np.argmax(data[minEn:]) + minEn + np.array([-750, 750])

        p1 = np.polyfit(data[minSt:minEn], data[minSt:minEn], 3)
        p2 = np.polyfit(data[maxSt:maxEn], data[maxSt:maxEn], 2)

        x1 = data[minSt:minEn]
        x2 = data[maxSt:maxEn]
        y1 = np.polyval(p1, x1)
        y2 = np.polyval(p2, x2)
        return np.max(y1) - np.min(y2)

    def saveData(self):
        data = np.array(self.settings["saveData"])
        # convert mV to mJ
        T = tkTrans(self.settings["thzFreq"])
        energy = data[:,1] / (0.49 * T) * tkCalFactor

        f = self.settings["saveDir"].split('.txt')[0]
        num = len([ii for ii in glob.glob(f) if os.path.isfile(ii)])
        print "found {} files".format(num)
        f += "{}.txt".format(num)

        data = np.column_stack((data, energy))




        oh = "#Freq: {}\nAngle,TK,TK\ndeg,mV,mJ\nAngle,TK,TK".format(self.settings["thzFreq"])
        np.savetxt(f, data, fmt="%.6e", delimiter=',', header=oh, comments='')

    def makeGuiThings(self, func, args):
        if args is None:
            func()
        else:
            func(args)






if __name__ == '__main__':
    ex = QtGui.QApplication([])
    win = TKCalibrator()
    import sys
    sys.exit(ex.exec_())