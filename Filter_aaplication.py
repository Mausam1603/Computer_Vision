import cv2
import numpy as np

imagepath = 'C:/Users/DELL/Documents/img_processing_programms/images/'
imagename = 'darkimg_gain_ip.png'
new_imglight = 'new_imglight.jpg'
inputimage = imagepath + imagename
outputimage = imagepath + new_imglight

def apply_filters (inputimage, outputimage, gain, bias):
    """Applies gain and bias to an image.

    Args:
        inputimage: Path to the input image.
        outputimage: Path to save the output image.
        gain: Gain factor to apply to the image.
        bias: Bias value to add to the image.
    """

    image = cv2.imread(inputimage, cv2.IMREAD_COLOR)

    if image is None:
        print("Error: Could not open or find the image.")
        return

    # Apply gain and bias
    output_image = (gain * image + bias).astype(np.uint8)

    # Write the output image
    cv2.imwrite(outputimage, output_image)

# Example usage:
gain_value = 1.5  # can be adjusted
bias_value = 30   # can be adjusted
apply_gain_and_bias(inputimage, outputimage, gain_value, bias_value)


