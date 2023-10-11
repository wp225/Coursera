import cv2
import matplotlib.pyplot as plt

# Load the padded image

# Display the image


from utils.img import image
from utils.padding import zero_padding
img_obj=image('./test_image.webp')
img=img_obj.load_image()
padded_image=zero_padding(img,3)
