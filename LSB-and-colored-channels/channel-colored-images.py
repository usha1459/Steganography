import cv2
import numpy as np

def extract_channels(image_path):
  """Extracts red, green, and blue channels from an image.

  Args:
    image_path: Path to the image file.

  Returns:
    A tuple of three NumPy arrays representing the red, green, and blue channels.
  """

  img = cv2.imread(image_path)

  # Split the image into its BGR channels
  b, g, r = cv2.split(img)

  return r, g, b

# Example usage:
image_path = "D:\Encoder\Final\encoded_image.png"
red, green, blue = extract_channels(image_path)

# Display the channels (optional)
cv2.imshow("Red", red)
cv2.imshow("Green", green)
cv2.imshow("Blue", blue)
cv2.waitKey(0)
cv2.destroyAllWindows()
