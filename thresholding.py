import cv2 
import numpy as np

#Load the image 
image = cv2.imread('D:/img_processing_programms/images/Space.jpg')

#Convert the image to grayscale (if it's not already) 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Apply a binary threshold to the image 
#Parameters: source image, threshold value, max value, threshold type

threshold_value = 128         # values between 0 and 255
max_value = 255

thresh_type = cv2.THRESH_BINARY

_, thresholded_image = cv2.threshold(gray_image, threshold_value, max_value, thresh_type)

#Display the original and thresholded images.

cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)

#Wait until a key is pressed and then close the image windows 
cv2.waitKey(0) 
cv2.destroyAllWindows()