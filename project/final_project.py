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
cv2.imshow("Original image", image)
cv2.waitKey(0) 

# Creating a histogram for RGB colors - making the histogram
channels = cv2.split(image) # splits into B G and R channels
colors = ("b", "g", "r")
pyplot.figure() # make a figure to add to
pyplot.title("Color Prominence in Selected Image") 
pyplot.xlabel("Bins")
pyplot.ylabel("Num. Pixels")

# "Accumulator" to determine which color is the least prominent
# Because the color goes in B, G, R order "b" will always start as the smallest
leastProminentColor = "b"
leastProminentStrength = 2147483647 # largest possible integer

# Loop over the channels and respective colors to make histogram with three lines
for (channel, color) in zip(channels, colors):
	# For each color, make a new histogram with said color and add it to the plot
	histogram = cv2.calcHist([channel], [0], None, [256], [0, 256]) # just like grayscale b/c only one color is shown

	# Calculate how much one color shows up in the image by looping over the histogram
	totalColorWeight = 0
	for i in range(255):
		# Add the strength (0-255) multiplied by how many pixels have said strength
		# That way, the strongest colors (most high strength) will have higher values
		totalColorWeight += i * int(histogram[i])
	
	# If that color's strength is less than the least prominent strength...
	if leastProminentStrength > totalColorWeight:
		# ... it is the new least prominent color
		leastProminentColor = color
		# Update the least prominent color value so future checks work
		leastProminentStrength = totalColorWeight
	
	# Draw the plot
	pyplot.plot(histogram, color = color) # set the color of the histogram to match the color it reflects
	pyplot.xlim([0, 256]) # set the bounds as RGB

pyplot.show() # show the combined RGB histogram
cv2.waitKey(0) 

distinctColor = (0, 0, 0) # 'accumulator' for the color to draw in
if leastProminentColor == "r":
	distinctColor = (0, 0, 255) # red b/c BGR space
elif leastProminentColor == "g":
	distinctColor = (0, 255, 0)
else:
	distinctColor = (255, 0, 0) # if not red or green, then blue

# Draw a random amount circles on the screen in order to mess up the image
totalCircles = np.random.randint(5) + 10 # variable used to space circles
height, width, _ = image.shape # get dimensions of shape (channels aren't relevant here)

# Iterate to draw the circles
for i in range(totalCircles):
	if i != 0: # no circles on the edges (x = 0 or x = total width)
		cv2.circle(image, (int((i / totalCircles) * width), np.random.randint(height - 60) + 30), (np.random.randint(10) + 5) * 2, distinctColor, -1)

print("Total circles drawn: " + str(totalCircles - 1)) # check if the counting code detected the right amount of circles later
# Subtract one because the "first circle" at x = 0 is skipped

cv2.imshow("Image with drawn-on circles", image)
cv2.waitKey(0)

# Split into color channels to find the drawn-on shapes

(B, G, R) = cv2.split(image)
maskFinder = image # "accumulator" 
if leastProminentColor == "r":
	maskFinder = R
elif leastProminentColor == "g":
	maskFinder = G
else:
	maskFinder = B

# Display the image so the user sees how the colors are differentiated
cv2.imshow("Masked for color detection", maskFinder)
cv2.waitKey(0)

# Use thresholding to create a mask for what needs to be inpainted
# Binary thresh - all nonzero pixels are the ones that need to be fixed
T, shapeMask = cv2.threshold(maskFinder, 254, 255, cv2.THRESH_BINARY) # 254 - only the most pure colors
# This works because we drew our shapes with 255 r/g/b, meaning that they'll show up even with a 
# very narrow qualification for what counts as a color.
cv2.imshow("Mask for inpainting", shapeMask)
cv2.waitKey(0)

# Count however many circles there were and print to the console

# Count the amount of contours on a copy of the mask (this method is destructive)
contours, _ = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("There are " + str(len(contours)) + " shapes on this image.")
if len(contours) == totalCircles - 1: 
	print("CV2 counted an equal amount of circles as were drawn on by the code!")
elif len(contours) > totalCircles - 1:
	print("CV2 counted more contours than were drawn by it, meaning that there are little patches of every color on your image. Cool!")

# Display the contours
contoursFound = cv2.cvtColor(maskFinder, cv2.COLOR_GRAY2RGB) # convert to RGB so the circled contours show up as red
# Circle the contours and then display them on the grayscale image
cv2.drawContours(contoursFound, contours, -1, (0, 0, 255), 2)
cv2.imshow("Counted shapes", contoursFound)
cv2.waitKey(0)