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
    padded_h,padded_w=h+2*padding_req,w+2*padding_req
    padded_image=np.ones((padded_h,padded_w),dtype=array.dtype)
    padded_image[padding_req:padding_req + h, padding_req:padding_req + w] = array
    #print(padded_image.shape)
    return padded_image