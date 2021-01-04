from dialog import Dialog


def autorange(min0, max0, val0, min1, max1, val1):
	return (int((val0/(max0/255))-min0), int((val1/(max1/255))-min1))


d = Dialog(autowidgetsize=True)
d.set_background_title("Laser Light Microscopy Control Software")

d.infobox("Loading...")
import CamView as cam
from pyGrapher import plot
import scalevals
import LSM
import time
from PIL import Image
import glob
import numpy as np
from numpy import mean
import statistics
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mpl
mpl.style.use('classic')

b=0

loopvar=True
while loopvar:
	try:
		a=LSM.LSM()
		loopvar=False
	except:
		try:
			a=LSM.LSM(port=glob.glob("/dev/ttyUSB*")[0])
			loopvar=False
		except:
			d.infobox("No arduino was recognized.\nPlease plug in the LSM.\n\nIf it is already plugged in, it may be in use by another program.")
			time.sleep(1)

#d.msgbox("Remove any previous specimens from the microscope.")

off=0.7 #The lowest (as a percent) value of the laser brightness through the specimen

loopvar=True
while loopvar:
	ocode, otag = d.menu("Choose an option:", choices=[("1) Align", "Align the laser/sensor"), ("2) Test", "Test the optics"), ("3) Calibrate", "Calibrate the optical system"), ("4) Scan", "Run a scan with the most recent calibration")], extra_button=True, extra_label="Exit")
	loopvar=(ocode!=d.EXTRA) #Only keep looping if the 'OK' option was selected.
	if ocode==d.OK:
		if otag=="1) Align":
			d.infobox("Align the camera so that the dot is roughly centered in the picture and stable.\nWhen you are done, press ESC.")
			a.pos(127,0,0)
			cam.cheese()
		if otag=="2) Test":
			#d.msgbox("Do not change anything from the alignment step, but make sure that the power supply is on and at 3-5 volts depending on your final magnification level.")
			code=d.CANCEL
			while code!=d.EXTRA:
				code, tag = d.menu("Testing", choices=[("Brain", "Test the Arduino serial connection"), ("Actuators", "Test the actuators and lens movement"), ("Raw", "Send a raw command or coordinates")], extra_button=True, extra_label="Back")
				if code==d.OK:
					if tag=="Raw":
						ncode, ntag = d.inputbox("What command?")
						if ncode==d.OK:
							a.ser.write(bytes(ntag+"\n", "utf-8"))
							d.infobox("Awaiting response...")
							d.msgbox(str(a.ser.readline().decode('utf-8')))
					if tag=="Brain":
						if(a.test()):
							d.msgbox("Passed.")
						else:
							d.msgbox("Failed.")
					if tag=="Actuators":
						passed=True
						d.infobox("Square Test...")
						passed&=a.laser(1)
						passed&=a.pos(127,0,0)
						#passed&=a.pos(255,0,0)
						passed&=a.pos(255,255,0)
						#passed&=a.pos(127,255,0)
						passed&=a.pos(0,255,0)
						#passed&=a.pos(127,-255,0)
						passed&=a.pos(0,-255,0)
						#passed&=a.pos(127,-255,0)
						passed&=a.pos(255,-255,0)
						#passed&=a.pos(127,255,0)
						passed&=a.pos(0,0,0)
						a.laser(0)
						if passed:
							d.msgbox("Passed.")
						else:
							d.msgbox("FAILED!")
						d.infobox("Testing Z-axis...")
						a.laser(1)
						passed&=a.pos(0,0,-255)
						passed&=a.pos(0,0,0)
						passed&=a.pos(0,0,255)
						a.pos(0,0,0)
						a.laser(0)
						if passed:
							d.msgbox("It supposedly passed.")
						else:
							d.msgbox("FAILED!")
						d.infobox("Testing actuator filtering/noise")
						a.laser(1)
						a.pos(-200,0,0)
						a.pos(-100,0,0)
						a.pos(0,0,0)
						a.pos(100,0,0)
						a.pos(200,0,0)
						a.pos(0,-200,0)
						a.pos(0,-100,0)
						a.pos(0,0,0)
						a.pos(0,100,0)
						a.pos(0,200,0)
						a.pos(0,0,-200)
						a.pos(0,0,-100)
						a.pos(0,0,0)
						a.pos(0,0,100)
						a.pos(0,0,200)
						a.pos(0,0,0)
						a.laser(0)
						d.msgbox("Finished.")
		if otag=="3) Calibrate":
			#d.msgbox("Make sure that the specimen is out of the path of the laser!")
			code=d.CANCEL
			while code!=d.EXTRA:
				code, tag = d.menu("Calibration", choices=[("1) Range", "Increase the color sensitivity"), ("2) Focus", "Focus the laser for better quality images")], extra_button=True, extra_label="Back")
				if code==d.OK:
					if tag=="2) Focus":
						d.msgbox("Please make sure that the camera is aligned.")
						best=cam.read()
						bestpos=0
						for focus in range(-255,255, 5):
							d.infobox("Scanning for focus ("+str(focus)+", coarse)...")
							if cam.read() < best:
								bestpos=focus
						for focus in range(bestpos-10, bestpos+10):
							d.infobox("Scanning for focus ("+str(focus)+", fine)...")
							if cam.read() < best:
								bestpos=focus
						d.msgbox("Optimal focus value: "+str(focus))
					if tag=="1) Range":
						#a.laser(1)
						m=[]
						d.msgbox("Please make sure that there are no obstructions to the laser, and that the camera is aligned.")
						d.infobox("Calibrating...\n(ON state)")
						cam.warmup()
						for i in range(30):
							m+=[cam.read()]
						m0on=statistics.median(m) #find the median of all 30 samples
						m0on+=np.mean(m)
						m0on/=2 #Average that with the mean
						d.msgbox("Please obstruct the laser to the maximum extent needed for this scan.")
						d.infobox("Calibrating...\n(OFF state)")
						m=[]
						cam.warmup()
						for i in range(30):
							m+=[cam.read()]
						m0off=statistics.median(m) #find the median of all 30 samples
						m0off+=np.mean(m)*0.5
						m0off/=2
						with open("./calib/m0on.txt", "w") as file:  #Write calibration values to files:
							file.write(str(m0on))
							file.close()
						with open("./calib/m0off.txt", "w") as file:
							file.write(str(m0off))
							file.close()
						calib_show =d.yesno("Calibration values updated.\n", yes_label="Continue", no_label="Show Calibration Data")
						if calib_show==d.CANCEL:  #The user has requested to see the values
							d.msgbox("M0on: "+str(m0on)+"\nM0off: "+str(m0off))
		if otag=="4) Scan":
			with open("./calib/m0on.txt", "r") as file:  #Write calibration values to files:
				m0on=int(float(file.read()))
				file.close()
			with open("./calib/m0off.txt", "r") as file:
				m0off=int(float(file.read()))
				file.close()
			scaler=scalevals.Scaler(int(m0off), int(m0on)) #Set up a scaler for the values
			d.msgbox("Using last calibration values from "+str(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getmtime("./calib/m0off.txt"))))+".")
			b,z=d.rangebox("Z focus value: ", min=-255, max=255, init=0)
			b,step=d.rangebox("Enter the step size.", min=1, max=255, init=20)
			b,accuracy=d.rangebox("Enter the number of camera samples to take", min=0, max=10, init=2)
			#a.laser(1)
			d.infobox("Align the camera so that the dot is roughly centered in the picture and stable.\nMake sure that the specimen is also centered. When you are done, press ESC.")
			a.pos(127,0,z)
			cam.cheese()
			d.msgbox("Ready to start?")
			a.pos(0,0,0)
			d.pause("Ahh! The suspense!\n\n", seconds=5)
			#Clear the screen for plotting:
			for i in range(100):
				print("")
			plot(0, 65, 0, char=" ")
			print("^^ Image ^^")
			#Start scanning:
			#d.gauge_start(text="Scanning...\n", percent=0)
			pic=[[]*int(512/step)]*int(255/step) #Generate a matrix that is equal to the size of the scan, each pixel being represented by an int
			total_pixels=int(255/step)*int(512/step)
			xpos=0
			ypos=0
			for i in range(100): #Clear the screen so we can plot on it
				print(" ")
			a.test() #Re-establish the serial connection if it died.
			cam.warmup()
			img=[]
			imgindex=0
			for xval in range(0,255,step):
				img+=[[]]
				for yval in range(-255,255,step): #For each pixel
					#d.gauge_update(int(100*((xval*yval)/total_pixels)), text="Scanning...\n("+str(xval)+","+str(yval)+")") #update progress bar
					#print("Gettin' there...")
					a.pos(xval, yval, z) #Get there
					#print("("+str(xpos)+", "+str(ypos)+")")
					#print("("+str(xval)+", "+str(yval)+")\n\n")
					#try:
					#print("Collecting Samples...")
					samples=[]
					#for i in range(accuracy):
					#	cam.read()
					for i in range(accuracy):
						samples+=[cam.read()]
					pix=mean(samples)
					img[imgindex]+=[pix]
					#pix=a.ldr(sleepval=int(accuracy))+(0,) #record the pixel
					#pic[xpos][ypos]=autorange(m0off, m0on, pix[0], m1off, m1on, pix[1])
					#print(a.ldr(sleepval=int(accuracy))+(0,))
					#except:
					#	print("Nonexistent pixel.\n(The array wasn't auto-generated correctly, but this is okay.  This just means that a few pixels that weren't meant to be scanned were scanned.)")
					#repeat for the next pixel
					#if yval==0 or xval==0:
					#	plot(xpos, ypos, int(scaler.scaleto(pix)*7+1), char="#")
					#	plot(xpos+1, ypos, int(scaler.scaleto(pix)*7+1), char="#")
					#else:
					#print("Plotting Pixel...")
					scaled=scaler.scaleto(pix)*7+1
					plot(xpos, ypos, int(scaled), char=str(int(scaled)))
					plot(xpos+1, ypos, int(scaled), char=str(int(scaled)))
					ypos+=1
				ypos=0
				xpos+=2
				imgindex+=1
			#a.laser(0)
			a.pos(0,0,0)
			#print(pic)
			#time.sleep(int(accuracy))
			#d.gauge_stop()
			d.infobox("Processing...")
			img=np.rot90(img)
			img=np.rot90(img)
			img=np.rot90(img)
			d.msgbox("Finished and ready to display!")
			print(img)

						ncode, ntag = d.inputbox("Graph Title?")
						if ncode==d.OK:
							graphtitle=ntag
						else:
							graphtitle="unknown"

			plt.style.use('ggplot')
			plt.figure(1)
			plt.title("Scan of "+graphtitle+":")
			plt.imshow(img)
			plt.figure(2)
			plt.title("Histogram of Shades")
			plt.hist(img, bins=10)


			d.infobox("Displayed the image!")
			plt.show()
			#b,path=d.fselect("./")
			#im = Image.fromarray(np.array(pic).astype('uint8'))
			#aplot=plt.imshow(np.array(pic).astype('uint8')[:,0,0])
			#refplot=plt.imshow(np.array(pic).astype('uint8')[0,:,0])
			#aplot.set_cmap('nipy_spectral')
			#plt.colorbar()
			#im.save(path)
	if ocode=='ok':
		a.close()

