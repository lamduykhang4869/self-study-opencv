# Note:
Command line argument flags have a ‘-‘ (dash) in them such as --features-db, it’s a little bit confusing and a bit of a nuissance that when grabbing the value contained by the argument, you need to use a ‘_’ (underscore).  
Example:  
\# construct the argument parser and parse the arguments  
ap = argparse.ArgumentParser()  
ap.add_argument("-f", "--features-db", required=True, help="Path to the features database")  
args = vars(ap.parse_args())  
\# load the codebook and open the features database  
featuresDB = h5py.File(args["features_db"], mode="r")  

# cv2.GaussianBlur:
cv2.GaussianBlur(\<image\>, \<kernel_size\>, \<standard_deviation\>)  

We should specify the width and height of the kernel which should be positive and odd. We also should specify the standard deviation in the X and Y directions, sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is taken as the same as sigmaX. If both are given as zeros, they are calculated from the kernel size. Gaussian blurring is highly effective in removing Gaussian noise from an image.  

# cv2.threshold:
cv2.threshold (\<grayscale_image\>, \<threshold_value\>, \<maximum_value\>, \<threshold_type\>)

The first argument is the source image, which should be a grayscale image. The second argument is the threshold value which is used to classify the pixel values. The third argument is the maximum value which is assigned to pixel values exceeding the threshold. OpenCV provides different types of thresholding which is given by the fourth parameter of the function. Basic thresholding as described above is done by using the type cv.THRESH_BINARY.  
The method returns two outputs. The first is the threshold that was used and the second output is the thresholded image.

# cv2.findContours:
cv2.findContours(\<image\>, \<contour_retrieval_mode\>, \<contour_approximation_method\>)  

There are three arguments in cv.findContours() function, first one is source image, second is contour retrieval mode, third is contour approximation method. And it outputs a modified image, the contours and hierarchy. contours is a Python list of all the contours in the image. Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object. 


# imutils.grab_contours:
imutils.grab_contours(\<findContours_output\>: cnts)

The function returns counters (contours) in the output of method findContours, which does not distinguish between opencv2 or opencv3. OpenCV2 return cnts[0], OpenCV3 return cnts[1].  


# cv2.drawContours:
cv2.drawContour(\<image\>, \<contours\>, \<contours_index\>, \<color\>, \<thickness\>)  

To draw the contours, cv.drawContours function is used. It can also be used to draw any shape provided you have its boundary points. Its first argument is source image, second argument is the contours which should be passed as a Python list, third argument is index of contours (useful when drawing individual contour. To draw all contours, pass -1) and remaining arguments are color, thickness etc.  

# cv2.putText:
cv2.putText(\<image\>, \<text\>, \<bottem_left_corner_coordinates\>, \<font\>, \<font_scale\>, \<color\>, \<thickness\>)  



