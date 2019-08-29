import cv2
import time
from pathlib import Path

img_path = str(Path(__file__).parent.parent / 'Images/african_leopard_bw_low.jpg')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
contrast = 2
start_time = time.time()
img = img * contrast
img[img > 255] = 255
elapsed_time = time.time() - start_time

print(elapsed_time)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
