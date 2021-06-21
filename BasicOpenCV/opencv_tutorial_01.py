# import the necessary packages 
import imutils 
import cv2 
import matplotlib.pyplot as plt

# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)

image = cv2.cvtColor(cv2.imread('jp.jpg'), cv2.COLOR_BGR2RGB)
# rotated = imutils.rotate(image, 90, ) 
(h, w, d) = image.shape 
print("width={}, height={}, depth={}".format(w, h, d))

# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
# cv2.imshow("Image", rotated)
# cv2.imwrite('jp.jpg', rotated)
# rotated = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
# plt.imshow(rotated, cmap="gray")
# plt.show()
# print(rotated.shape)
# cv2.waitKey(0)

# extract a 100x100 pixel square ROI (Region of Interest) from the 
# input image starting at x=320,y=60 at ending at x=420,160
# roi = image[60:160,320:420]
# plt.imshow(roi, cmap="gray")
# plt.show()
# cv2.waitKey(0)

# resize the image to 200x200px, ignoring aspect ratio
# resized = cv2.resize(image, (200, 200))
# plt.imshow(resized, cmap="gray")
# plt.show()
# cv2.waitKey(0)

# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
# r = 300.0 / w
# dim = (300, int(h * r))
# resized = cv2.resize(image, dim)
# plt.imshow(resized, cmap="gray")
# plt.show()
# cv2.waitKey(0)

# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead
# resized = imutils.resize(image, width=300)
# plt.imshow(resized, cmap="gray")
# plt.show()
# cv2.waitKey(0)


# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
# center = (w // 2,  h // 2)
# M = cv2.getRotationMatrix2D(center, -45, 1.0)   # center, angle, scale
# rotated = cv2.warpAffine(image, M, (w, h ))

# rotation can also be easily accomplished via imutils with less code
# rotated = imutils.rotate(image, -45)

# OpenCV doesn't "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convenience function to help
# us out
# rotated = imutils.rotate_bound(image, 45)
# plt.imshow(rotated, cmap="gray")
# plt.show()
# cv2.waitKey(0)

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
# blurred = cv2.GaussianBlur(image, (11, 11), 0)
# plt.imshow(blurred, cmap="gray")
# plt.show()
# cv2.waitKey(0)

# draw a 2px thick red rectangle surrounding the face
output = image.copy()
# Since we are using OpenCV’s functions rather than NumPy operations we can supply our coordinates in (x, y)
# order rather than (y, x) since we are not manipulating or accessing the NumPy array directly — 
# OpenCV is taking care of that for us.
# cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
# plt.imshow(output, cmap="gray")
# plt.show()
# cv2.waitKey(0)



# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
# output = image.copy()
# cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
# plt.imshow(output, cmap="gray")
# plt.show()
# cv2.waitKey(0)

# draw green text on the image
output = image.copy()
cv2.putText(output, "OpenCV + Jurassic Park!!!", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
plt.imshow(output, cmap="gray")
plt.show()
cv2.waitKey(0)