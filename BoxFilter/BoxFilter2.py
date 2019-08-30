import numpy as np
import cv2
import time
from pathlib import Path

img_path = str(Path(__file__).parent.parent / 'Images/cat_bw.jpg')
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img_out = img.copy()
height = img.shape[0]
width = img.shape[1]

# This code chạy rất là chậm !
# 1  1  1  1  1  1 -> 6
# 1  2  2  2  2  1 -> 10
# 1  2  3  3  2  1 -> 12
# 1  2  3  3  2  1 -> 12
# 1  2  2  2  2  1 -> 10
# 1  1  1  1  1  1 -> 6
# 36 + 20 56
start_time = time.time()
for i in range(3, height - 3):
    for j in range(3, width - 3):
        sum = 0
        for k in range(-3, 4):
            for l in range(-3, 4):
                sum = sum + img[i + k, j + l]

        img_out[i, j] = int(sum / 49.0)

img_out = np.array(img_out, dtype=np.uint8)
elapsed_time = time.time() - start_time
print(elapsed_time)

cv2.imshow('image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
