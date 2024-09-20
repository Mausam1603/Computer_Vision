import numpy as np
import cv2
import math
imgpath='C:/Users/DELL/Documents/img_processing_programms/images/'

#Create a black image with dimensions 500 X 500
image = np.zeros ((500, 500, 3) , dtype = np.uint8)

# Polygon corner points coordinates
pts = np.array([[25, 70], [25, 145],
                [75, 190], [150, 190],
                [200, 145], [200, 70], 
                [150, 25], [75, 25]],
               np.int32)

pts = pts.reshape((-1,1,2))

isClosed = True

#green colour in BGR
color = (0,255,0)

#Line thickness of 8 px
thickness = 8

## Using cv2.polylines() method
# Draw a Green polygon with 
# thickness of 1 px
image = cv2.polylines(image, [pts], 
                      isClosed, color, 
                      thickness)
 
# Displaying the image
cv2.imshow('image', image)
   

cv2.waitKey(0)
cv2.destroyAllWindows()

