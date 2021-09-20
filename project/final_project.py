from matplotlib import pyplot
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

# Creating a histogram for RGB colors - making the histogram
channels = cv2.split(image) # splits into B G and R channels
colors = ("b", "g", "r")
pyplot.figure() # make a figure to add to
pyplot.title("Color Prominence in Selected Image") 
pyplot.xlabel("Bins")
pyplot.ylabel("Num. Pixels")

# Loop over the channels and respective colors to make histogram with three lines
for (channel, color) in zip(channels, colors):
	# For each color, make a new histogram with said color and add it to the plot
	histogram = cv2.calcHist([channel], [0], None, [256], [0, 256]) # just like grayscale b/c only one color is shown
	pyplot.plot(histogram, color = color) # set the color of the histogram to match the color it reflects
	pyplot.xlim([0, 256]) # set the bounds as RGB

pyplot.show() # show the combined RGB histogram
cv2.waitKey(0) 