# import the necessary packages
from imutils import build_montages
from imutils import paths
import argparse
import random
import cv2
import matplotlib.pyplot as plt 

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to input directory of images")
ap.add_argument("-s", "--sample", type=int, default=21,
    help="# of images to sample")
args = vars(ap.parse_args())

# grab the paths to the image, then randomly select a sample of 
# them 
imagePaths = list(paths.list_images(args["image"]))
random.shuffle(imagePaths)
imagePaths = imagePaths[:args["sample"]]

# initialize the list of images
images = []

# loop over the list of image paths
for imagePath in imagePaths:
    # load the image and update the list of images
    image = cv2.imread(imagePath)
    images.append(image)

# construct the montage for the images
montages = build_montages(images, (128, 196), (7, 3))

# loop over the montages and display each of them
for montage in montages:
    plt.imshow(cv2.cvtColor(montage, cv2.COLOR_BGR2RGB), cmap="gray")
    plt.show()
    