#Based on https://www.pyimagesearch.com/2014/09/29/finding-brightest-spot-image-using-python-opencv/

# import the necessary packages
import numpy as np
import argparse
import cv2

cam = cv2.VideoCapture(0)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
ap.add_argument("-r", "--radius", type = int,
	help = "radius of Gaussian blur; must be odd")
args = vars(ap.parse_args())
# load the image and convert it to grayscale
image = cv2.imread(args["image"])
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# perform a naive attempt to find the (x, y) coordinates of
# the area of the image with the largest intensity value
#(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
#cv2.circle(image, maxLoc, 5, (255, 0, 0), 2)
# display the results of the naive attempt
#cv2.imshow("Naive", image)


while True:
	_, image = cam.read()
	orig = image.copy()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# apply a Gaussian blur to the image then find the brightest
	# region
	gaussian = cv2.GaussianBlur(gray, (args["radius"], args["radius"]), 0)
	print("Intensity: %f" % gaussian.mean().mean())
	bilateral = cv2.bilateralFilter(gray, 9, 75, 75)
	median = cv2.medianBlur(gray, args["radius"])
	cv2.imshow("Blurred", gaussian)
	cv2.imshow("Bilateral", bilateral)
	cv2.imshow("Median", median)
	cv2.imshow("Original", orig)
	cv2.waitKey(1)
