# cython: language_level=4

import cv2
import math
import numpy as np

def adjust_contrast(img, contrast):
    height = img.shape[0]
    width = img.shape[1]

    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i, j)
            b = math.ceil(a * contrast)
            if b > 255:
                b = 255
            img.itemset((i, j), b)