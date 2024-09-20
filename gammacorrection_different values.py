import cv2
import numpy as np

def gamma_correction(image, gamma):

    #Create a lookup table for the gamma correction
    lookup_table = np.array([(i / 255.0) ** gamma * 255 for i in range(256)], dtype = 'uint8')  #(i / 255.0): Normalizes the pixel value i to the range [0, 1].

    #Apply gamma correction using the lookup table
    corrected_image = cv2.LUT(image, lookup_table) #LUT - look Up Table: The precomputed table that maps each pixel value to its gamma-corrected value.
    return corrected_image

imagepath = 'D:/img_processing_programms/images/'
imagename = 'darkimg_1.png'
inputimage = imagepath+imagename
#D:\img_processing_programms\images\darkimg_1.png


#Load an image
image = cv2.imread(inputimage)

# Gamma values for correction
#gamma_values = [0.8, 1.2, 1.5, 2.0]   """we used these values for bright to dark"""  1 and below is light
gamma_values = [0.1, 0.8, 0.88, 1.0]

# Apply gamma correction for different gamma values
for gamma in gamma_values:
    corrected_image = gamma_correction(image, gamma)   #applies the gamma correction function to each gamma value
    output_image = imagepath + str(gamma) + imagename   #output_img = output path_{gamma}.png
    cv2.imwrite(output_image, corrected_image)
    print(f"Image saved as {output_image}")     # f string : formatted string literal
