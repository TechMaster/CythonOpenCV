import numpy as np
import cv2
from pathlib import Path

img1_path = str(Path(__file__).parent.parent / 'Images/african_leopard_bw.jpg')
img2_path = str(Path(__file__).parent.parent / 'Images/eagle_bw.jpg')

img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

height = img1.shape[0]
width = img1.shape[1]

alpha = 0.5

'''
for i in range(height):
    for j in range(width):
        img1[i, j] = alpha * img1[i, j] + (1 - alpha) * img2[i, j]
'''
img_out = np.array(alpha * img1 + (1 - alpha) * img2, dtype=np.uint8)

cv2.imshow('image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
