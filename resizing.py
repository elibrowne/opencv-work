import numpy as np
import argparse
import imutils # custom package
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

aspectRatio = 150.0 / image.shape[1] # create the aspect ratio for width 150 pixels
dimensions = (150, int(image.shape[0] * aspectRatio))

resizedImage = cv2.resize(image, dimensions, interpolation = cv2.INTER_AREA) # or INTER_LINEAR, INTER_NEAREST, INTER_CUBIC
cv2.imshow("Resized to 150px width", resizedImage)
cv2.waitKey(0)

aspectRatio = 100.0 / image.shape[0] # create the aspect ratio for height 100 pixels
dimensions = (int(image.shape[1] * aspectRatio), 100)

resizedImage = cv2.resize(image, dimensions, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resizedImage)
cv2.waitKey(0)

# Using imutils
resizedImage = imutils.resize(image, width = 300)
cv2.imshow("Resized with imutils", resizedImage)
cv2.waitKey(0)