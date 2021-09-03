import argparse
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

flippedImage = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flippedImage)
cv2.waitKey(0)

flippedImage = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flippedImage)
cv2.waitKey(0)

flippedImage = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally and Vertically", flippedImage)
cv2.waitKey(0)

# Basically, 1 is a horizontal flip, 0 is vertical, and -1 is both. 
# No need for imutils here: this is pretty easy to do with the methods given.