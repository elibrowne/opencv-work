from __future__ import print_function
import numpy as np
import argparse
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# CV2 OPERATIONS with 8 bit unsigned integers (0 to 255)
print("Addition stops at 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("Subtraction stops at 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

# NUMPY OPERATIONS with 8 bit unsigned integers (0 to 255)
print("Wrap past 255 to 0: {}".format(np.uint8([200]) + np.uint8([100])))
print("Wrap past 0 to 255: {}".format(np.uint8([50]) - np.uint8([100])))

# ADDING TO IMAGE WITH CV2
M = np.ones(image.shape, dtype = "uint8") * 100 
addedImage = cv2.add(image, M)
cv2.imshow("Added with CV2", addedImage)
cv2.waitKey(0)

# SUBTRACTING FROM IMAGE WITH NP
M = np.ones(image.shape, dtype = "uint8") * 40
subtractedImage = cv2.subtract(image, M)
cv2.imshow("Subtracted with CV2", subtractedImage)
cv2.waitKey(0)