import cv2
import time
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

img_path = str(Path(__file__).parent.parent / 'Images/african_leopard_bw.jpg')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
# Tính histogram bằng Numpy chạy cực nhanh
start_time = time.time()
hist, bins = np.histogram(img.ravel(), 256, [0, 256])
elapsed_time = time.time() - start_time
print(elapsed_time)

'''
ravel chuyển ma trận nhiều chiều thành 1 chiều
[[  0   0   0   0]
 [  0 255 255   0]
 [  0 255 255   0]
 [  0   0   0   0]]

[  0   0   0   0   0 255 255   0   0 255 255   0   0   0   0   0]
'''

fig, axs = plt.subplots(1, 2, figsize=(16, 8))

axs[0].fill_between(range(256), 0, hist)

axs[0].set(title="Histogram")

axs[1].grid(False)
axs[1].set_xticks([])
axs[1].set_yticks([])
axs[1].imshow(img, cmap='gray')

plt.show()
