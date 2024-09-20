import cv2
import numpy
imagepath ='D:/images/'
imagename='Mausam.jpeg'
imagefile = imagepath+imagename
image = cv2.imread(imagefile)

#Create a negative image by subtracting the image from 255
negative_image = 255 - image     #For each pixel in the image, this operation subtracts the pixel value from 255. In RGB images, each pixel value ranges from 0 to 255. Subtracting from 255 inverts the color.

#Display the negative image
cv2.imshow('original Image', image)
cv2.imshow('Negative Image', negative_image)

negname= 'Mneg_img.jpeg'
imagefile = imagepath+negname
cv2.imwrite(imagefile,negative_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
