from pathlib import Path

import cv2
import numpy as np

import convolute_lib as cnn

img_path = str(Path(__file__).parent.parent / 'Images/cat_bw.jpg')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
sobelX = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])

sobelY = np.array([[-1, -2, -1],
               [0, 0, 0],
               [1, 2, 1]])



img_x = cnn.convolve_np4(img, sobelX)
img_y = cnn.convolve_np4(img, sobelY)

print(img_x.shape)

cv2.imshow('EdgeX', cv2.convertScaleAbs(img_x))
cv2.imshow('EdgeY', cv2.convertScaleAbs(img_y))
cv2.waitKey(0)
cv2.destroyAllWindows()
