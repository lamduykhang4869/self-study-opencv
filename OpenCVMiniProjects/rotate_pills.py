# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2
import matplotlib.pyplot as plt 

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the image file")
args = vars(ap.parse_args())

# load the image from disk, convert it to grayscale, blur it,
# and apply edge detection to reveal the outline of the pill
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(gray, 20, 200)
# plt.imshow(edged, cmap="gray")
# plt.show()

# find contours in the edge map 
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# ensure at least one contour was found 
if len(cnts) > 0:
    # grab the largest contour, then draw a mask for the pill
    c = max(cnts, key=cv2.contourArea)
    mask = np.zeros(gray.shape, dtype='uint8')
    cv2.drawContours(mask, [c], -1, 255, -1)

    # compute its bounding box of pill, then extract the ROI,
    # and apply the mask 
    (x, y, w, h) = cv2.boundingRect(c)
    imageROI = image[y:y+h, x:x+w]
    maskROI = mask[y:y+h,x:x+w]
    imageROI = cv2.bitwise_and(imageROI, imageROI, mask=maskROI)

plt.imshow(cv2.cvtColor(imageROI, cv2.COLOR_BGR2RGB), cmap="gray")
plt.show()