# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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
        MainWindow.resize(1692, 933)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 106, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 42, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 56, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 106, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 42, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 56, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 42, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 106, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 42, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 56, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 42, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 42, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/laser-icon-6.jpg/laser-icon-6.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip(_fromUtf8(""))
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 40, 1031, 451))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.align = QtGui.QCommandLinkButton(self.gridLayoutWidget)
        self.align.setObjectName(_fromUtf8("align"))
        self.gridLayout.addWidget(self.align, 1, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.gridLayoutWidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.outZPos = QtGui.QSpinBox(self.groupBox_3)
        self.outZPos.setGeometry(QtCore.QRect(10, 60, 60, 27))
        self.outZPos.setMinimum(0)
        self.outZPos.setMaximum(0)
        self.outZPos.setSingleStep(1)
        self.outZPos.setObjectName(_fromUtf8("outZPos"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 91, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.pickleOut = QtGui.QPushButton(self.groupBox_3)
        self.pickleOut.setGeometry(QtCore.QRect(120, 60, 97, 27))
        self.pickleOut.setObjectName(_fromUtf8("pickleOut"))
        self.plotOut = QtGui.QPushButton(self.groupBox_3)
        self.plotOut.setGeometry(QtCore.QRect(120, 30, 97, 27))
        self.plotOut.setObjectName(_fromUtf8("plotOut"))
        self.plotOut_2 = QtGui.QPushButton(self.groupBox_3)
        self.plotOut_2.setGeometry(QtCore.QRect(220, 30, 151, 27))
        self.plotOut_2.setObjectName(_fromUtf8("plotOut_2"))
        self.pickleOut_2 = QtGui.QPushButton(self.groupBox_3)
        self.pickleOut_2.setGeometry(QtCore.QRect(220, 60, 97, 27))
        self.pickleOut_2.setObjectName(_fromUtf8("pickleOut_2"))
        self.alpha = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.alpha.setGeometry(QtCore.QRect(10, 90, 62, 27))
        self.alpha.setMaximum(1.0)
        self.alpha.setSingleStep(0.01)
        self.alpha.setProperty("value", 1.0)
        self.alpha.setObjectName(_fromUtf8("alpha"))
        self.label_16 = QtGui.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(80, 100, 66, 17))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout.addWidget(self.groupBox_3, 2, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.calRange = QtGui.QPushButton(self.groupBox)
        self.calRange.setGeometry(QtCore.QRect(20, 30, 391, 41))
        self.calRange.setObjectName(_fromUtf8("calRange"))
        self.calRange_2 = QtGui.QPushButton(self.groupBox)
        self.calRange_2.setGeometry(QtCore.QRect(20, 70, 391, 41))
        self.calRange_2.setObjectName(_fromUtf8("calRange_2"))
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)
        self.laserOff = QtGui.QPushButton(self.gridLayoutWidget)
        self.laserOff.setObjectName(_fromUtf8("laserOff"))
        self.gridLayout.addWidget(self.laserOff, 0, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.gridLayoutWidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.Xres = QtGui.QSpinBox(self.groupBox_2)
        self.Xres.setGeometry(QtCore.QRect(100, 70, 60, 27))
        self.Xres.setMinimum(1)
        self.Xres.setMaximum(255)
        self.Xres.setProperty("value", 50)
        self.Xres.setObjectName(_fromUtf8("Xres"))
        self.Yres = QtGui.QSpinBox(self.groupBox_2)
        self.Yres.setGeometry(QtCore.QRect(160, 70, 60, 27))
        self.Yres.setMinimum(1)
        self.Yres.setMaximum(255)
        self.Yres.setProperty("value", 50)
        self.Yres.setObjectName(_fromUtf8("Yres"))
        self.Zres = QtGui.QSpinBox(self.groupBox_2)
        self.Zres.setGeometry(QtCore.QRect(220, 70, 60, 27))
        self.Zres.setReadOnly(True)
        self.Zres.setMinimum(1)
        self.Zres.setMaximum(255)
        self.Zres.setObjectName(_fromUtf8("Zres"))
        self.scan = QtGui.QPushButton(self.groupBox_2)
        self.scan.setGeometry(QtCore.QRect(810, 0, 211, 41))
        self.scan.setObjectName(_fromUtf8("scan"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(120, 50, 16, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(180, 50, 16, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(250, 20, 16, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 81, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(310, 40, 91, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(310, 70, 91, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(310, 20, 151, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalSlider = QtGui.QSlider(self.groupBox_2)
        self.verticalSlider.setGeometry(QtCore.QRect(550, 20, 29, 71))
        self.verticalSlider.setMaximum(3)
        self.verticalSlider.setSingleStep(1)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.verticalSlider_2 = QtGui.QSlider(self.groupBox_2)
        self.verticalSlider_2.setGeometry(QtCore.QRect(580, 20, 29, 71))
        self.verticalSlider_2.setMaximum(10)
        self.verticalSlider_2.setProperty("value", 4)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setInvertedAppearance(False)
        self.verticalSlider_2.setInvertedControls(False)
        self.verticalSlider_2.setTickPosition(QtGui.QSlider.TicksAbove)
        self.verticalSlider_2.setObjectName(_fromUtf8("verticalSlider_2"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(540, 0, 81, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(530, 90, 91, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(610, 40, 131, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(480, 40, 71, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.zVals = QtGui.QLineEdit(self.groupBox_2)
        self.zVals.setGeometry(QtCore.QRect(130, 20, 113, 27))
        self.zVals.setObjectName(_fromUtf8("zVals"))
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(20, 30, 111, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.colorMax = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.colorMax.setGeometry(QtCore.QRect(410, 40, 62, 27))
        self.colorMax.setObjectName(_fromUtf8("colorMax"))
        self.colorMin = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.colorMin.setGeometry(QtCore.QRect(410, 70, 62, 27))
        self.colorMin.setObjectName(_fromUtf8("colorMin"))
        self.scan_pause = QtGui.QPushButton(self.groupBox_2)
        self.scan_pause.setGeometry(QtCore.QRect(810, 70, 211, 31))
        self.scan_pause.setFlat(False)
        self.scan_pause.setObjectName(_fromUtf8("scan_pause"))
        self.scanxyz = QtGui.QRadioButton(self.groupBox_2)
        self.scanxyz.setEnabled(False)
        self.scanxyz.setGeometry(QtCore.QRect(680, 80, 115, 22))
        self.scanxyz.setObjectName(_fromUtf8("scanxyz"))
        self.scanzxy = QtGui.QRadioButton(self.groupBox_2)
        self.scanzxy.setGeometry(QtCore.QRect(680, 100, 115, 22))
        self.scanzxy.setChecked(True)
        self.scanzxy.setObjectName(_fromUtf8("scanzxy"))
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(210, 50, 71, 17))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(270, 110, 351, 22))
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.warmup = QtGui.QCheckBox(self.groupBox_2)
        self.warmup.setGeometry(QtCore.QRect(630, 10, 141, 22))
        self.warmup.setChecked(False)
        self.warmup.setObjectName(_fromUtf8("warmup"))
        self.scan_cancel = QtGui.QPushButton(self.groupBox_2)
        self.scan_cancel.setGeometry(QtCore.QRect(810, 100, 211, 31))
        self.scan_cancel.setFlat(False)
        self.scan_cancel.setObjectName(_fromUtf8("scan_cancel"))
        self.scan_pause_2 = QtGui.QPushButton(self.groupBox_2)
        self.scan_pause_2.setGeometry(QtCore.QRect(810, 40, 211, 31))
        self.scan_pause_2.setFlat(False)
        self.scan_pause_2.setObjectName(_fromUtf8("scan_pause_2"))
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 2)
        self.laserOn = QtGui.QPushButton(self.gridLayoutWidget)
        self.laserOn.setObjectName(_fromUtf8("laserOn"))
        self.gridLayout.addWidget(self.laserOn, 0, 0, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.gridLayoutWidget)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.pickleIn = QtGui.QPushButton(self.groupBox_5)
        self.pickleIn.setGeometry(QtCore.QRect(80, 60, 251, 27))
        self.pickleIn.setObjectName(_fromUtf8("pickleIn"))
        self.gridLayout.addWidget(self.groupBox_5, 1, 1, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 10, 1031, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.image_label = QtGui.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(10, 500, 181, 201))
        self.image_label.setFrameShape(QtGui.QFrame.WinPanel)
        self.image_label.setObjectName(_fromUtf8("image_label"))
        self.camStop = QtGui.QPushButton(self.centralwidget)
        self.camStop.setGeometry(QtCore.QRect(10, 700, 181, 27))
        self.camStop.setObjectName(_fromUtf8("camStop"))
        self.camStart = QtGui.QPushButton(self.centralwidget)
        self.camStart.setGeometry(QtCore.QRect(10, 730, 181, 27))
        self.camStart.setObjectName(_fromUtf8("camStart"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(230, 580, 16, 17))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.Ypos_current = QtGui.QSpinBox(self.centralwidget)
        self.Ypos_current.setGeometry(QtCore.QRect(270, 600, 60, 27))
        self.Ypos_current.setMinimum(-255)
        self.Ypos_current.setMaximum(255)
        self.Ypos_current.setObjectName(_fromUtf8("Ypos_current"))
        self.Zpos_current = QtGui.QSpinBox(self.centralwidget)
        self.Zpos_current.setGeometry(QtCore.QRect(330, 600, 60, 27))
        self.Zpos_current.setMinimum(-255)
        self.Zpos_current.setMaximum(255)
        self.Zpos_current.setObjectName(_fromUtf8("Zpos_current"))
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(290, 580, 16, 17))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(350, 580, 16, 17))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.Xpos_current = QtGui.QSpinBox(self.centralwidget)
        self.Xpos_current.setGeometry(QtCore.QRect(210, 600, 60, 27))
        self.Xpos_current.setMinimum(-255)
        self.Xpos_current.setMaximum(255)
        self.Xpos_current.setObjectName(_fromUtf8("Xpos_current"))
        self.setPos = QtGui.QPushButton(self.centralwidget)
        self.setPos.setGeometry(QtCore.QRect(210, 630, 171, 27))
        self.setPos.setObjectName(_fromUtf8("setPos"))
        self.status = QtGui.QTextEdit(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(10, 760, 1011, 121))
        self.status.setReadOnly(True)
        self.status.setObjectName(_fromUtf8("status"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(1040, 10, 641, 871))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.plot = Canvas(self.groupBox_4)
        self.plot.setGeometry(QtCore.QRect(0, 110, 631, 731))
        self.plot.setObjectName(_fromUtf8("plot"))
        self.bar = QtGui.QFrame(self.groupBox_4)
        self.bar.setGeometry(QtCore.QRect(0, 50, 631, 41))
        self.bar.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bar.setFrameShadow(QtGui.QFrame.Raised)
        self.bar.setObjectName(_fromUtf8("bar"))
        self.intensity = QtGui.QCheckBox(self.centralwidget)
        self.intensity.setGeometry(QtCore.QRect(20, 670, 151, 22))
        self.intensity.setObjectName(_fromUtf8("intensity"))
        self.groupBox_7 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(220, 510, 171, 61))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.xCalib = QtGui.QLineEdit(self.groupBox_7)
        self.xCalib.setGeometry(QtCore.QRect(0, 20, 171, 27))
        self.xCalib.setObjectName(_fromUtf8("xCalib"))
        self.groupBox_8 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(610, 500, 321, 211))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.current = QtGui.QLCDNumber(self.groupBox_8)
        self.current.setGeometry(QtCore.QRect(30, 50, 231, 81))
        self.current.setObjectName(_fromUtf8("current"))
        self.startCurrent = QtGui.QPushButton(self.groupBox_8)
        self.startCurrent.setGeometry(QtCore.QRect(30, 130, 97, 27))
        self.startCurrent.setObjectName(_fromUtf8("startCurrent"))
        self.stopCurrent = QtGui.QPushButton(self.groupBox_8)
        self.stopCurrent.setGeometry(QtCore.QRect(160, 130, 97, 27))
        self.stopCurrent.setObjectName(_fromUtf8("stopCurrent"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1692, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.label_8.setBuddy(self.outZPos)
        self.label_4.setBuddy(self.Xres)
        self.label_5.setBuddy(self.Yres)
        self.label_6.setBuddy(self.zVals)
        self.label.setBuddy(self.zVals)
        self.label_2.setBuddy(self.Xres)
        self.label_3.setBuddy(self.colorMax)
        self.label_7.setBuddy(self.colorMin)
        self.label_10.setBuddy(self.verticalSlider_2)
        self.label_11.setBuddy(self.verticalSlider_2)
        self.label_12.setBuddy(self.verticalSlider_2)
        self.label_13.setBuddy(self.verticalSlider)
        self.label_14.setBuddy(self.zVals)
        self.label_15.setBuddy(self.Zres)
        self.label_17.setBuddy(self.Xpos_current)
        self.label_18.setBuddy(self.Ypos_current)
        self.label_19.setBuddy(self.Zpos_current)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "TLSM Control Software by Joseph R. Freeston", None))
        self.align.setText(_translate("MainWindow", "Align", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Output", None))
        self.outZPos.setPrefix(_translate("MainWindow", "#", None))
        self.label_8.setText(_translate("MainWindow", "Z point index", None))
        self.pickleOut.setText(_translate("MainWindow", "Python-pickle", None))
        self.plotOut.setText(_translate("MainWindow", "MatPlotLib", None))
        self.plotOut_2.setText(_translate("MainWindow", "Intensity Histogram", None))
        self.pickleOut_2.setText(_translate("MainWindow", "Python List", None))
        self.label_16.setText(_translate("MainWindow", "Alpha", None))
        self.groupBox.setTitle(_translate("MainWindow", "Calibration", None))
        self.calRange.setText(_translate("MainWindow", "Cal. HIGH Intensity", None))
        self.calRange_2.setText(_translate("MainWindow", "Cal. LOW Intensity", None))
        self.laserOff.setText(_translate("MainWindow", "Stop (off)", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Scan", None))
        self.scan.setText(_translate("MainWindow", "Scan now!", None))
        self.label_4.setText(_translate("MainWindow", "X", None))
        self.label_5.setText(_translate("MainWindow", "Y", None))
        self.label_6.setText(_translate("MainWindow", "Z", None))
        self.label.setText(_translate("MainWindow", "Z points to scan", None))
        self.label_2.setText(_translate("MainWindow", "Step Size:", None))
        self.label_3.setText(_translate("MainWindow", "Max intensity", None))
        self.label_7.setText(_translate("MainWindow", "Min intensity", None))
        self.label_9.setText(_translate("MainWindow", "Intensity Calibration", None))
        self.label_10.setText(_translate("MainWindow", "Longer Scan", None))
        self.label_11.setText(_translate("MainWindow", "Less Accuracy", None))
        self.label_12.setText(_translate("MainWindow", "Sample Averaging", None))
        self.label_13.setText(_translate("MainWindow", "Delay time", None))
        self.zVals.setText(_translate("MainWindow", "[-255, 0, 255]", None))
        self.label_14.setText(_translate("MainWindow", "(Python List)", None))
        self.scan_pause.setText(_translate("MainWindow", "PAUSE SCAN", None))
        self.scanxyz.setText(_translate("MainWindow", "Scan x,y,z", None))
        self.scanzxy.setText(_translate("MainWindow", "Scan z: x,y", None))
        self.label_15.setText(_translate("MainWindow", "Resolution", None))
        self.checkBox.setToolTip(_translate("MainWindow", "NOTE: disabled for multifocal scans.", None))
        self.checkBox.setText(_translate("MainWindow", "Subtract calibration values in ./calib/blank.pickle", None))
        self.warmup.setText(_translate("MainWindow", "Warmup sensor", None))
        self.scan_cancel.setText(_translate("MainWindow", "CANCEL SCAN", None))
        self.scan_pause_2.setText(_translate("MainWindow", "RESUME SCAN", None))
        self.laserOn.setText(_translate("MainWindow", "Laser on", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "File Operations", None))
        self.pickleIn.setText(_translate("MainWindow", "Load graph from pickle file", None))
        self.image_label.setText(_translate("MainWindow", "Camera Stream", None))
        self.camStop.setText(_translate("MainWindow", "Stop Camera Stream", None))
        self.camStart.setText(_translate("MainWindow", "Start Camera Stream", None))
        self.label_17.setText(_translate("MainWindow", "X", None))
        self.label_18.setText(_translate("MainWindow", "Y", None))
        self.label_19.setText(_translate("MainWindow", "Z", None))
        self.setPos.setText(_translate("MainWindow", "Set Position", None))
        self.status.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\" bgcolor=\"#000000\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Graph", None))
        self.intensity.setText(_translate("MainWindow", "Display intensity", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "X Axis cal Function", None))
        self.xCalib.setText(_translate("MainWindow", "4.17*np.exp(0.016*%i)", None))
        self.groupBox_8.setTitle(_translate("MainWindow", "Laser Current (mA)", None))
        self.startCurrent.setText(_translate("MainWindow", "Start", None))
        self.stopCurrent.setText(_translate("MainWindow", "Stop", None))

from canvas import Canvas
import GUI_resource_rc
