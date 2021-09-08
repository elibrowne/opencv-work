import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image) # split into three color channels

# Show the three channels indiviudally and then the combined result
cv2.imshow("Blue", B)
cv2.waitKey(0)
cv2.imshow("Green", G)
cv2.waitKey(0)
cv2.imshow("Red", R)
cv2.waitKey(0)

mergedImage = cv2.merge([B, G, R])
cv2.imshow("Merged Colors", mergedImage)
cv2.waitKey(0)

mergedImage = cv2.merge([G, B, R]) # if you change the order the colors will change too
cv2.imshow("Merged Colors", mergedImage)
cv2.waitKey(0)
cv2.destroyAllWindows() # why didn't we learn this earlier?