# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dvalovcin\Documents\GitHub\MotorDriver-cloaked\movementWindow.ui'
#
# Created: Fri Apr 17 17:38:22 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(796, 331)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.bp01 = QtGui.QPushButton(self.centralwidget)
        self.bp01.setGeometry(QtCore.QRect(500, 110, 75, 23))
        self.bp01.setObjectName(_fromUtf8("bp01"))
        self.bp05 = QtGui.QPushButton(self.centralwidget)
        self.bp05.setGeometry(QtCore.QRect(490, 170, 75, 23))
        self.bp05.setObjectName(_fromUtf8("bp05"))
        self.bp10 = QtGui.QPushButton(self.centralwidget)
        self.bp10.setGeometry(QtCore.QRect(630, 210, 75, 23))
        self.bp10.setObjectName(_fromUtf8("bp10"))
        self.bm01 = QtGui.QPushButton(self.centralwidget)
        self.bm01.setGeometry(QtCore.QRect(210, 100, 75, 23))
        self.bm01.setObjectName(_fromUtf8("bm01"))
        self.bm05 = QtGui.QPushButton(self.centralwidget)
        self.bm05.setGeometry(QtCore.QRect(340, 170, 75, 23))
        self.bm05.setObjectName(_fromUtf8("bm05"))
        self.bm10 = QtGui.QPushButton(self.centralwidget)
        self.bm10.setGeometry(QtCore.QRect(110, 110, 75, 23))
        self.bm10.setObjectName(_fromUtf8("bm10"))
        self.bQuit = QtGui.QPushButton(self.centralwidget)
        self.bQuit.setGeometry(QtCore.QRect(140, 230, 75, 23))
        self.bQuit.setObjectName(_fromUtf8("bQuit"))
        self.bGo = QtGui.QPushButton(self.centralwidget)
        self.bGo.setGeometry(QtCore.QRect(300, 240, 75, 23))
        self.bGo.setObjectName(_fromUtf8("bGo"))
        self.sbAngle = SpinBox(self.centralwidget)
        self.sbAngle.setGeometry(QtCore.QRect(360, 100, 91, 22))
        self.sbAngle.setObjectName(_fromUtf8("sbAngle"))
        self.bStop = QtGui.QPushButton(self.centralwidget)
        self.bStop.setGeometry(QtCore.QRect(190, 60, 75, 23))
        self.bStop.setObjectName(_fromUtf8("bStop"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMore = QtGui.QMenu(self.menubar)
        self.menuMore.setObjectName(_fromUtf8("menuMore"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.mMoreSettings = QtGui.QAction(MainWindow)
        self.mMoreSettings.setObjectName(_fromUtf8("mMoreSettings"))
        self.mMoreZero = QtGui.QAction(MainWindow)
        self.mMoreZero.setObjectName(_fromUtf8("mMoreZero"))
        self.menuMore.addAction(self.mMoreSettings)
        self.menuMore.addAction(self.mMoreZero)
        self.menubar.addAction(self.menuMore.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.bp01.setText(_translate("MainWindow", "+1°", None))
        self.bp05.setText(_translate("MainWindow", "+5°", None))
        self.bp10.setText(_translate("MainWindow", "+10°", None))
        self.bm01.setText(_translate("MainWindow", "-1°", None))
        self.bm05.setText(_translate("MainWindow", "-5°", None))
        self.bm10.setText(_translate("MainWindow", "-10°", None))
        self.bQuit.setText(_translate("MainWindow", "Quit", None))
        self.bGo.setText(_translate("MainWindow", "Go", None))
        self.bStop.setText(_translate("MainWindow", "Stop", None))
        self.menuMore.setTitle(_translate("MainWindow", "More", None))
        self.mMoreSettings.setText(_translate("MainWindow", "Control Panel", None))
        self.mMoreZero.setText(_translate("MainWindow", "Set Zero", None))

from pyqtgraph import SpinBox
