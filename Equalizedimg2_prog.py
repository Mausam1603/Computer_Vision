import cv2
#import numpy as np
#from matplotlib import pyplot as plt
#read image as grayscale
image = cv2.imread('C:/Users/DELL/Documents/img_processing_programms/images/low_contrast2img.png', cv2.IMREAD_GRAYSCALE)
equalized_image = cv2.equalizeHist(image)
cv2.imwrite('C:/Users/DELL/Documents/img_processing_programms/images/equalizedimg2.jpeg', equalized_image)

