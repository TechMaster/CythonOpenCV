import cv2
import time
import contrast

img = cv2.imread('tiger_low_constrast.jpg', cv2.IMREAD_GRAYSCALE)

start_time = time.time()

contrast.adjust_contrast(img, 3)

elapsed_time = time.time() - start_time
print(elapsed_time)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
