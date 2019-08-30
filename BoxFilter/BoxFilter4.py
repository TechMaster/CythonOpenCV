import numpy as np
import cv2
import time
import BoxFilter # Cần phải vào console chạy lệnh để tạo file so trước đã python setup.py build_ext --inplace
from pathlib import Path

img_path = str(Path(__file__).parent.parent / 'Images/cat_bw.jpg')
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

start_time = time.time()
img_out = BoxFilter.filter(img)
elapsed_time = time.time() - start_time
print(elapsed_time)

cv2.imshow('image', np.array(img_out))
cv2.waitKey(0)
cv2.destroyAllWindows()
