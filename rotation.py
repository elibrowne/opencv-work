import numpy as np
import argparse
import imutils # self made package
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

(height, width) = image.shape[:2] # only get the first two elements
centerOfImage = (width // 2, height // 2) # whole integer numbers for the center point

# Rotate the image by 45 degrees
rotationMatrix = cv2.getRotationMatrix2D(centerOfImage, 45, 1.0)
rotatedImage = cv2.warpAffine(image, rotationMatrix, (width, height))
cv2.imshow("Rotated by 45 degrees", rotatedImage)
cv2.waitKey(0)

# Rotate the other direction to 90 degrees
rotationMatrix = cv2.getRotationMatrix2D(centerOfImage, -90, 1.0)
rotatedImage = cv2.warpAffine(image, rotationMatrix, (width, height))
cv2.imshow("Rotated by -90 degrees", rotatedImage)
cv2.waitKey(0)

# Using the rotation method wrote in imutils.py
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 degrees", rotated)
cv2.waitKey(0)