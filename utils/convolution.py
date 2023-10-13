import numpy as np
import cv2

def conv(image):
    '''
    :param image:
    :return:convolved image
    '''
    kernel = np.array([[-1, 0, 1],
                       [-1, 0, 1],
                       [-1, 0, 1]], dtype=np.float32)

    kernel = kernel / np.sum(np.abs(kernel)) if np.sum(np.abs(kernel)) != 0 else kernel
    convolved_img = cv2.filter2D(image, -1, kernel)

    return convolved_img