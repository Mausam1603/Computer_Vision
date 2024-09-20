import numpy as np
import cv2
import math
imgpath='C:/Users/DELL/Documents/img_processing_programms/images/'

#Create a black image with dimensions 500X500
image = np.zeros((500, 500, 3), dtype = np.uint8)   #uint8 - unsigned integer
#The np.zeros function is used to create a black image by initializing a matrix (or an array) of the given dimensions filled with zeros. 

#Draw a blue recatnagle on the image
cv2.rectangle(image, (100,100), (200,200), (255,0,0), -1)
cv2.rectangle(image, (200,200), (400,300), (255,0,255), -1)

#creating a circle
cv2.circle(image, (150,150), 25, (0,0,255), -1)

#creating a circumference
radius = int(math.sqrt (50 * 50 + 50 * 50))
cv2.circle (image, (150,150), radius, (255, 255, 0), 2)
#cv2.circle(image, (70,70), 25, (0,0,255), 2)


#Draw a line
pta = (150,150)
ptb = (150, 400)

cv2.line(image, pta,ptb, (255,255,255), 1)

#Draw a triangle
ptc = (500, 150)

cv2.line(image, pta,ptc, (255,255,255), 1)
cv2.line(image, ptb,ptc, (255,255,255), 1)

cv2.imshow('image', image)

#image_name
imgname='Geometry.jpg'
fullimgname=imgpath + imgname
cv2.imwrite(fullimgname, image)



cv2.waitKey(0)
cv2.destroyAllWindows()
