import cv2

# Load the image from the specified path
image_path = 'E:\\MY FILES\\Wallpapers\\Screenshot_20221014-185651_YouTube.jpg'
image = cv2.imread(image_path)

# Check if the image was successfully loaded
if image is None:
    print(f"Error: Unable to load image at {image_path}")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale image
    blurred_image = cv2.GaussianBlur(gray_image, (3, 3), 0)

    # Detect edges using the Canny algorithm
    edges = cv2.Canny(blurred_image, 15, 35)

    # Display the original image and the edges
    cv2.imshow('Original Image', image)
    cv2.imshow('Edges', edges)

    # Wait for a key press and close the displayed windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()