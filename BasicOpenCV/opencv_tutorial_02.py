# import the necessary packages
import argparse 
import imutils
import cv2 
import matplotlib.pyplot as plt 

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, 
    help="path to input image")
args = vars(ap.parse_args())

# load the input image (whose path was supplied via command line 
# argument) and display the image to our screen
image = cv2.imread(args["image"])
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap="gray")
# plt.show()

# convert the image to grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# plt.imshow(gray, cmap="gray")
# plt.show()
# cv2.waitKey(0)

# applying edge detection we can find the outlines of objects in 
# images
edged = cv2.Canny(gray, 30, 150)
# plt.imshow(edged, cmap="gray")
# plt.show()
# cv2.waitKey(0)

# threshold the image by setting all pixel values less than 225 
# to 255 (white; foreground) and all pixel values >= 225 to 255
# (black; background), thereby segmenting the image 
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
# plt.imshow(thresh, cmap="gray")
# plt.show()
# cv2.waitKey(0)

# find contours (i.e., outlines) of the foreground objects in the 
# thresholded image
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, 
#     cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# output = image.copy()

# loop over the contours
# for c in cnts:
    # draw each contour on the output image with a 3px thick purple
    # outline, the display the output contours one at a time
    # cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
    # plt.imshow(output, cmap="gray")
    # plt.show()
    # cv2.waitKey(0)

# draw the total number of contours found in purple 
# text = "I found {} objects!".format(len(cnts))
# cv2.putText(output, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
#     (240, 0, 159), 2)
# plt.imshow(output, cmap="gray")
# plt.show()
# cv2.waitKey(0)

# we apply erosions to reduce the size of foreground objects 
mask = thresh.copy()
# mask = cv2.erode(mask, None, iterations=5)
# plt.imshow(mask, cmap="gray")
# plt.show()
# cv2.waitKey(0)


# similarly, dilations can increase the size of the ground objects
mask = cv2.dilate(mask, None, iterations=5)
# plt.imshow(mask, cmap="gray")
# plt.show()
# cv2.waitKey(0)

# a typical operation we may want to apply is to take our mask and
# apply a bitwise AND to our input image, keeping only the masked
# regions

output = cv2.bitwise_and(image, image, mask=mask)
plt.imshow(output, cmap="gray")
plt.show()
cv2.waitKey(0)