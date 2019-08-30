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

sum(sum(gauss))

start_time = time.time()
for i in np.arange(2, height - 2):
    for j in np.arange(2, width - 2):
        # Sử dụng np.tensordot tốc độ tăng lên gấp 3 lần !
        img_out[i, j] = np.tensordot(img[i - 2:i + 3, j - 2:j + 3], gauss, axes=((0, 1), (0, 1)))

elapsed_time = time.time() - start_time
print(elapsed_time)

cv2.imshow('image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
