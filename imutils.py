import numpy as np
import cv2

# Make the process of translating much quicker
def translate(image, x, y):
	translationMatrix = np.float32([[1, 0, x], [0, 1, y]])
	shiftedImage = cv2.warpAffine(image, translationMatrix, (image.shape[1], image.shape[0]))
	# Return the resulting image with its shift
	return shiftedImage