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
scale = 255.0/pixels

img_out = np.array(cum_hist[img] * scale, dtype=np.uint8)

fig, axs = plt.subplots(1, 2, figsize=(16, 8))

hist_out = cv2.calcHist([img_out], [0], None, [256], [0, 256])
cum_hist_out = hist_out.cumsum()
axs[0].bar(range(256), hist_out.ravel())
axs[0].bar(range(256), cum_hist_out/20)
axs[0].set(title="Histogram")

axs[1].grid(False)
axs[1].set_xticks([])
axs[1].set_yticks([])
axs[1].imshow(img_out, cmap='gray', vmin=0, vmax=255)

plt.show()
