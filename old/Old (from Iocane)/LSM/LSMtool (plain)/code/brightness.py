import cv2
import time
import numpy as np
from matplotlib import pyplot as plt
import serial

try:
    print "LSM tool 0.1"
    print ""
    print "Please enter a number to scale each pixel by."
    print "It should probably be around 10-45, a higher number resulting in lower sensitivity."
    divnum=input(">>> ")
    print ""
    print "Next, please enter the number you want for the simplescan resolution parameter."
    print "A bigger number means a lower resolution, the maximum being 100."
    resval=input(">>> ")
    print ""
    print "Finally, please type the allowable error as a percent."
    print "A bigger value means a longer scan, but the recommended value is about 50."
    aerror=input(">>> ")
except:
    print "You entered something incorrectly."
    print "Scan FAILED."
    print "TERMINATING..."
    exit()

numpix=0
output=[]

try:
    trinket = serial.Serial('/dev/ttyACM0',baudrate=9600)
except:
    print "Error:"
    print "Cannot connect to LSM!!"
    print "\n\nTERMINATING..."
    exit()


def pad_array(array):
    global resval
    size=int((200/resval))**2
    if len(array)>size:
        rval=array[0:size]
    else:
        rval=array+([0]*(size-len(array)))
    return rval
def scan(resval):
    global aerror
    trinket.write("\n\r")
    trinket.write("\n\r")
    trinket.write("\n\r")
    time.sleep(1)
    print "Sending SCAN command..."
    trinket.write("import main\n\r")
    time.sleep(2)
    trinket.write("main.simplescan("+str(resval)+", "+str(float(aerror)/float(100))+")\n\r")
    time.sleep(1)
    #print "Serial Buffer:"
    #print trinket.read(100)
    print "Sent:\n"+str("main.simplescan("+str(resval)+", "+str(float(aerror)/float(100))+")\n\r")+"\n"
    print "Scanning..."
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

def go():
    global numpix
    global output
    global resval
    global divnum
    cap = cv2.VideoCapture(0)
    image = cv2.imread("normal.jpg")
    scan(resval)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        newimg=crop_image(cv2.cvtColor(cv2.subtract(frame,image), cv2.COLOR_BGR2GRAY))
        (thresh, nimg) = cv2.threshold(newimg, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        #newimg = cv2.resize(cv2.resize(newimg, (1, 1)), (50,50))
        # Display the resulting frame
        try:
            cv2.imshow('frame',nimg)
            cv2.setMouseCallback('frame',newpixel)
            #print "LASER!"
	        #print "Brightness: "+str(brightness(nimg))
            if (cv2.waitKey(1) & 0xFF == ord('n')):
                numpix+=1
                print "Pixel "+str(numpix)+", Value "+str(brightness(nimg)),str(brightness(nimg)/divnum)
                output+=[int(brightness(nimg)/divnum)]
        except:
            pass
            #print "NO LASER!"
        if (cv2.waitKey(1) & 0xFF == ord('q')) or len(output)==(int((200/resval))**2):
            print nimg
            plt.imshow(makeimage(output, []))
            plt.show()
            #histr = cv2.calcHist([(makeimage(output, ['hi']))],[0],None,[256],[0,256])
            #plt.plot(histr)
            #plt.show()
            #while not (cv2.waitKey(1) & 0xFF == ord('q')):
            #    cv2.imshow('Final Image:',(cv2.resize((makeimage((output), ([['p','p','p','p'],['p','p','p','p'],['p','p','p','p'],['p','p','p','p']]))), (100, 100))))
            print np.array(makeimage((output), ([['p','p','p','p'],['p','p','p','p'],['p','p','p','p'],['p','p','p','p']])))
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
            cv2.imshow('Final Picuture', np.array(makeimage((output), ([['p','p','p','p'],['p','p','p','p'],['p','p','p','p'],['p','p','p','p']]))))
            time.sleep(5)
            break
#    
    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    go()
    trinket.close()
