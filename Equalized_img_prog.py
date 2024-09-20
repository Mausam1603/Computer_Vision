import cv2
#import numpy as np
#from matplotlib import pyplot as plt
#read image as grayscale
image = cv2.imread('C:/Users/DELL/Documents/img_processing_programms/images/Low_contrast_img.jpg', cv2.IMREAD_GRAYSCALE) 
#Specifies that the image should be read in grayscale mode. This means the image will be converted to a single channel where each pixel represents intensity.
equalized_image = cv2.equalizeHist(image)
cv2.imwrite('C:/Users/DELL/Documents/img_processing_programms/images/equalizedimg.jpeg', equalized_image)



#Histogram equalization is a technique used in image processing to enhance the contrast of an image. 
#It works by redistributing the intensity values of the image to span the full range of possible values, which can improve visibility and details in images with low contrast.