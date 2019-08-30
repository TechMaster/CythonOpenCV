import numpy as np
import cv2
import time
from pathlib import Path

img_path = str(Path(__file__).parent.parent / 'Images/cat_bw.jpg')
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

img_out = img.copy()
height = img.shape[0]
width = img.shape[1]

laplace = (1.0 / 16) * np.array(
    [[ 0,  0, -1,  0,  0],
     [ 0, -1, -2, -1,  0],
     [-1, -2, 16, -2, -1],
     [ 0, -1, -2, -1,  0],
     [ 0,  0, -1,  0,  0]])

print(sum(sum(laplace)))

start_time = time.time()
for i in np.arange(2, height - 2):
    for j in np.arange(2, width - 2):
        img_out[i, j] = np.tensordot(img[i-2:i+3, j-2:j+3], laplace, axes=((0, 1), (0, 1)))

elapsed_time = time.time() - start_time
print(elapsed_time)

cv2.imshow('image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
