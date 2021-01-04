import LSMtools
from adafruit_hid.keyboard import Keyboard
#from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import time


time.sleep(1)
kbd = Keyboard()
#layout = KeyboardLayoutUS(kbd)
m=LSMtools.Move()
l=LSMtools.Laser()


def simplescan(val, ttime):
	l.laser_on()
	i=0
	i2=0
	while i<200:
		i2=0
		while i2<200:
			m.move(i-100, i2-100)
			key = 0x11
			kbd.press(key)
			time.sleep(1)
			kbd.release_all()
			time.sleep(ttime)
			m.home()			
			i2+=val
		i+=val
	l.laser_off()
for times in range(5):
	l.laser_on()
	time.sleep(1/(times+1))
	l.laser_off()
	time.sleep(1/(times+1))
if __name__=="__main__":
	time.sleep(1)
	simplescan(10, 1)
