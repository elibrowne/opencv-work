import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

croppedImage = image[100:400, 100:400]
cv2.imshow("300 by 300 Snippet", croppedImage)
cv2.waitKey(0)

croppedImage = image[325:625, 475:775] # y-axis values first, then x-axis
cv2.imshow("300 by 300 Snippet", croppedImage)
cv2.waitKey(0)

# Cropping is also quite simple and doesn't require an imutils method.