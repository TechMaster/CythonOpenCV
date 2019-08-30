import numpy as np
import cv2
from pathlib import Path

img_path = str(Path(__file__).parent.parent / 'Images/4by4.jpg')
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

for ix, iy in np.ndindex(img.shape):
    print(img[ix, iy])
