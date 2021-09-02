import numpy as np
import cv2

# Make the process of translating much quicker
def translate(image, x, y):	
	translationMatrix = np.float32([[1, 0, x], [0, 1, y]])
	shiftedImage = cv2.warpAffine(image, translationMatrix, (image.shape[1], image.shape[0]))
	# Return the resulting image with its shift
	return shiftedImage

# Make the process of rotating much quicker
def rotate(image, angle, center = None, scale = 1.0):
	(height, width) = image.shape[:2]

	if center is None: # set the center as the center if the user doesn't provide one
		center = (width // 2, height // 2) 

	rotationMatrix = cv2.getRotationMatrix2D(center, angle, scale)
	rotated = cv2.warpAffine(image, rotationMatrix, (width, height))

	return rotated