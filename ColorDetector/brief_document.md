## cv2.bitwise_and:
cv2.bitwise_and(\<image1\>, \<image2\>, \<mask\>)  

A mask is the same size as our image, but has only two pixel
values, 0 and 255 -- pixels with a value of 0 (background) are
ignored in the original image while mask pixels with a value of
255 (foreground) are allowed to be kept.  

* mask = 0 => output = 0  
* mask > 0 => output = image1 & image2  