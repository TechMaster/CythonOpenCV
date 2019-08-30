# cython: language_level=3, boundscheck=False

import numpy as np
import cv2

cpdef unsigned char[:, :] filter(unsigned char[:, :] img):
    cdef int i, j, width, height
    img_out = img.copy()
    height = img.shape[0]
    width = img.shape[1]

    for i in range(3, height - 3):
        for j in range(3, width - 3):
            img_out[i, j] = int(np.sum(img[i-3:i+4, j-3:j+4]) / 49.0)

    return np.array(img_out, dtype=np.uint8)