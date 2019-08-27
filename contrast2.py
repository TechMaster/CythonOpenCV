import cv2
import math
import time

img = cv2.imread('tiger_low_constrast.jpg', cv2.IMREAD_GRAYSCALE)

def adjust_contrast(img, contrast):
    height = img.shape[0]
    width = img.shape[1]

    for i in range(height):
        for j in range(width):
            a = img.item(i, j)
            b = math.ceil(a * contrast)
            if b > 255:
                b = 255
            img.itemset((i, j), b)


start_time = time.time()
adjust_contrast(img, 3)
elapsed_time = time.time() - start_time

print(elapsed_time)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
