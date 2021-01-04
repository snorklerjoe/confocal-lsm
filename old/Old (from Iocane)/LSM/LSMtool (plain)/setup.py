import os

print("Installing required libraries...")

try:
	import PyInstaller
	print("PyInstaller OK")
except:
	print("Installing Pyinstaller...")
	os.system("sudo pip install PyInstaller")

try:
	import matplotlib
except:
	os.system("python -mpip install -U pip")
	os.system("python -mpip install -U matplotlib")

try:
	import serial
except:
	os.system("pip install pyserial")

try:
	import cv2
except:
	os.system("sudo apt-get install python-opencv")

print("Compiling...")
os.system("pyinstaller ./code/brightness.py")
os.system("cp -r ./dist/brightness/* ./Final/")
os.system("sudo chmod 755 ./Final/*")
os.system("gcc -o ./run ./code/run.c")
os.system("sudo chmod 755 ./run")
