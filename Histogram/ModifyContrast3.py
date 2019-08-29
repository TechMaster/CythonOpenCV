# https://www.youtube.com/watch?v=lRNt6CpkrbU

import numpy as np
import cv2
from pathlib import Path
import time
import cummulative_contrast as contrast

img_path = str(Path(__file__).parent.parent / 'Images/african_leopard_bw_low.jpg')
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
start_time = time.time()
img_out = contrast.auto_contrast(img)
elapsed_time = time.time() - start_time

print(elapsed_time)

cv2.imshow('image', np.array(img_out))
cv2.waitKey(0)
cv2.destroyAllWindows()
