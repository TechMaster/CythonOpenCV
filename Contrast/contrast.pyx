# cython: language_level=3, boundscheck=False
# Chưa tối ưu triệt để, chỉ biên dịch ra C
import cv2
import math

def adjust_contrast(img, contrast):
    height = img.shape[0]
    width = img.shape[1]

    for i in range(height):
        for j in range(width):
            a = img.item(i, j)
            b = math.ceil(a * contrast)
            if b > 255:
                b = 255
            img.itemset((i, j), b)