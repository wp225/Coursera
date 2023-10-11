from utils.img import image
from utils.padding import zero_padding
img_obj=image('./test_image.webp')
img=img_obj.load_image()
zero_padding(img)
