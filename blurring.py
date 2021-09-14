import numpy as np
import argparse
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

blurred = np.hstack([
	cv2.blur(image, (3, 3)),
	cv2.blur(image, (13, 13)),
	cv2.blur(image, (21, 21)) # refers to kernel size
])
cv2.imshow("Averaged Image", blurred)
cv2.waitKey(0)

# Gaussian Blur - more "weight" to the middle of the blurred area 

blurred = np.hstack([
	cv2.GaussianBlur(image, (3, 3), 0),
	cv2.GaussianBlur(image, (13, 13), 0),
	cv2.GaussianBlur(image, (21, 21), 0)
])
cv2.imshow("Gaussian Blurs", blurred)
cv2.waitKey(0)

# Median Blur - replace central pixel with median instead of average

blurred = np.hstack([
	cv2.medianBlur(image, 3),
	cv2.medianBlur(image, 13),
	cv2.medianBlur(image, 21)
])
cv2.imshow("Median Blurs", blurred)
cv2.waitKey(0)

# Bilateral Blur - maintain edges in the image

blurred = np.hstack([
	cv2.bilateralFilter(image, 5, 21, 21),
	cv2.bilateralFilter(image, 13, 31, 31),
	cv2.bilateralFilter(image, 21, 41, 41)
])
cv2.imshow("Bilateral Blur", blurred)
cv2.waitKey(0)