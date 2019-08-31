from pathlib import Path

import cv2
import numpy as np

img_path = str(Path(__file__).parent.parent / 'Images/plane_noisy.png')
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

weights = np.array(
    [[0, 0, 1, 2, 1, 0, 0],
     [0, 1, 2, 3, 2, 1, 0],
     [1, 2, 3, 4, 3, 2, 1],
     [2, 3, 4, 5, 4, 3, 2],
     [1, 2, 3, 4, 3, 2, 1],
     [0, 1, 2, 3, 2, 1, 0],
     [0, 0, 1, 2, 1, 0, 0]])


for i in np.arange(3, height - 3):
    for j in np.arange(3, width - 3):
        # Cách này không thực sự đúng
        img_out[i, j] = np.average(img[i-3:i+4, j-3:j+4], weights=weights)


cv2.imshow('image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
