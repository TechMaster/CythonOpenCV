# https://www.youtube.com/watch?v=lRNt6CpkrbU

import numpy as np
import cv2
from pathlib import Path
import time
import cummulative_contrast as contrast
import matplotlib.pyplot as plt

img_path = str(Path(__file__).parent.parent / 'Images/african_leopard_bw_low.jpg')
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

fig = plt.figure(figsize=(12, 8))

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.2, wspace=0.1)
ax1 = fig.add_subplot(221)
ax1.set(title="Histogram Before")
ax1.fill_between(range(256), 0, hist.ravel())

ax2 = fig.add_subplot(222)
ax2.grid(False)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.imshow(img, cmap='gray', vmin=0, vmax=255)

img_out = np.array(contrast.auto_contrast(img))

hist_after = cv2.calcHist([img_out], [0], None, [256], [0, 256])
ax3 = fig.add_subplot(223)
ax3.fill_between(range(256), 0, hist_after.ravel())
ax3.set(title="Histogram After")

ax4 = fig.add_subplot(224)
ax4.grid(False)
ax4.set_xticks([])
ax4.set_yticks([])
ax4.imshow(img_out, cmap='gray', vmin=0, vmax=255)
plt.show()
