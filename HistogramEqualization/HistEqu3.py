# https://github.com/machinelearninggod/Image-Processing-Algorithms/blob/master/histogram_equalization.py
# https://www.youtube.com/watch?v=z_Gm3UL_j_0&list=PLh6SAYydrIpctChfPFBlopqw-TGjwWf_8&index=7
import numpy as np
import cv2
import matplotlib.pyplot as plt
from pathlib import Path

img_path = str(Path(__file__).parent.parent / 'Images/african_leopard_bw_low.jpg')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
height = img.shape[0]
width = img.shape[1]
pixels = width * height

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
cum_hist = hist.cumsum()
scale = 255.0 / pixels

# Sử dụng numpy
#img_out = np.array(cum_hist[img] * scale, dtype=np.uint8)

# Sử dụng OpenCV xem thêm ở đây
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html
img_out = cv2.equalizeHist(img)

fig = plt.figure(figsize=(12, 8))

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.2, wspace=0.1)
ax1 = fig.add_subplot(221)
ax1.set_xlim([0, 255])
ax1.bar(range(256), hist.ravel())
ax1.bar(range(256), cum_hist / 20)
ax1.set(title="Histogram Before")


ax2 = fig.add_subplot(222)
ax2.grid(False)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.imshow(img, cmap='gray', vmin=0, vmax=255)

hist_out = cv2.calcHist([img_out], [0], None, [256], [0, 256])
cum_hist_out = hist_out.cumsum()
ax3 = fig.add_subplot(223)
ax3.set_xlim([0, 255])

ax3.bar(range(256), hist_out.ravel())
ax3.bar(range(256), cum_hist_out / 20)
ax3.set(title="Histogram Equalize")

ax4 = fig.add_subplot(224)
ax4.grid(False)
ax4.set_xticks([])
ax4.set_yticks([])
ax4.imshow(img_out, cmap='gray', vmin=0, vmax=255)

plt.show()
