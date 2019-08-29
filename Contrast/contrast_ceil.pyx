# cython: language_level=3, boundscheck=False

import cv2
cdef extern from "math.h":
    double ceil(double x)

cpdef unsigned char[:, :] adjust_contrast(unsigned char[:, :] img, float contrast):
    cdef int x, y, width, height, b
    height = img.shape[0]
    width = img.shape[1]

    for y in range(height):
        for x in range(width):
            b = int(ceil(img[y, x] * contrast))
            if b > 255:
                b = 255
            img[y, x] = b
    return img