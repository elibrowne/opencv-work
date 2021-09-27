# OpenCV Work - Eli Browne
*First quarter work done in Advanced Honors Computer Science with OpenCV*

## OpenCV Project 

The content of this project can be found in the `project` folder. Images used to test the final project are also present in the `project/images` folder. The images were picked to have different color balances, meaning that the code will have to determine which color is least present.

#### What does the project do? 
1. The project opens an image specified by the user (ch. 3)
2. The project draws a histogram of the RGB colors and uses it to calculate the least common color (ch. 7)
3. Using the least common color, the project draws random shapes on the image (ch. 5 + understanding of 4)
4. Using thresholding, edge detection, color spaces + masking, and contours, the project identifies, labels, and counts the obstructions on the image (chs. 6, 9, 11)
5. Using inpainting methods built into OpenCV, the program attempts to "repair" the image (not from book - learned online)
6. Using callback methods, the program lets the user draw on the original image (not from book - learned online)
7. In the same process as (5), the lines are removed by inpainting and the result is shown

That should be representative of at least 6 chapters from the book. All the images were new (not used earlier). The program should theoretically work with any image, although some may present more challenges than others. The four included all work somewhat well. The only argparse argument is `--image``, which is described with `help`.

#### Notes on usage

 - When clicking through the project using the space bar, you will probably have to close out the histogram after viewing it. I've used `waitKey(0)` to pause frames, but unfortuately, the histogram seems to mess with it.
 - Images must be a "normal size." They have to be at least 60 pixels tall for the random placement of circles to work, and if they're way too large, the method to determine which colors are most prominent will cause an integer overflow exception.
 - Sometimes, the amount of contours will be counted as higher than the amount of drawn shapes. This is caused by small parts of the image being the least prominent color. An example can be found in `waterfall.jpg`, where small red dots in the forest are detected and included in the mask, or on `sandstone.jpg`, which has a lot of tiny blue dots on the branch. This doesn't have any super significant implications for the final image as they're both very small and will be inpainted the same as the drawn on circles. 
 - You *must* use the spacebar to exit the drawing section of the program: another key will *not* work. This is because the while loop uses the ASCII for the spacebar to determine when it needs to close. 
 - There can be a small delay after you draw, especially if you draw a big shape or a lot of shapes! If you press space twice, it may delay and immediately close out the program following the display of the final product. You may have to be patient with inpainting.

## OpenCV Practice

I went through the book and did all of the example code. I tried to comment where I didn't understand to make sure I was learning the content.