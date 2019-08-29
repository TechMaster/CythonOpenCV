# Cải tiến code từ video này, sử dụng numpy để tăng tốc
# https://www.youtube.com/watch?v=LJtVG2IAVfU
import cv2
import time
import numpy as np
from pathlib import Path

img_path = str(Path(__file__).parent.parent / 'Images/african_leopard_bw_low.jpg')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img_np = np.array(img)
min_pix = img_np.min()  # Lấy giá trị xám nhất của ảnh
max_pix = img_np.max()  # Lấy giá trị sáng nhất của ảnh

# Tính scale để sau khi nhân, điểm sáng nhất là 255
# điểm tối nhất là 0.0
scale = 255.0 / float(max_pix - min_pix)

start_time = time.time()
# Bắt buộc phải dùng np.array(..., dtype=np.uint8) để bit
# đảm bảo mỗi phần tử là unsigned interger 8

imgout = np.array((img - min_pix) * scale, dtype=np.uint8)
elapsed_time = time.time() - start_time

print(elapsed_time)

cv2.imshow('image', imgout)
cv2.waitKey(0)
cv2.destroyAllWindows()
