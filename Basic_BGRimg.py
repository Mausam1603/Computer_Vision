import numpy as np
import cv2
#from google.colab.patches import cv2_imshow #Import the function from the patches module

#Create a blue rectangle image using a numpy array     
image = np.zeros((300, 400, 3), dtype = np.uint8)   #The shape (300, 400, 3) indicates that the image has a height of 300 pixels, a width of 400 pixels, and 3 color channels (for RGB).
imageb = image.copy()                               #dtype=np.uint8 means the data type of the array elements is 8-bit unsigned integers, which is standard for image data (values range from 0 to 255).
imager = image.copy()
imageg = image.copy()

imageb[:, :] = (255, 0, 0) #set all pixels to the blue colour    #imageb[:, :] refers to all rows and all columns in the image.
imageg[:, :] = (0, 255, 0) #set all pixels to the blue green
imager[:, :] = (0, 0, 255) #set all pixels to the blue red


cv2.imshow("Blue", imageb)
cv2.imshow("Green", imageg)
cv2.imshow("red", imager)
#cv2_imshow(imageb) #Use the function from google.colab.patches
#cv2_imshow(imageg)
#cv2_imshow(imager)

cv2.waitKey(0)             #This function waits for a key event indefinitely. The argument 0 means the program will wait indefinitely until a key is pressed.
cv2.destroyAllWindows      # To close all the windows of opencv
