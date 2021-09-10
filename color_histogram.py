from __future__ import print_function 
from matplotlib import pyplot as plt
import numpy as np
import argparse 
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image) # no need to convert to grayscale because we're using color here

channels = cv2.split(image) # splits into B G and R channels
colors = ("b", "g", "r")
plt.figure() # make a figure
plt.title("Color Histogram") 
plt.xlabel("Bins")
plt.ylabel("Num. Pixels")

# Loop over the channels and respective colors to make histograms
for (channel, color) in zip(channels, colors):
	histogram = cv2.calcHist([channel], [0], None, [256], [0, 256]) # just like the grayscale b/c only one type of color is concerned
	plt.plot(histogram, color = color) # set the color of the histogram?
	plt.xlim([0, 256])

plt.show() # show the combined RGB histogram
cv2.waitKey(0)

# More histograms and 2D histograms

fig = plt.figure()

# Subplot of green and blue
ax = fig.add_subplot(131)
histogram = cv2.calcHist([channels[1], channels[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(histogram, interpolation = "nearest")
ax.set_title("Green and Blue - 2D Histogram")
plt.colorbar(p)

# Subplot of red and green
ax = fig.add_subplot(132)
histogram = cv2.calcHist([channels[1], channels[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(histogram, interpolation = "nearest")
ax.set_title("Green and Red - 2D Histogram")
plt.colorbar(p)

# Subplot of red and blue
ax = fig.add_subplot(133)
histogram = cv2.calcHist([channels[0], channels[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(histogram, interpolation = "nearest")
ax.set_title("Blue and Red - 2D Histogram")
plt.colorbar(p)

print("2D histogram shape: {}, with {} values".format(histogram.shape, histogram.flatten().shape[0]))

# 3d histogram - can't be visualized at this moment, but made in the same fashion

histogram = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
plt.show()

cv2.waitKey(0)