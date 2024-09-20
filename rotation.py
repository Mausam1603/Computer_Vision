import cv2
import numpy as np

#Load an image
imagepath = 'D:/images/'
imagename = 'Mausam_N.jpeg'
imagefile =imagepath +imagename
orimage = cv2.imread(imagefile)
image = orimage.copy()

height, width = image.shape[:2]     #:2 stands for slicing of height and width
print("\nHeight=", height,"width=", width)
angle = 90

#find rotation matrix
cx = width/2
cy = height/2
rotation_matrix = cv2.getRotationMatrix2D((cx,cy), angle,1)
rotatio_matrix = cv2.getRotationMatrix2D((0,0), angle, 0.5)  #0.5: This is the scaling factor. A value of 0.5 means the image will be scaled down to half its original size after rotation.

#Apply the rotation to the image
rotated_image = cv2.warpAffine(image, rotation_matrix, (width,height))

#Display the rotated Image
rotimgname='rotmausam.jpeg'
rotimgfile=imagepath + imagename
cv2.imshow('original Image', image)
cv2.imwrite(rotimgfile, rotated_image)

#Display the rotated image
cv2.imshow('rotated_image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
