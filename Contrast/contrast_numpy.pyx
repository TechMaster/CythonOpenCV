# cython: language_level=3, boundscheck=False
# Chưa tối ưu triệt để, chỉ biên dịch ra C
import cv2
import math

def adjust_contrast(img, contrast):
    img = img * contrast
    img[img > 255] = 255