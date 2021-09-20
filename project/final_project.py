import numpy as np
import argparse
import cv2

##  Plan  ##
# Open image (3)
# Manipulate colors and display histogram (6, 7)
# Draw a random amount of small shapes on the image (5)
# Detect them and count them (and fill them in? inpainting) (9, 10, 11)

# Opening processes - create ArgumentParser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

# Opening processes - save and display the original image
image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0) 
