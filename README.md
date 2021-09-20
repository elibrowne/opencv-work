# OpenCV Work - Eli Browne
*First quarter work done in Advanced Honors Computer Science with OpenCV*

## OpenCV Project 

The content of this project can be found in the `project` folder. Images used to test the final project are also present in the `project/images` folder. The images were picked to have different color balances, meaning that the code will have to determine which color is least present.

#### What does the project do? 
1. The project opens an image specified by the user (ch. 3)
2. The project draws a histogram of the RGB colors and uses it to calculate the least common color (ch. 7)
3. Using the least common color, the project draws random shapes on the image (ch. 5)
4. Using thresholding, edge detection, color spaces + masking, and contours, the project identifies, labels, and counts the obstructions on the image (chs. 6, 9-11)
5. Using inpainting methods built into OpenCV, the program attempts to "repair" the image (not from book)

That should be representative of more than 6 chapters from the book. All the images were new (not used earlier). You should be able to use the space bar to navigate through the program, as I've just been using `waitKey(0)` to pause - after the histogram is shown, you may have to close it before refocusing on the OpenCV window and pressing space. 

## OpenCV Practice

I went through the book and did all of the example code. I tried to comment where I didn't understand to make sure I was learning the content.