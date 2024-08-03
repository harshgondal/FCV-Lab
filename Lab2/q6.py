import cv2
import numpy as np


def resize_image(image, width, height):
    """
    Resize the image to the specified width and height.

    Parameters:
    - image: Input image.
    - width: Desired width of the output image.
    - height: Desired height of the output image.

    Returns:
    - Resized image.
    """
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)


def crop_image(image, x, y, width, height):
    """
    Crop a rectangular region from the image.

    Parameters:
    - image: Input image.
    - x: Starting x-coordinate of the crop rectangle.
    - y: Starting y-coordinate of the crop rectangle.
    - width: Width of the crop rectangle.
    - height: Height of the crop rectangle.

    Returns:
    - Cropped image.
    """
    return image[y:y + height, x:x + width]


# Load the image
image = cv2.imread('sample.jpg')

# Check if the image is loaded successfully
if image is None:
    raise ValueError("Image not loaded. Please check the file path.")

# Resize the image
new_width = 800
new_height = 600
resized_image = resize_image(image, new_width, new_height)
cv2.imwrite('resized_image.jpg', resized_image)

# Crop the image
x_start = 100
y_start = 50
crop_width = 400
crop_height = 300
cropped_image = crop_image(image, x_start, y_start, crop_width, crop_height)
cv2.imwrite('cropped_image.jpg', cropped_image)
