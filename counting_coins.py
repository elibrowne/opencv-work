from __future__ import print_function 
import numpy as np
import argparse 
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Blurred Grayscale Image", blurred)
cv2.waitKey(0)

edgedImage = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edges", edgedImage)
cv2.waitKey(0)

# Count the amount of curves in the image 
# This function is destructive so copy an image before using it
(cnts, _) = cv2.findContours(edgedImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("There are {} coins in this image!".format(len(cnts)))

coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2) # draw green curves over the coins
cv2.drawContours(coins, cnts, 0, (0, 0, 255), 2) # redraw the first contour as red
cv2.drawContours(coins, cnts, 1, (255, 0, 0), 2) # redraw the second contour as blue
cv2.imshow("Coins", coins)
cv2.waitKey(0)

# Crop out coins
for (i, c) in enumerate(cnts):
	(x, y, w, h) = cv2.boundingRect(c) # create a rectangle around each coin
	
	print("Coin #{}".format(i + 1))
	coin = image[y:y + h, x:x + w] # cut out the image
	cv2.imshow("Cropped Coin", coin)

	mask = np.zeros(image.shape[:2], dtype = "uint8") # create a mask for the image
	((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
	cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
	mask = mask[y:y + h, x:x + w]
	cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask)) # mask over the coins
	cv2.waitKey(0)