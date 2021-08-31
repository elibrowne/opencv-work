import numpy as np
import argparse
import imutils # a library that we're going to write ourselves
import cv2 

# Argument parser for the command line
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(parser.parse_args())

# Display the original image (from load, display, save)
image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# Transform the image
# The first row of the translation matrix is the [1 = rows, 0 = columns, 25 pixels translation], the second one goes to columns
translationMatrix = np.float32([[1, 0, 25], [0, 1, 50]]) 
shifted = cv2.warpAffine(image, translationMatrix, (image.shape[1], image.shape[0]))
cv2.imshow("Image shifted 25 down and 50 right", shifted)
cv2.waitKey(0)

translationMatrix = np.float32([[1, 0, -25], [0, 1, -50]]) # reverse of the other matrix
shiftedAgain = cv2.warpAffine(image, translationMatrix, (image.shape[1], image.shape[0]))
cv2.imshow("Image brought back to original position", shiftedAgain)
cv2.waitKey(0)

# Use our new imutils package
shiftedImage = imutils.translate(image, 0, 100)
cv2.imshow("Shifted down with imutils", shiftedImage)
cv2.waitKey(0)