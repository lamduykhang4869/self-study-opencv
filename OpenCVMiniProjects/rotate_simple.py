# import the necessary packages 
import numpy as np
import argparse
import imutils
import cv2
import convenience
import matplotlib.pyplot as plt 

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to the image file")
args = vars(ap.parse_args())

# load the image from disk
image = cv2.imread(args["image"])

# loop over the rotation angles
for angle in np.arange(0, 360, 15):
    rotated = imutils.rotate(image, angle)
    plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB), cmap="gray")
    plt.show()

# loop over the rotation angles again this time ensuring 
# no part of the image is cut off 
for angle in np.arange(0, 360, 15):
    rotated = convenience.rotate_bound(image, angle)
    plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB), cmap="gray")
    plt.show()