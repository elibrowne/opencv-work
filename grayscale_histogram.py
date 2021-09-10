from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert the image from color to grayscale
cv2.imshow("Original Grayscale Image", image)
cv2.waitKey(0)

# Calculate the histogram - (image, num. channels = 0 for grayscale, no mask, size, ranges for RGB)
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure() # make a new figure
plt.title("Grayscale Image Histogram") # title the frame
plt.xlabel("Bins") # label the x axis "bins"
plt.ylabel("Num. Pixels") # label the y axis "num. pixels"
plt.plot(histogram) # plot the histogram on the figure
plt.xlim([0, 256]) # set the limits for x values so it doesn't graph unneeded values
plt.show() # show the plot

cv2.waitKey(0)