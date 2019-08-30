# https://www.youtube.com/watch?v=BBHpijOTyUk&list=PLh6SAYydrIpctChfPFBlopqw-TGjwWf_8&index=11
import numpy as np
import cv2
import time
from pathlib import Path

img_path = str(Path(__file__).parent.parent / 'Images/cat_bw.jpg')
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

gauss = (1.0 / 57) * np.array(
    [[0, 1, 2, 1, 0],
     [1, 3, 5, 3, 1],
     [2, 5, 9, 5, 2],
     [1, 3, 5, 3, 1],
     [0, 1, 2, 1, 0]])
print(sum(sum(gauss)))


start_time = time.time()
for i in np.arange(2, height - 2):
    for j in np.arange(2, width - 2):
        sum = 0
        for k in np.arange(-2, 3):
            for l in np.arange(-2, 3):
                a = img.item(i + k, j + l)
                p = gauss[2 + k, 2 + l]
                sum = sum + (p * a)
        b = sum
        img_out.itemset((i, j), b)
elapsed_time = time.time() - start_time
print(elapsed_time)

cv2.imshow('image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
