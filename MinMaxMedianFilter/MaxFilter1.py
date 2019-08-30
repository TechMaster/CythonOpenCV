import numpy as np
import cv2
import time
from pathlib import Path

img_path = str(Path(__file__).parent.parent / 'Images/cat_bw.jpg')
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]
start_time = time.time()
for i in np.arange(3, height - 3):
    for j in np.arange(3, width - 3):
        max = 0
        for k in np.arange(-3, 4):
            for l in np.arange(-3, 4):
                a = img.item(i + k, j + l)
                if a > max:
                    max = a
        b = max
        img_out.itemset((i, j), b)

elapsed_time = time.time() - start_time
print(elapsed_time)
cv2.imshow('image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
