from pathlib import Path

import cv2
import numpy as np
from matplotlib import pyplot as plt

from convolve_np import convolve_np

img_path = str(Path(__file__).parent.parent / 'Images/cat_bw.jpg')
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

height = img.shape[0]
width = img.shape[1]
print(width, height)
Hx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])

Hy = np.array([[-1, -2, -1],
               [0, 0, 0],
               [1, 2, 1]])

img_x = convolve_np(img, Hx) / 8.0
img_y = convolve_np(img, Hy) / 8.0

img_out = np.sqrt(np.power(img_x, 2) + np.power(img_y, 2))

img_out = (img_out / np.max(img_out)) * 255

'''
cv2.imshow("Sobel Edged", img_out)
cv2.waitKey(0)
'''
plt.imshow(img_out, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
