import cv2

# Load the image
image = cv2.imread('Picture1.jpeg')

# Define the desired dimensions for the resized image
width = 500
height = 200

# Resize the image
resized_image = cv2.resize(image, (width, height))

# Save the resized image
cv2.imwrite('resized_image.jpg', resized_image)