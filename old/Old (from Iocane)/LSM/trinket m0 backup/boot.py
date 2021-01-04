import time
import sys
try:
	print("Testing LSMtools library:")
	print("	Importing LSMtools.py...")
	import LSMtools
	print("	Trying Laser class...")
	l=LSMtools.Laser()
	l.laser_on()
	time.sleep(1)
	l.laser_off()
	l.laser_disable()
	print("	Trying Movement class...")
	m=LSMtools.Move()
	time.sleep(5)
	m.move(100,100)
	m.home()
	time.sleep(5)
	LSMtools.scan(50, 0.5)
	print("	Hardware and LSMtools are OK!")
except:
	print("FAILED: LSMtools malfunction!")

print("")
print("")
print("Laser Scanning Microscope Controller up and running!")
print("Open the serial REPL and type:")
print("")
print(">>> import main")
print(">>> main.go()")
print("")
