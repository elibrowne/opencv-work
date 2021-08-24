from __future__ import print_function
import argparse 
import cv2

ap = argparse.ArgumentParser() 
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# 
(b, g, r) = image[0, 0] # get the blue, green, and red values from the pixel <0, 0>
print("Top left pixel - r: {}, g: {}, b: {}".format(r, g, b)) # print out the color

image [0, 0] = (0, 0, 255) # set top left pixel to red (reverse order BRG)
(b, g, r) = image[0, 0] # see the color change reflected in the variables
print("Top left pixel - r: {}, g: {}, b: {}".format(r, g, b))

# At this point, the changes to the image haven't been saved, so you can re-run the
# script over and over without the image actually changing.

corner = image[0:100, 0:100] # range of the top 100x100 corner
cv2.imshow("Corner", corner)

image[0:100, 1:100] = (255, 0, 0) # make the top corner blue

cv2.imshow("Updated", image) # here, the photo is changed on display
cv2.waitKey(0)

