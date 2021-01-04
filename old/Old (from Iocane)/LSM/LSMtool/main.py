version="2.0.1"

from PyQt4 import QtGui, uic # Import the PyQt4 module we'll needimport sys # We need sys so that we can pass argv to QApplication
import sys # We need sys so that we can pass argv to QApplication
import window
from window import Ui_MainWindow
import cv2
import time
import numpy as np
from matplotlib import pyplot as plt
import serial
import keyboard
import os
import Tkinter as tk
from tkMessageBox import *

root = tk.Tk().withdraw()  # hide the root window

divnum=0
aerror=0
resval=0

K_A=0
K_Q=0

def keyboard_is_pressed(key):
    global K_A
    global K_Q
    if key=="n":
        return K_A
    if key=="q":
        return K_Q


#    os.system("sudo python simplekey.py '"+str(key)+"' > ./tmp.txt")
#    a=open("./tmp.txt", "r")
#    result=bool(a.read())
#    a.close()
#    return result
#while not keyboard.is_pressed(" "):
#    time.sleep(1)

try:
    trinket = serial.Serial('/dev/ttyACM0',baudrate=9600)
    trinket.write("import main\n\r")
    trinket.write("import LSMtools\n\r")
    trinket.write("import time\n\r")
except:
    print "Error:"
    print "Cannot connect to LSM!!"
    print "\n\nTERMINATING..."
    exit()

def pad_array(array):
    global resval
    #array=array+([0]*10)
    size=int((200/resval))**2
    if len(array)>size:
        rval=array[0:size]
    else:
        rval=array+([0]*(size-len(array)))
    return rval
def customsend(data, bar):
    trinket.write("\n\r")
    trinket.write("\n\r")
    trinket.write("\n\r")
    bar.setValue(15)
    time.sleep(1)
    print "Sending "+str(data)+" command..."
    bar.setValue(35)
    time.sleep(2)
    bar.setValue(60)
    trinket.write(str(data)+"\n\r")
    bar.setValue(70)
    time.sleep(1)
    bar.setValue(80)
    time.sleep(1)
    bar.setValue(100)
def scan(resval, aerror, bar):
    #global aerror
    trinket.write("\n\r")
    trinket.write("\n\r")
    trinket.write("\n\r")
    bar.setValue(15)
    time.sleep(1)
    print "Sending SCAN command..."
    bar.setValue(35)
    time.sleep(2)
    bar.setValue(60)
    trinket.write("main.simplescan("+str(resval)+", "+str(float(aerror)/float(100))+")\n\r")
    bar.setValue(70)
    time.sleep(1)
    bar.setValue(80)
    #print "Serial Buffer:"
    #print trinket.read(100)
    print "Sent:\n"+str("main.simplescan("+str(resval)+", "+str(float(aerror)/float(100))+")\n\r")+"\n"
    print "Scanning..."
    bar.setValue(90)
def makeimage(out, template):
    global resval
    shape=int((200/resval))
    print out
    #try:
    #size=input("To compute a matrix, please enter a resolution for the microscope image:  ")
    #print size
    print "Image:"
    print np.array(np.array(out).reshape((shape,shape)))
    return np.array(np.array(out).reshape((shape,shape)))
    #except ValueError:
    #    print "ValueError.\nThe format was incorrect.\n\nScan Display Failed.\nTERMINATING..."
    #    exit()
    #except:
    #    print "Unknown Error.\n\nScan Display Failed.\nTERMINATING..."
    #    exit()
def brightness(img):
    num=0
    for line in img:
        for pixel in line:
            if pixel>0:
                num+=1
    return num
def crop_image(img,tol=70):
    # img is image data
    # tol  is tolerance
    try:
        mask = img>tol
        return img[np.ix_(mask.any(1),mask.any(0))]
    except:
        return img
def newpixel(event,x,y,flags,param):
    global numpics
    if event == cv2.EVENT_LBUTTONDBLCLK:
        try:
            print "Pixel "+str(numpix)+", Value "+str(brightness(nimg))
            output[numpix]=(brightness(nimg))
            numpix+=1
        except:
            print "Pixel "+str(numpix)+", Value "+str(brightness(nimg))
            output[numpix]=(brightness(nimg))
            numpix+=1

class ExampleApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        #QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined
        self.scan.clicked.connect(self.send)
        self.send_cmd.clicked.connect(self.sendcmd)
        self.pushButton.clicked.connect(self.refreshdata)
        self.actionAbout.triggered.connect(self.info)
    def keyPressEvent(self, event):
        global K_A
        global K_Q
        key = event.key()
        print key
        K_A=(key==78)
        K_Q=(key==81)
        print K_A
        print K_Q
    def refreshdata(self):
        #self.Output.clear()
        self.Output.appendPlainText(str(trinket.read(trinket.in_waiting)))
    def info(self):
        global version
        showinfo(title="About LSMtool", message="You are using LSMtool version "+str(version)+".\nLSMtool is a program made specifically for DragonFly, my homemade Laser Scanning microscope,\nor LSM.\n\nThank You!")
    def sendcmd(self):
        if self.lon.isChecked():
            customsend("l=LSMtools.Laser()", self.sendbar)
            customsend("l.laser_on()", self.sendbar)
        if self.loff.isChecked():
            customsend("l.laser_off()", self.sendbar)
            customsend("l.laser_disable()", self.sendbar)
        if self.other.isChecked():
            customsend(self.other_cmd.text(), self.sendbar)
    def send(self):
        global divnum
        global aerror
        global resval
        global K_A
        global K_Q
        self.sendbar.setValue(10)
        numpix=0
        output=[]
        print("Scan!")
        print "Res:   ",self.res.text()
        print "Pause: ",self.time.text()
        print "sense: ",self.sense.text()
        resval=int(self.res.text())
        divnum=int(self.sense.text())
        aerror=int(self.time.text())
        cap = cv2.VideoCapture(1)
        #self.sendbar.setValue(15)
        image = cv2.imread("normal.jpg")
        scan(resval, aerror, self.sendbar)
        self.sendbar.setValue(100)
        progress=0
        while(True):
            #print keyboard_is_pressed("n")
            # Capture frame-by-frame
            ret, frame = cap.read()
            cv2.waitKey(1)
            newimg=crop_image(cv2.cvtColor(cv2.subtract(frame,image), cv2.COLOR_BGR2GRAY))
            (thresh, nimg) = cv2.threshold(newimg, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            #newimg = cv2.resize(cv2.resize(newimg, (1, 1)), (50,50))
            # Display the resulting frame
            try:
                #cv2.imshow('frame',nimg)
                #cv2.setMouseCallback('frame',newpixel)
                #print "LASER!"
	            #print "Brightness: "+str(brightness(nimg))
                if (K_A):
                    numpix+=1
                    print "Pixel "+str(numpix)+", Value "+str(brightness(nimg)),str(brightness(nimg)/divnum)
                    output+=[int(brightness(nimg)/divnum)]
                    #K_A=0
                    while K_A != 0:
                            time.sleep(0.1)
                    #time.sleep((aerror/130)-10)
                    K_A=0
                    progress+=float(float(100)/float(int((200/resval))**float(2)))
                    self.scanbar.setValue(progress)
            except:
                pass
                #print "NO LASER!"
            if (K_Q) or len(output)==(int((200/resval))**2):
                if len(output)==(int((200/resval))**2):
                    self.scanbar.setValue(100)
                print nimg
                plt.imshow(makeimage(output, []))
                plt.show()
                #histr = cv2.calcHist([(makeimage(output, ['hi']))],[0],None,[256],[0,256])
                #plt.plot(histr)
                #plt.show()
                #while not (cv2.waitKey(1) & 0xFF == ord('q')):
                #    cv2.imshow('Final Image:',(cv2.resize((makeimage((output), ([['p','p','p','p'],['p','p','p','p'],['p','p','p','p'],['p','p','p','p']]))), (100, 100))))
                print np.array(makeimage(pad_array(output), ([['p','p','p','p'],['p','p','p','p'],['p','p','p','p'],['p','p','p','p']])))
                img=np.array(makeimage((output), ([['p','p','p','p'],['p','p','p','p'],['p','p','p','p'],['p','p','p','p']])))
                ascii=[range(int((200/resval))+1)]*int((200/resval)+1)
                print "ASCII-ART Template:"
                print np.array(ascii)
                i=0
                print "ASCII-ART representation of the image:"
                for line in img:
                    i2=0
                    for pix in line:
                        ascii[i][i2]=str('      ...\'\'\'```^^^""",,,:::;;;IIIlll!!!iii>>><<<~~~+++___---???]]][[[}}}{{{111)))(((|||\\\\\\///tttfffjjjrrrxxxnnnuuuvvvccczzzXXXYYYUUUJJJCCCLLLQQQ000OOOZZZmmmwwwqqqpppdddbbbkkkhhhaaaooo***###MMMWWW&&&888%%%BBB@@@#############################################')[pix]
                        #print pix
                        i2+=1
                    i+=1
                print np.array(ascii)
                #cv2.imshow('Final Picuture', np.array(makeimage((output), ([['p','p','p','p'],['p','p','p','p'],['p','p','p','p'],['p','p','p','p']]))))
                time.sleep(5)
                break
    #    
        # When everything is done, release the capture
        cap.release()
        cv2.destroyAllWindows()

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
