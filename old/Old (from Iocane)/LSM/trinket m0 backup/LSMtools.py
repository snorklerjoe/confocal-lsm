 #import libraries:
import board
import digitalio
import pulseio
import time

#Variables/pins:

#Functions/classes:
class Laser: #class for turning on and off the laser diode.
	def __init__(self):
		self.laser = digitalio.DigitalInOut(board.D1)
		self.laser.direction = digitalio.Direction.OUTPUT
	def laser_on(self):
		self.laser.value=1
	def laser_off(self):
		self.laser.value=0
	def laser_disable(self):
		self.laser.value=0
		self.laser.deinit()

class Move:
	def __init__(self):
		self.p0=pulseio.PWMOut(board.D0)
		self.p0.deinit()
		self.p1=pulseio.PWMOut(board.D4)
		self.p1.deinit()
		self.p2=pulseio.PWMOut(board.D2)
		self.p2.deinit()
		self.p3=pulseio.PWMOut(board.D3)
		self.p3.deinit()
	def setpwm(self, pin, dutycycle):
		pin.duty_cycle=int(65535*(float(dutycycle)/float(100)))
	def off(self,pin):
		self.setpwm(pin, 0)
	def move(self,x, y):
		'''
		Sets pwm so that given the x and y coordinates (extremes: -100, 100), it will cause the coils to pull the object so that the laser is aimed at those coordinates. 
		'''
		if x>0:
			self.p0=pulseio.PWMOut(board.D0)
			#self.p1=pulseio.PWMOut(board.D4)
			self.p1.deinit()
			self.setpwm(self.p0, x)
		if x<0:
			self.p0.deinit()
			self.p1=pulseio.PWMOut(board.D4)
			self.setpwm(self.p1, -x)
		if x==0:
			self.p0.deinit()
			self.p1.deinit()
		if y>0:
			self.p2.deinit()
			self.p3=pulseio.PWMOut(board.D3)
			self.setpwm(self.p3, y)
		if y<0:
			self.p3.deinit()
			self.p2=pulseio.PWMOut(board.D2)
			self.setpwm(self.p2, -y)
		if y==0:
			self.p3.deinit()
			self.p2.deinit()
	def home(self):
		self.move(0,0)
def scan(val, ttime):
	i=0
	i2=0
	m=Move()
	while i<200:
		i2=0
		while i2<200:
			m.move(i-100, i2-100)
			time.sleep(ttime)
			m.home()
			i2+=val
		i+=val
	m.home()
