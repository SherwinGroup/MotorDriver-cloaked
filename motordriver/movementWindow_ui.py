# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dvalovcin\Documents\GitHub\MotorDriver-cloaked\motordriver\movementWindow.ui'
#
# Created: Mon Jul 20 15:25:49 2015
#      by: PyQt4 UI code generator 4.10.4
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
        MainWindow.resize(593, 251)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.bm10 = QtGui.QPushButton(self.centralwidget)
        self.bm10.setObjectName(_fromUtf8("bm10"))
        self.horizontalLayout_2.addWidget(self.bm10)
        self.bm05 = QtGui.QPushButton(self.centralwidget)
        self.bm05.setObjectName(_fromUtf8("bm05"))
        self.horizontalLayout_2.addWidget(self.bm05)
        self.bm01 = QtGui.QPushButton(self.centralwidget)
        self.bm01.setObjectName(_fromUtf8("bm01"))
        self.horizontalLayout_2.addWidget(self.bm01)
        self.sbAngle = SpinBox(self.centralwidget)
        self.sbAngle.setObjectName(_fromUtf8("sbAngle"))
        self.horizontalLayout_2.addWidget(self.sbAngle)
        self.bp01 = QtGui.QPushButton(self.centralwidget)
        self.bp01.setObjectName(_fromUtf8("bp01"))
        self.horizontalLayout_2.addWidget(self.bp01)
        self.bp05 = QtGui.QPushButton(self.centralwidget)
        self.bp05.setObjectName(_fromUtf8("bp05"))
        self.horizontalLayout_2.addWidget(self.bp05)
        self.bp10 = QtGui.QPushButton(self.centralwidget)
        self.bp10.setObjectName(_fromUtf8("bp10"))
        self.horizontalLayout_2.addWidget(self.bp10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bStop = QtGui.QPushButton(self.centralwidget)
        self.bStop.setObjectName(_fromUtf8("bStop"))
        self.horizontalLayout.addWidget(self.bStop)
        self.bGo = QtGui.QPushButton(self.centralwidget)
        self.bGo.setObjectName(_fromUtf8("bGo"))
        self.horizontalLayout.addWidget(self.bGo)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.bQuit = QtGui.QPushButton(self.centralwidget)
        self.bQuit.setObjectName(_fromUtf8("bQuit"))
        self.horizontalLayout.addWidget(self.bQuit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelCosCalc = QtGui.QLabel(self.centralwidget)
        self.labelCosCalc.setObjectName(_fromUtf8("labelCosCalc"))
        self.horizontalLayout_3.addWidget(self.labelCosCalc)
        self.tCosCalc = QtGui.QLineEdit(self.centralwidget)
        self.tCosCalc.setReadOnly(True)
        self.tCosCalc.setObjectName(_fromUtf8("tCosCalc"))
        self.horizontalLayout_3.addWidget(self.tCosCalc)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 21))
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
        self.bm10.setText(_translate("MainWindow", "-10°", None))
        self.bm05.setText(_translate("MainWindow", "-5°", None))
        self.bm01.setText(_translate("MainWindow", "-1°", None))
        self.bp01.setText(_translate("MainWindow", "+1°", None))
        self.bp05.setText(_translate("MainWindow", "+5°", None))
        self.bp10.setText(_translate("MainWindow", "+10°", None))
        self.bStop.setText(_translate("MainWindow", "Stop", None))
        self.bGo.setText(_translate("MainWindow", "Go", None))
        self.bQuit.setText(_translate("MainWindow", "Quit", None))
        self.labelCosCalc.setText(_translate("MainWindow", "TextLabel", None))
        self.tCosCalc.setText(_translate("MainWindow", ".0321", None))
        self.menuMore.setTitle(_translate("MainWindow", "More", None))
        self.mMoreSettings.setText(_translate("MainWindow", "Control Panel", None))
        self.mMoreZero.setText(_translate("MainWindow", "Set Zero", None))

from pyqtgraph import SpinBox
