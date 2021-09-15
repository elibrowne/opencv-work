# Otsu's method - assume that there are two peaks and separate them optimally

from __future__ import print_function 
import numpy as np
import argparse
import mahotas 
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

# T is the value at which the threshold should be established
T = mahotas.thresholding.otsu(blurred)
print("Otsu's Method: {}".format(T))

# Using T as a value to split the peaks in half, we can color the image 
threshold = image.copy()
threshold[threshold > T] = 255 # set all values not meeting the threshold to white
threshold[threshold < 255] = 0 # all remaining pixels are black
threshold = cv2.bitwise_not(threshold) # mask with a not gate
cv2.imshow("Otsu Method", threshold)
cv2.waitKey(0)

# One can also use the Riddler-Calvard method
T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard Method: {}".format(T))
threshold = image.copy()
threshold[threshold > T] = 255
threshold[threshold < 255] = 0 # recolor to white then black
threshold = cv2.bitwise_not(threshold) # not gate
cv2.imshow("Riddler-Calvard Method", threshold)
cv2.waitKey(0)