#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#This script will find the brightness of a laser in transmission-mode, and allow for focus adjustment (eventually maybe)

import cv2
import numpy as np
import sys
import time


cam = cv2.VideoCapture(0)


cam.set(3,160)
cam.set(4,120)

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
    if np.sum(img.shape)<1:
        return 0
    else:
        return brightness(img)
def size(img):
    (a,b)=img.shape
    return a*b
def crop_image(img,tol=25):
    # img is image data
    # tol  is tolerance
    try:
        mask = img>tol
        return img[np.ix_(mask.any(1),mask.any(0))]
    except:
        return img
def pic():
    ret, frame = cam.read()
    newimg=crop_image(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    return newimg
def warmup():
    for i in range(10):
        ret, frame = cam.read()
def get_cropped():
	return crop_image(cv2.cvtColor(cam.read()[1], cv2.COLOR_BGR2GRAY))
def read(ssize=False):
    #return cv2.cvtColor(cv2.resize(cam.read()[1], (1,1), interpolation = cv2.INTER_AREA), cv2.COLOR_BGR2GRAY)[0][0]

	#newimg = get_cropped()
	#brightness = np.mean(np.mean(newimg))*10
	#return size(newimg)/40 + brightness

	_, image = cam.read()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gaussian = cv2.GaussianBlur(gray, (299, 299), 0)
	return gaussian.mean().mean()
def cheese(): #Display a window streaming from the camera
    mustloop=True
    loop=True
    while mustloop or loop:
        ret, frame = cam.read()
        loop=(cv2.waitKey(1)!=27)
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        try:
            cv2.imshow("Image", frame)
            mustloop=False
            print("Mean Brightness: "+str(np.mean(np.mean(frame))))
        except:
            mustloop=True
            time.sleep(0.25)
    cv2.destroyAllWindows()
if __name__=="__main__":
#	cheese()
    while 1:
#		#ret, frame = cam.read()
#		#cv2.imshow("Original", frame)
#		#cv2.waitKey(0)
#		#try:
#		#newimg=crop_image(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
#		#try:
#		#	cv2.imshow("Cropped", newimg)
#		#	cv2.waitKey(1)
#		#except:
#		#	print("It's dark.")
#		#except:
#		#	print("Couldn't display.")
#		#cv2.waitKey(0)
#		#(thresh, nimg) = cv2.threshold(newimg, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#		#cv2.imshow("Binary", nimg)
#		#cv2.waitKey(0)
#		#print("Size:       "+str(read(True)))
        print("Size:       "+str(read()))
