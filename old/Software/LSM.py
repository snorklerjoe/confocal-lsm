import glob
import serial
import time
import CamView

class LSM:
	'''
	This class allows for easy communication to the Arduino Nano "brains" of the LSM (for controlling the microscope).
	'''
	def __init__(self, port='/dev/ttyUSB0'):
		self.ser=serial.Serial(port, 115200, timeout=1) #Set up serial interface
		self.buf=b'' #set up a simple buffer variable

		self.curpos=[0,0,0]
	def test(self):
		try:
			self.ser.write(b"TEST\n")
		except:
			self.__init__(port=glob.glob("/dev/ttyUSB*")[0])
			self.ser.write(b"TEST\n")
		return (self.ser.readline()==b'OK.\r\n')
	def joy(self):
		self.test()
		self.ser.write(b"JOY\n")
		self.buf=self.ser.readline()
		return (int(str(self.buf)[2:-5].split(" ")[0]), int(str(self.buf)[2:-5].split(" ")[1]))
	def current(self):
		'''
		Returns the mA going through the laser.
		'''
		self.ser.write(b"Current\n")
		self.buf=self.ser.readline()
		#
		# print(self.buf)
		return (int(self.buf[:-2])/1024)*5
	def ldr(self, sleepval=2):
		#self.test()
		time.sleep(sleepval)
		#self.ser.write(b"LDR\n")
		#self.buf=self.ser.readline()
		#return (int(str(self.buf)[2:-5].split(" ")[0]), int(str(self.buf)[2:-5].split(" ")[1]))
		return CamView.read()
	def pos(self,x,y,z, sleepval=0.001):
		if type(x) != int:
			print("WARNING: X value is not an integer. Fixing...")
			x=int(x)
		for i in range(3):
			self.test()
			while abs(self.curpos[1]-y)+abs(self.curpos[2]-z)>100:
				self.ser.write(bytes(('('+str(x)+','+str(int((y+self.curpos[1])/2))+','+str(int((z+self.curpos[2])/2))+')'), "utf-8"))
				self.curpos[2]=int((z+self.curpos[2])/2)
				self.curpos[1]=int((y+self.curpos[1])/2)
				self.curpos[0]=int(x)
				self.ser.readline()
				time.sleep(sleepval)
			self.ser.write(bytes(('('+str(x)+','+str(y)+','+str(z)+')'), "utf-8"))
			time.sleep(sleepval)
		return(self.ser.readline()==b'Done!\r\n')
	def laser(self, value):
		self.test()
		if value:
			self.ser.write(b'Laser on\n')
		else:
			self.ser.write(b'Laser off\n')
		time.sleep(2)
		return 1
	def simplescan(self, step, z, accuracy): #Scan a square
		self.test()
		self.laser(1)
		time.sleep(3) #Let the laser and LDRs warm up
		rval=[[(0,0)]*int(255/step)]*int(510/step) #Generate a matrix that is equal to the size of the scan, each pixel being represented by the tuple (Reference, Measurement)
		for xval in range(0,255,step):
			for yval in range(-255,255,step): #For each pixel
				self.pos(xval, yval, z) #Get there
				rval[xval][yval]=self.ldr(sleepval=accuracy) #record the pixel
				#repeat for the next pixel
		self.laser(0)
		return rval #return the picture
	def close(self):
		self.test()
		self.ser.close()
