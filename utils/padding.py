import cv2
import numpy as np

def zero_padding(image,filter_size):
    '''
    :param image:
    :return: padded image
    '''
    array=np.array(image)
    h,w=array.shape[0],array.shape[1]
    padding_req=int((filter_size-1)/2)
    padded_image=np.array([h+padding_req,w+padding_req,3],dtype=np.uint8)
    padded_h,padded_w=padded_image[0],padded_image[1]
    padded_image[:,:]=np.array([0,64,128])
    padded_image[padded_h:h,padded_w:w]=array
    return padded_image

if __name__ == '__main__':
    image=cv2.imread('./test_image.webp')
    cv2.imshow('img',image)
    #zero_padding(image,3)