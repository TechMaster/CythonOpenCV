import cv2
import time
import matplotlib.pyplot as plt
from pathlib import Path


img_path = str(Path(__file__).parent.parent / 'Images/african_leopard_bw_low.jpg')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
start_time = time.time()
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
elapsed_time = time.time() - start_time
print(elapsed_time)

fig, axs = plt.subplots(1, 2, figsize=(16, 8))


axs[0].fill_between(range(256), 0, hist.ravel())

axs[0].set(title="Histogram")

axs[1].grid(False)
axs[1].set_xticks([])
axs[1].set_yticks([])
axs[1].imshow(img, cmap='gray', vmin=0, vmax=255)

plt.show()
