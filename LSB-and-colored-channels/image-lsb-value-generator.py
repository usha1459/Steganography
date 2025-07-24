import cv2
import numpy as np
import pandas as pd

def extract_rgb_to_dataframe(image_path):
  """Extracts RGB values and LSBs from an image and returns a pandas DataFrame.

  Args:
    image_path: Path to the image file.

  Returns:
    A pandas DataFrame with columns 'x', 'y', 'red', 'green', 'blue', 'lsb_red', 'lsb_green', 'lsb_blue'.
  """

  img = cv2.imread(image_path)
  img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

  height, width, _ = img_rgb.shape

  # Create coordinate matrices
  x, y = np.meshgrid(np.arange(width), np.arange(height))

  # Reshape image to a 2D array
  img_flat = img_rgb.reshape(-1, 3)

  # Extract LSBs
  lsb_red = img_flat[:, 0] & 1
  lsb_green = img_flat[:, 1] & 1
  lsb_blue = img_flat[:, 2] & 1

  # Create DataFrame
  df = pd.DataFrame({'x': x.flatten(), 'y': y.flatten(), 'red': img_flat[:, 0], 'green': img_flat[:, 1], 'blue': img_flat[:, 2],
                     'lsb_red': lsb_red, 'lsb_green': lsb_green, 'lsb_blue': lsb_blue})

  return df

# Example usage:
image_path = "D:\Encoder\Final\encoded_image.png"
df = extract_rgb_to_dataframe(image_path)
print(df.head())
df.to_csv('D:\Encoder\Final\RGB_values_with_LSB.csv')