import numpy as np
import cv2 

# Create an array of zeros, 300x300, for the canvas (with 3 channels for RGB)
canvas = np.zeros((300, 300, 3), dtype = "uint8") # data type = unsigned integer, 8 bit

green = (0, 255, 0) # create a variable to reference for the color green
cv2.line(canvas, (0, 0), (150, 150), green, 3) # draw a line from (0, 0) to (250, 250) that's green
cv2.imshow("Green Line on Canvas", canvas)
cv2.waitKey(0) # display and wait for the user to close

red = (0, 0, 255) # red variable (cv2 uses BGR so this is red!)
cv2.line(canvas, (150, 150), (300, 300), red, 3) # is there a reason for them appearing to have different thickness? I imagine it's the angle and approximations of how to draw thickness diagonally.
cv2.imshow("Green and Red Line on Canvas", canvas)
cv2.waitKey(0)

white = (255, 255, 255)
cv2.rectangle(canvas, (0, 0), (300, 300), white, 10) # create a white frame for the image
cv2.imshow("Red Line, Green Line, White Frame", canvas)
cv2.waitKey(0)

blue = (255, 0, 0) # again BGR
cv2.rectangle(canvas, (125, 125), (175, 175), blue, -1) # -1 thickness = filled in circle
cv2.imshow("Red + Green Line, Blue Rect. w/ Frame", canvas)
cv2.waitKey(0)

# Reset canvas to be blank
canvas = np.zeros((300, 300, 3), dtype = "uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2) # 150 and 150 in my case

for r in range(0, 120, 20):
	cv2.circle(canvas, (centerX, centerY), r, white)

# Draw a bullseye, each circle is 20 pixels apart from one another, 120 max radius
cv2.imshow("Bullseye!", canvas)
cv2.waitKey(0)

# Reset the canvas to be blank
canvas = np.zeros((300, 300, 3), dtype = "uint8")

for r in range (130, 30, -10):
	color = np.random.randint(50, high = 255, size = (3,)).tolist() # start at 50 for lighter colors
	center = np.random.randint(10, high = 290, size = (2,))

	cv2.circle(canvas, tuple(center), r, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)