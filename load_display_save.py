from __future__ import print_function

import argparse # argument parser
import cv2 # openCV - problem with virtual env?

ap = argparse.ArgumentParser() # create argument parser
ap.add_argument("-i", "--image", required = True, help="point lobos.jpg")
args = vars(ap.parse_args())

image = cv2.imread(args["image"]) # returns an array "representing" the image

# Array structure - [width, height, channels]
print("width: {}".format(image.shape[1]))
print("height: {}".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

# The order of the array structure is reversed because the height is the number of rows and the width is the number of columns.

cv2.imshow("Point Lobos", image) # window name + image (which is set with the --image flag from 7)
cv2.waitKey(0) # pause the execution until a key is clicked (so it doesn't close immediately)

cv2.imwrite("newimage.jpg", image) # writes a new image, "newimage.jpg", in this folder