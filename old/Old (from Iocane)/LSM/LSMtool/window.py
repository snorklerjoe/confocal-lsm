# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(529, 372)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 10, 251, 211))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.res = QtGui.QLineEdit(self.frame)
        self.res.setGeometry(QtCore.QRect(130, 0, 113, 30))
        self.res.setObjectName(_fromUtf8("res"))
        self.time = QtGui.QLineEdit(self.frame)
        self.time.setGeometry(QtCore.QRect(130, 30, 113, 30))
        self.time.setObjectName(_fromUtf8("time"))
        self.sense = QtGui.QLineEdit(self.frame)
        self.sense.setGeometry(QtCore.QRect(130, 60, 113, 30))
        self.sense.setObjectName(_fromUtf8("sense"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 111, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 121, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 121, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.scan = QtGui.QPushButton(self.frame)
        self.scan.setGeometry(QtCore.QRect(80, 90, 85, 30))
        self.scan.setCheckable(False)
        self.scan.setChecked(False)
        self.scan.setAutoDefault(False)
        self.scan.setDefault(True)
        self.scan.setFlat(False)
        self.scan.setObjectName(_fromUtf8("scan"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 230, 221, 111))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.scanbar = QtGui.QProgressBar(self.frame_3)
        self.scanbar.setGeometry(QtCore.QRect(90, 80, 118, 23))
        self.scanbar.setProperty("value", 0)
        self.scanbar.setObjectName(_fromUtf8("scanbar"))
        self.sendbar = QtGui.QProgressBar(self.frame_3)
        self.sendbar.setGeometry(QtCore.QRect(90, 60, 118, 23))
        self.sendbar.setProperty("value", 0)
        self.sendbar.setObjectName(_fromUtf8("sendbar"))
        self.label_5 = QtGui.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(0, 80, 101, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label = QtGui.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(0, 60, 91, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_6 = QtGui.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(60, 10, 57, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(260, 10, 261, 281))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.frame_2 = QtGui.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 261, 241))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.send_cmd = QtGui.QPushButton(self.frame_2)
        self.send_cmd.setGeometry(QtCore.QRect(0, 200, 85, 30))
        self.send_cmd.setObjectName(_fromUtf8("send_cmd"))
        self.lon = QtGui.QRadioButton(self.frame_2)
        self.lon.setGeometry(QtCore.QRect(10, 60, 101, 25))
        self.lon.setObjectName(_fromUtf8("lon"))
        self.loff = QtGui.QRadioButton(self.frame_2)
        self.loff.setGeometry(QtCore.QRect(10, 90, 101, 25))
        self.loff.setObjectName(_fromUtf8("loff"))
        self.other = QtGui.QRadioButton(self.frame_2)
        self.other.setEnabled(True)
        self.other.setGeometry(QtCore.QRect(10, 160, 101, 25))
        self.other.setAutoFillBackground(False)
        self.other.setChecked(True)
        self.other.setObjectName(_fromUtf8("other"))
        self.label_9 = QtGui.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 111, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.other_cmd = QtGui.QLineEdit(self.frame_2)
        self.other_cmd.setGeometry(QtCore.QRect(110, 160, 113, 30))
        self.other_cmd.setObjectName(_fromUtf8("other_cmd"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.pushButton = QtGui.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(70, 110, 85, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(0, 10, 231, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.Output = QtGui.QPlainTextEdit(self.tab_2)
        self.Output.setGeometry(QtCore.QRect(3, 30, 241, 75))
        self.Output.setReadOnly(True)
        self.Output.setObjectName(_fromUtf8("Output"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionDocs = QtGui.QAction(MainWindow)
        self.actionDocs.setObjectName(_fromUtf8("actionDocs"))
        self.actionLoad_from_CSV = QtGui.QAction(MainWindow)
        self.actionLoad_from_CSV.setObjectName(_fromUtf8("actionLoad_from_CSV"))
        self.actionSave_to_CSV = QtGui.QAction(MainWindow)
        self.actionSave_to_CSV.setObjectName(_fromUtf8("actionSave_to_CSV"))
        self.actionQuick_Start = QtGui.QAction(MainWindow)
        self.actionQuick_Start.setObjectName(_fromUtf8("actionQuick_Start"))
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionQuick_Start)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "LSM tool 2.0.1", None))
        self.label_2.setText(_translate("MainWindow", "Resolution", None))
        self.label_3.setText(_translate("MainWindow", "Pause", None))
        self.label_4.setText(_translate("MainWindow", "Sensitivity", None))
        self.scan.setText(_translate("MainWindow", "Scan!", None))
        self.label_5.setText(_translate("MainWindow", "Scanning:", None))
        self.label.setText(_translate("MainWindow", "Sending:", None))
        self.label_6.setText(_translate("MainWindow", "Status:", None))
        self.send_cmd.setText(_translate("MainWindow", "Send!", None))
        self.lon.setText(_translate("MainWindow", "Laser ON", None))
        self.loff.setText(_translate("MainWindow", "Laser Off", None))
        self.other.setText(_translate("MainWindow", "Other", None))
        self.label_9.setText(_translate("MainWindow", "Controls:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "To LSM", None))
        self.pushButton.setText(_translate("MainWindow", "Refresh", None))
        self.label_7.setText(_translate("MainWindow", "Data from the Trinket", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "From LSM", None))
        self.menuHelp.setTitle(_translate("MainWindow", "help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionDocs.setText(_translate("MainWindow", "Docs", None))
        self.actionLoad_from_CSV.setText(_translate("MainWindow", "Load from File", None))
        self.actionSave_to_CSV.setText(_translate("MainWindow", "Save to File", None))
        self.actionQuick_Start.setText(_translate("MainWindow", "Quick Start", None))

