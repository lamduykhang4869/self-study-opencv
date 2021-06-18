import argparse
import cv2
import imutils

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
    help="path to input image")
ap.add_argument("-o", "--output", required=True,
    help="path to output image")
args = vars(ap.parse_args())

# load the input image from disk
image = cv2.imread(args["input"])

# convert the image to grayscale, blur it, and threshold it
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# extract contours from the image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL)