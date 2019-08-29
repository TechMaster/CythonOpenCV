# cython: language_level=3, boundscheck=False


import numpy as np
import cv2

cpdef unsigned char[:, :] auto_contrast(unsigned char[:, :] img):
    cdef int x, y, width, height, pixels, a_low, a_high
    cdef int a, b
    cdef float scale, p
    p = 0.005
    height = img.shape[0]
    width = img.shape[1]
    pixels = width * height

    pixels_p = pixels * p
    pixels_1_p = pixels * (1 - p)

    hist =  cv2.calcHist([np.array(img)], [0], None, [256], [0, 256])
    cum_hist = hist.cumsum()
    a_low = np.argmax(cum_hist >= pixels_p)
    cum_hist_reverse = cum_hist[::-1]
    a_high = 255 - np.argmax(cum_hist_reverse <= pixels_1_p)
    scale = 255.0 / (a_high - a_low)

    for y in range(height):
        for x in range(width):
            a = img[y, x]
            if a < a_low:
                b = 0
            elif a > a_high:
                b = 255
            else:
                b = int((a - a_low) * scale)
                
            img[y, x] = b
    return img