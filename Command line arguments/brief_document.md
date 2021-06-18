Command line argument flags have a ‘-‘ (dash) in them such as --features-db, it’s a little bit confusing and a bit of a nuissance that when grabbing the value contained by the argument, you need to use a ‘_’ (underscore).  
Example:  
\# construct the argument parser and parse the arguments  
ap = argparse.ArgumentParser()  
ap.add_argument("-f", "--features-db", required=True, help="Path to the features database")  
args = vars(ap.parse_args())  
\# load the codebook and open the features database  
featuresDB = h5py.File(args["features_db"], mode="r")  

# cv2.GaussianBlur:
cv2.GaussianBlur(<image>, <kernel_size>, <standard_deviation>)  

We should specify the width and height of the kernel which should be positive and odd. We also should specify the standard deviation in the X and Y directions, sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is taken as the same as sigmaX. If both are given as zeros, they are calculated from the kernel size. Gaussian blurring is highly effective in removing Gaussian noise from an image.  

# cv2.threshold:
cv2.threshold(<image>)