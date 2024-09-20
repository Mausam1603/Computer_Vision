import cv2
import numpy as np

def gamma_correction(image, gamma):

    #Create a lookup table for the gamma correction
    lookup_table = np.array([(i / 255.0) ** gamma * 255 for i in range(256)], dtype = 'uint8')

    #Apply gamma correction using the lookup table
    corrected_image = cv2.LUT(image, lookup_table)
    return corrected_image

image = cv2.imread('D:/img_processing_programms/images/low_contrast2img.png')
gamma = 2.2

#Apply gamma correction
gamma_corrected_image = gamma_correction(image,gamma)

#Write the gammacorrected image
#outputimage = imagepath+str(gamma)+imagename    - here we use str to get multiple o/p images with gamma values

cv2.imwrite("gammacorrectedimg.jpg", gamma_corrected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
