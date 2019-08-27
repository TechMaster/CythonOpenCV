# cython: language_level=3, boundscheck=False

import cv2
cdef extern from "math.h":
    double ceil(double x)

cpdef unsigned char[:, :] adjust_contrast(unsigned char[:, :] img, float contrast):
    cdef int x, y, w, h, b
    height = img.shape[0]
    width = img.shape[1]
    for y in range(0, height):
        for x in range(0, width):
            b = int(ceil(img[y, x] * contrast))
            if b > 255:
                b = 255
            img[y, x] = b

    return img