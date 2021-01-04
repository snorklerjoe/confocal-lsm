#!/usr/bin/python3

import sys
from dialog import Dialog
import time
import glob
import statistics
import numpy as np
import threading
import pickle

from PyQt4 import QtCore, QtGui
from gui import *

from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar 
import matplotlib.pyplot as plt
plt.style.use("ggplot")

import LSM # Control library



# Main Window class:
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self, microscope):
		self.image=[[0,1], [1,2]]
		self.images=[self.image]
		self.laser_state=False
		self.laseronyet=False # True since the first time the laser is power on
		self.scanning=False   # Not currently scanning

		self.microscope=microscope # Take in the LSM class.
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		# Connect buttons:
		self.laserOn.clicked.connect(lambda:self.laser(True))
		self.laserOff.clicked.connect(lambda:self.laser(False))

		self.align.clicked.connect(self.alignLaser)
		self.camStart.clicked.connect(self.camInit)
		self.camStop.clicked.connect(self.camStopper)

		self.setPos.clicked.connect(lambda:self.goto(self.Xpos_current.value(), self.Ypos_current.value(), self.Zpos_current.value()))

		self.calRange.clicked.connect(self.calibrate_range_on)
		self.calRange_2.clicked.connect(self.calibrate_range_off)

		self.scan_cancel.setEnabled(False)
		self.plotOut.setEnabled(False)
		self.plotOut_2.setEnabled(False)
		self.pickleOut.setEnabled(False)
		self.pickleOut_2.setEnabled(False)

		self.plotOut.clicked.connect(self.plotimg)
		self.plotOut_2.clicked.connect(self.plothist)
		self.pickleIn.clicked.connect(self.loadFromPickle)
		self.pickleOut.clicked.connect(lambda: pickle.dump(self.images, open(QtGui.QFileDialog.getOpenFileName(self, 'Filename?', "./", "Pickle files (*.pickle)"), "wb")))
		self.pickleOut_2.clicked.connect(lambda: self.msg(str(self.images)))

		self.scan.clicked.connect(self.startscan)
		self.scan_cancel.clicked.connect(self.stopscan)
		self.scan_pause.clicked.connect(self.pause)
		self.scan_pause_2.clicked.connect(self.resume)

		self.navbar = NavigationToolbar(self.plot, self)
		self.bar.setLayout(QtGui.QVBoxLayout())
		self.bar.layout().addWidget(self.navbar)
		#self.plot.figure.figsize=(5,1)
		self.plotimg()

		self.current.display("ABC")
		self.currentTimer = QtCore.QTimer()
		self.currentTimer.timeout.connect(self.updateCurrentMeter)

		self.startCurrent.clicked.connect(lambda: self.currentTimer.start())
		self.stopCurrent.clicked.connect(lambda: self.currentTimer.stop())

		self.import_calib()
		self.msg("Ready.")
	def laser(self, value):
		self.laser_state=value
		if not self.laseronyet and value:
			msg=QtGui.QMessageBox()
			msg.setIcon(QtGui.QMessageBox.Warning)
			msg.setText("Laser radiation can be dangerous and can cause severe eye damage, including blindness.\n\nEnsure that the LSM is properly set up and plugged in before proceeding, so as to not cause injury or damage to the microscope.")
			#msg.setTitle("Continue?")
			msg.setStandardButtons(QtGui.QMessageBox.Ok)
			msg.exec_()
			self.laseronyet=True
		self.msg("Set laser to " + ("ON" if value else "OFF") )
		self.microscope.laser(value)
		if not value:
			time.sleep(1)
			self.microscope.laser(value)
	def camStopper(self):
		self.msg("Stopping Camera Stream.")
		self.camTimer.stop()
		self.image_label.clear()
		self.image_label.setText("Camera Stream")
	def camInit(self):
		self.msg("Starting Camera Stream.")
		self.camTimer = QtCore.QTimer()
		self.camTimer.timeout.connect(self.camRun)
		self.camTimer.start(30)
	def camRun(self):
		#frame = LSM.CamView.cv2.cvtColor(LSM.CamView.get_cropped().resize((120,120)), LSM.CamView.cv2.COLOR_GRAY2RGB)
		#print(frame.shape)
		if self.intensity.isChecked():
			self.msg(str(self.getIntensity()))
		#frame=LSM.CamView.cv2.cvtColor(frame, LSM.CamView.cv2.COLOR_BGR2GRAY)
		#frame=LSM.CamView.cv2.cvtColor(frame, LSM.CamView.cv2.COLOR_BGR2RGB)
		_, frame = LSM.CamView.cam.read()
		self.image_label.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QtGui.QImage.Format_RGB888)))
	def goto(self, x, y, z, delay=0, noQt=False):
		if x != 0:
			self.goto(0,y,z, noQt=noQt)
			time.sleep(0.1+delay)
		if x>255 or x<0 or abs(y)>255 or abs(z)>255:
			raise ValueError("Bad location specified.")

		if x==0:
			print("Zeroing X axis.")
		else:
			x = eval(self.xCalib.text() % x)

		if x=="-inf":
			x=0
		elif x>255:
			x=255
		elif x<0:
			x=0

		print(x)
		
		if not self.laser_state and not noQt:
			msg=QtGui.QMessageBox()
			msg.setIcon(QtGui.QMessageBox.Critical)
			msg.setText("Cannot move the laser without the laser turned on.\n\nPlease turn on the laser.")
			#msg.setTitle("Continue?")
			msg.setStandardButtons(QtGui.QMessageBox.Ok)
			msg.exec_()
			return
			#self.msg("Turning on laser...")
			#self.laser(True)
			#time.sleep(0.1)
			#self.laser(True) # Just in case...
		elif not self.laser_state:
			raise ValueError("Laser must be turned on.")
		if not noQt:
			self.msg("Going to (%i, %i, %i)." % (x, y, z))
			self.Xpos_current.setValue(x)
			self.Ypos_current.setValue(y)
			self.Zpos_current.setValue(z)

		self.microscope.pos(x,y,z)

	def alignLaser(self):
		self.goto(127,0,0)
		self.camInit()
	def msg(self, txt):
		self.status.append('<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#7fff00;">'+txt+'</span></p>')
	def calibrate_range_on(self):
		msg=QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Question)
		msg.setText("The laser should be aligned such that the maximum intensity possible will be measured.\nThe laser, if currently off, will be turned on by this process.\n\nContinue?")
		#msg.setTitle("Continue?")
		msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
		if msg.exec_()==QtGui.QMessageBox.Ok:
			if not self.laser_state:
				self.msg("Turning on laser...")
				self.laser(True)
				time.sleep(0.1)
				self.laser(True) # Just in case...
			self.msg("Warming up...")
			LSM.CamView.warmup()
			self.msg("Taking measurements...")
			m=[]
			for i in range(30):
				m+=[LSM.CamView.read()]
			m0on=statistics.median(m) #find the median of all 30 samples
			m0on+=np.mean(m)
			m0on/=2 #Average that with the mean
			with open("./calib/m0on.txt", "w") as file:  #Write calibration values to files:
				file.write(str(m0on))
				file.close()
			msg.setIcon(QtGui.QMessageBox.Information)
			msg.setText("Done.")
			#msg.setTitle("Continue?")
			msg.setStandardButtons(QtGui.QMessageBox.Ok)
			msg.exec_()

			self.msg("Calibrated ON state...")
			self.msg("Got "+str(m0on)+" and saved to ./calib/m0on.txt")
			self.import_calib()
	def calibrate_range_off(self):
		msg=QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Question)
		msg.setText("The laser should be aligned such that the minimum intensity possible will be measured.\n\nContinue?")
		#msg.setTitle("Continue?")
		msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
		if msg.exec_()==QtGui.QMessageBox.Ok:
			self.msg("Warming up...")
			LSM.CamView.warmup()
			self.msg("Taking measurements...")
			m=[]
			for i in range(30):
				m+=[LSM.CamView.read()]
			m0off=statistics.median(m) #find the median of all 30 samples
			m0off+=np.mean(m)*0.5
			m0off/=2
			with open("./calib/m0off.txt", "w") as file:
				file.write(str(m0off))
				file.close()

			msg.setIcon(QtGui.QMessageBox.Information)
			msg.setText("Done.")
			#msg.setTitle("Continue?")
			msg.setStandardButtons(QtGui.QMessageBox.Ok)
			msg.exec_()

			self.msg("Calibrated OFF state...")
			self.msg("Got "+str(m0off)+" and saved to ./calib/m0off.txt")
			self.import_calib()
	def import_calib(self):
		try:
			with open("./calib/m0off.txt", "r") as file:
				self.colorMin.setValue(float(file.read()))
				file.close()
			with open("./calib/m0on.txt", "r") as file:
				self.colorMax.setValue(float(file.read()))
				file.close()
		except:
			self.msg("WARNING: not fully calibrated yet.")
	def startscan(self):
		self.doneScanning = False
		msg=QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Question)
		msg.setText("The specimen should be aligned and ready to scan.\n\nAre you sure you want to continue?")
		#msg.setTitle("Continue?")
		msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
		if msg.exec_() == QtGui.QMessageBox.Ok:
			print(self.zVals.text())
			self.msg("Beginning scan with resolution %i:%i,%i" % (self.Xres.value(), self.Yres.value(), len(eval(self.zVals.text()))))
			self.scan_iteration = 0
			self.scanTimer = QtCore.QTimer()
			self.scanTimer.timeout.connect(self.scanLoop)
			self.scanTimer.start(30)
		else:
			self.msg("Scan aborted.")
		self.scan_cancel.setEnabled(True)
	def scanLoop(self):
		if self.scan_iteration == 0:       # Alert user we are initializing
			self.msg("Initializing...")
			self.scan_iteration = 0.5	 # Init scan:
			return
		if self.scan_iteration == 0.5:
			#Generate scanning tables:
			#self.image=[[0]*int(255/self.Xres.value())]*int((355*2)/self.Yres.value())
			self.image = []
			self.images = []
			self.scanx = list(range(0,256,self.Xres.value()))
			self.scany = list(range(-255,256,self.Yres.value()))
			try:
				print(self.zVals.text())
				self.scanz=eval(self.zVals.text()) # Grab/evaluate the list from the user
				#if len(self.scanz)>1:
				#	raise NotImplementedError("Only one Z scan value is currently supported.")
				if (np.max(self.scanz))>255 or (np.min(self.scanz)) < -255:
					raise TypeError("Invalid integers out of scanning range. Please fix.")
			except Exception as e:
				print(e)
				self.msg("Malformed python list in \"Z points to scan\"!")
				msg = QtGui.QMessageBox()
				msg.setIcon(QtGui.QMessageBox.Critical)
				msg.setText("Could not complete scan:\n\nMalformed python list in \"Z points to scan\"!\nShould be a list of integers: [0]\nAll integers must be -255 to 255\nSee Terminal for more info.\n")
				msg.setStandardButtons(QtGui.QMessageBox.Ok)
				msg.exec_()
				self.stopscan()
				return
			#Start a thread for doing the scanning:
			self.scan_iteration=1
			self.scanningThread = threading.Thread(target=self.scanner, name="LSM Scanner")
			self.progress = 0
			self.scan_iteration=1
			self.laser(True)
			self.scanningThread.start()
			self.msg("Scanning...")
			return #Exit this function

			#The rest of the code in this case of this function is not used and serves only archival purposes.
			#Generate a full table of points:
			self.scanPoints = []
			self.imageIndicies = []
			xind=-1
			if self.scanzxy.isChecked():
				for z in self.scanz:
					imageindex = [-1,-1]
					for x in self.scanx:
						imageindex[0] += 1			#Generate a full table of points:
			self.scanPoints = []
			self.imageIndicies = []
			xind=-1
			if self.scanzxy.isChecked():
				for z in self.scanz:
					imageindex = [-1,-1]
					for x in self.scanx:
						imageindex[0] += 1
						imageindex[1] = 0
						for y in self.scany:
							self.scanPoints += [(x, y, z)]
							self.imageIndicies.append(imageindex[:]) # Need to cpy list w/ : index
							imageindex[1] += 1
							print(imageindex)
							print(self.imageIndicies)
				for x in self.scanx:
					xind+=1
					self.image+=[[]]
					self.image[xind]+=[0]
					for y in self.scany:
						self.image[xind]+=[0]
			else:
				raise NotImplementedError("No. You cannot use the scan x,y,z feature.")
				for x in self.scanx:
					for y in self.scany:
						for z in self.scanz:
							self.scanPoints+=[(x, y, z)]
			self.imageindex=[0,0]
			print(self.scanPoints)
			#Turn on the laser and confirm:
			self.laser(True) #Make sure that the laser is turned on...
			msg=QtGui.QMessageBox()
			msg.setIcon(QtGui.QMessageBox.Question)
			msg.setText("All set?\n\n(is the laser on? / are you ready?)")
			#msg.setTitle("Continue?")
			msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
			if msg.exec_() == QtGui.QMessageBox.Cancel:
				self.stopscan()
				self.msg("Aborted scan.")
				return
			self.Zres.value=len(self.scanz)
			self.scan_iteration=1
			self.currentZpos=self.scanPoints[0][2]
			self.imagetemplate = self.image
			print("Shape: %s" % str(np.array(self.image).shape))
			LSM.CamView.warmup()
			return
		# Run the scan:
		else:
			if self.progress<=99 or not self.doneScanning:
				self.progressBar.setValue(self.progress) # Set the progress
				return
				#try:
				#if self.scanPoints[self.scan_iteration-1][0]!=0:
				#	self.goto(0, self.scanPoints[self.scan_iteration-1][1], self.scanPoints[self.scan_iteration-1][2])
				#	time.sleep(self.verticalSlider.value()+0.2)
				#self.goto(self.scanPoints[self.scan_iteration-1][0], self.scanPoints[self.scan_iteration-1][1], self.scanPoints[self.scan_iteration-1][2])

				if np.sum(self.imageindex) == 0:
					self.msg("Beginning layer %i" % eval(self.zVals.text()).index(self.scanPoints[self.scan_iteration-1][2]))
				self.imageindex = self.imageIndicies[self.scan_iteration]
				self.goto(self.scanPoints[self.scan_iteration-1][0], self.scanPoints[self.scan_iteration-1][1], self.scanPoints[self.scan_iteration-1][2], self.verticalSlider.value()+0.1)
				time.sleep(self.verticalSlider.value())
				intreadings = []
				intensity = self.getIntensity()
				self.image[self.imageindex[0]][self.imageindex[1]] = intensity
				self.msg(str(self.scanPoints[self.scan_iteration-1])+" --> "+str(intensity))
				self.msg(str(self.imageindex))
				self.progressBar.setValue(100*(self.scan_iteration/len(self.scanPoints)))
				self.scan_iteration+=1
				self.imageindex[1]+=1
				#self.msg(str(self.imageindex))
				#if self.imageindex[1] == len(self.image[self.imageindex[0]])-1:
				#	self.imageindex[1] = 0
				#	self.imageindex[0] += 1
				if self.currentZpos != self.scanPoints[self.scan_iteration-1][2]:
					raise IndexError()
				#except IndexError as e:
			else:
				#print(e)
				self.msg("Done with scan.")
				#if self.scanPoints[self.scan_iteration-1][2] != self.currentZpos:  # Next layer:
				#if 100*(self.scan_iteration/len(self.scanPoints)) < 70:
				#	self.image = np.rot90(self.image) #Rotate it for matplotlib :)
				#	self.image = np.rot90(self.image) #Rotate it for matplotlib :)
				#	self.image = np.rot90(self.image) #Rotate it for matplotlib :)
				#	self.image = self.image[:-1]
				#	self.msg("Starting next layer...")
				#	self.images.append(self.image)
				#	self.image = self.imagetemplate
				#	self.imageindex = [0,0]
				#	self.currentZpos = self.scanPoints[self.scan_iteration-1][2]
				#	return
				self.progressBar.setValue(self.progress)
				#We're done!
				msg=QtGui.QMessageBox()
				msg.setIcon(QtGui.QMessageBox.Information)
				
				self.goto(0,0,0)
				self.laser(False)
				msg.setText("Scan finished.")
				#msg.setTitle("Continue?")
				msg.setStandardButtons(QtGui.QMessageBox.Ok)
				msg.exec_()
				self.msg("Done scanning!")
				self.plotOut.setEnabled(True)
				self.plotOut_2.setEnabled(True)
				self.pickleOut.setEnabled(True)
				self.pickleOut_2.setEnabled(True)
				if self.checkBox.isChecked():
					self.image = (np.array(pickle.load(open("./calib/blank.pickle", "rb")))-np.array(self.image)).tolist()
				self.outZPos.setMinimum(0)
				self.outZPos.setMaximum(len(self.images)-1)

				self.stopscan()
					
				#self.image = np.rot90(self.image) #Rotate it for matplotlib :)
				#self.image = np.rot90(self.image) #Rotate it for matplotlib :)
				#self.image = np.rot90(self.image) #Rotate it for matplotlib :)
				#self.image = self.image[:-1]
				#self.msg("Done with layer %i" % eval(self.zVals.text()).index(self.scanPoints[self.scan_iteration-1][2]))
				#self.images.append(self.image)
				#self.image = []
				#self.imageindex = [0,0]

				#Generate averaged layer:   # Never mind-- We can do that with small alpha values.
				#avgimg = self.images[0]
				#for img in self.images[1:]:
				#	for ri, row in enumerate(img):
				#		for pi, pixel in enumerate(row):
				#			avgimg[ri][pi]+=pixel
				#self.images.append(avgimg)

				return
	def scanner(self):
		'''
		Threading target for scanning. :)
		'''
		print("Started scanning thread")
		self.images=[]
		LSM.CamView.warmup()
		scannedpoints = 0
		totalpoints = len(self.scanz) * len(self.scanx) * len(self.scany)
		print("Beginning scan...")
		for zindex, z in enumerate(self.scanz):
			self.images.append([])
			for xindex, x in enumerate(self.scanx):
				self.images[zindex].append([])
				for y in self.scany:
					self.goto(x,y,z, delay=self.verticalSlider.value()/2, noQt=True)
					time.sleep(self.verticalSlider.value())
					print("measuring intensity")
					intensity = self.getIntensity()
					print("(%i, %i, %i) -> %f" % (x, y, z, intensity))
					self.images[zindex][xindex].append(intensity)
					self.progress=100*scannedpoints/totalpoints
					scannedpoints += 1
			self.images[zindex] = np.rot90(self.images[zindex]) #Rotate it for matplotlib :)
			self.images[zindex] = np.rot90(self.images[zindex]) #Rotate it for matplotlib :)
			self.images[zindex] = np.rot90(self.images[zindex]) #Rotate it for matplotlib :)
		self.doneScanning = True
	def getIntensity(self):
		intreadings=[]
		if self.warmup.isChecked():
			LSM.CamView.warmup()
		for i in range(self.verticalSlider_2.value()):
			intreadings += [LSM.CamView.read()]
		return statistics.mean(intreadings)
	def stopscan(self):
		self.scan_cancel.setEnabled(False)
		self.scanTimer.stop()
	def selectLayer(self):
		self.image = self.images[self.outZPos.value()]
	def plotimg(self):
		'''
		Plots the image in matplotlib.
		'''
		#a.hold(False)
		self.selectLayer()
		self.plt=self.plot.figure.add_subplot(111)
		self.plt.imshow(self.image, cmap = plt.cm.jet, interpolation = 'none', extent = [255, 0, 255, -255], alpha = self.alpha.value())
		self.plot.draw()
	def plothist(self):
		'''
		Plots the image in matplotlib.
		'''
		#a.hold(False)
		self.selectLayer()
		self.plt=self.plot.figure.add_subplot(111)
		self.plt.hist(self.image, bins=10)
		self.plot.draw()
	def loadFromPickle(self):
		self.images = pickle.load(open(QtGui.QFileDialog.getOpenFileName(self, 'File?', "./", "Pickle files (*.pickle)"), "rb"))
		self.outZPos.setMaximum(len(self.images)-1)
		self.plotOut.setEnabled(True)
		self.plotOut_2.setEnabled(True)
		self.pickleOut.setEnabled(True)
		self.pickleOut_2.setEnabled(True)
	def pause(self):
			self.scanTimer.stop()
	def resume(self):
			self.scanTimer.timeout.connect(self.scanLoop)
			self.scanTimer.start(30)
	def updateCurrentMeter(self):
		self.current.display(microscope.current())

#	def scanner(self):
#		'''
#			Does the scan.
#		'''
#		for xval in self.scanx:
#			for yval in self.scany:
#				for zval in self.scanz:
#					self.text2out="(%i, %i, %i) --> %f" % (xval, yval, zval, 0)
#					self.outneeded=True
#					print("Outneeded")
#					if not self.scanning:
#						return
#					while self.outneeded:
#						time.sleep(0.001)


# Wait for the user to plug in the LSM:
d = Dialog(autowidgetsize=True)
d.set_background_title("Laser Light Microscopy Control Software")
loopvar=True
while loopvar:
	try:
		microscope=LSM.LSM()
		loopvar=False
	except:
		try:
			a=LSM.LSM(port=glob.glob("/dev/ttyUSB*")[0])
			loopvar=False
		except:
			d.infobox("No arduino was recognized.\nPlease plug in the LSM.\n\nIf it is already plugged in, it may be in use by another program.")
			time.sleep(1)
d.infobox("Connected!\nLaunching GUI...")

# Launch the GUI
app = QtGui.QApplication(sys.argv)
try:
	window=MainWindow(microscope)
except NameError:
	print("Try un-plugging and plugging back in the microscope.")
	exit()
window.show()
app.exec_()
d.infobox("Exited OK.")
exit()