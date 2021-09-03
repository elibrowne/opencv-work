import numpy as np
import cv2

# Create a rectangle
rectangle = np.zeros((300, 300), dtype = "uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)

# Create a circle
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)
cv2.waitKey(0)

# Use the circle and rectangle in bitwise operations #

# AND operator - where both shapes are
bitwiseAND = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND Operator", bitwiseAND)
cv2.waitKey(0)

# OR operator - where at least one shape is
bitwiseOR = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR Operator", bitwiseOR)
cv2.waitKey(0)

# XOR operator - where only one shape is
bitwiseXOR = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR Operator", bitwiseXOR)
cv2.waitKey(0)

# NOT operator - invert the pixels in one image (no comparisons)
bitwiseNOT = cv2.bitwise_not(circle)
cv2.imshow("NOT Operator", bitwiseNOT)
cv2.waitKey(0)