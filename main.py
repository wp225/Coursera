import cv2
from utils.padding import zero_padding
from utils.convolution import conv
import matplotlib.pyplot as plt
import numpy as np
path='./test_image.webp'
def padding (path):
    '''
    :param image: np array
    :return: same padded np array
    '''
    image=load_image(path)
    padded_image=zero_padding(image,7)
    return padded_image

def convolution(image):
    conv_image=conv(image)
    show_image(conv_image)
def load_image(path):
    '''
    :param path: image path
    :return: image
    '''
    image = cv2.imread(path)
    img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return img

def show_image(image: object) -> object:
    '''
   :param image:image np array
    :return: show image
    '''
    cv2.imshow('imahge',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image=padding('./test_image.webp')
convolved_img=convolution(image)
show_image(convolved_img)