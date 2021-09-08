import numpy as np
import argparse
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype = "uint8") # create an array of zeros to serve as the mask
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2) # compute the center X and Y of the image
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1) # make a rectangle that's 150x150
cv2.imshow("Mask", mask)
cv2.waitKey(0)

maskedImage = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Masked Image", maskedImage)
cv2.waitKey(0)

circleMask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.circle(circleMask, (cX, cY), 300, 255, -1) # 300 radius of mask
masked = cv2.bitwise_and(image, image, mask = circleMask)
cv2.imshow("Circle Mask on Image", masked)
cv2.waitKey(0)