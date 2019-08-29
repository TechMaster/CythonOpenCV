# https://github.com/machinelearninggod/Image-Processing-Algorithms/blob/master/histogram_equalization.py
# https://www.youtube.com/watch?v=z_Gm3UL_j_0&list=PLh6SAYydrIpctChfPFBlopqw-TGjwWf_8&index=7
import numpy as np
import cv2
from pathlib import Path

img_path = str(Path(__file__).parent.parent / 'Images/african_leopard_bw_low.jpg')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
height = img.shape[0]
width = img.shape[1]
pixels = width * height

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
cum_hist = hist.cumsum()
scale = 255.0/pixels

img = np.array(cum_hist[img] * scale, dtype=np.uint8)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
