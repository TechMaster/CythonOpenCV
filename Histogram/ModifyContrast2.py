# https://www.youtube.com/watch?v=lRNt6CpkrbU

import numpy as np
import cv2
from pathlib import Path

img_path = str(Path(__file__).parent.parent / 'Images/african_leopard_bw_low.jpg')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
cum_hist = hist.cumsum()

height = img.shape[0]
width = img.shape[1]

p = 0.005
pixels_p = (width * height) * p
pixels_1_p = (width * height) * (1 - p)

a_low = np.argmax(cum_hist >= pixels_p)
cum_hist_reverse = cum_hist[::-1]
a_high = 255 - np.argmax(cum_hist_reverse <= pixels_1_p)
scale = 255 / (a_high - a_low)

table = np.array([0 if i <= a_low else 255 if i >= a_high else float(i - a_low) * scale
                  for i in range(256)]).astype("uint8")

img_out = cv2.LUT(img, table) # Chạy cực chậm

cv2.imshow('image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
