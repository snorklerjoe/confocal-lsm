import cv2
import numpy as np
import sys
import time


cam = cv2.VideoCapture(0)

def crop_image(img,tol=70):
    # img is image data
    # tol  is tolerance
    try:
        mask = img>tol
        return img[np.ix_(mask.any(1),mask.any(0))]
    except:
        return img

def brightness(img):
    num=0
    cnt=0
    thresh=img.mean()+10
    for line in img:
        for pixel in line:
            cnt+=1
            if pixel>thresh:
                num+=1
    return 2000*num/cnt
def rbrightness(img):
	buf=[]
	for i in range(2):
		buf+=[brightness(img)]
	return np.mean(buf)
def size(img):
	(a,b)=img.shape
	return a*b

if __name__=="__main__":
	while 1:
		ret, frame = cam.read()
		cv2.imwrite("./test.jpg", frame)
		#cv2.imshow("Original", frame)
		#cv2.waitKey(0)
		try:
			newimg=crop_image(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
			cv2.imshow("Cropped", newimg)
			cv2.waitKey(2)
			#cv2.imshow("Binary", newimg)
			#cv2.waitKey(0)
		except Exception as e:
			print(e)
		#cv2.waitKey(0)
		#(thresh, nimg) = cv2.threshold(newimg, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
		try:
			print("Size: %i, Brightness: %f" % (size(newimg), np.mean(np.mean(newimg))*10))
		except:
			print(" ")
