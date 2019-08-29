import cv2
import time
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

img_path = str(Path(__file__).parent.parent / 'Images/african_leopard_bw.jpg')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)


def histogram(img):
    height = img.shape[0]
    width = img.shape[1]

    hist = np.zeros(256)

    for i in range(height):
        for j in range(width):
            a = img.item(i, j)
            hist[a] += 1

    return hist


np.set_printoptions(suppress=True, precision=0)
hist = histogram(img)

fig, axs = plt.subplots(1, 2, figsize=(16, 8))

axs[0].plot(range(256), hist)
axs[0].fill_between(range(256), 0, hist)

axs[0].set(title="Histogram")

axs[1].grid(False)
axs[1].set_xticks([])
axs[1].set_yticks([])
axs[1].imshow(img, cmap='gray')

plt.show()
