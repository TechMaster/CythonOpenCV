from pathlib import Path

import cv2
import numpy as np

import convolute_lib as cnn

img_path = str(Path(__file__).parent.parent / 'Images/cat_bw.jpg')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

identity = np.array((
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]))

edge = np.array((
    [0,  1,  0],
    [1, -4,  1],
    [0,  1,  0]))

boxblur = (1.0 / 9) * np.array(
    [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]])

gaussian = (1.0 / 16) * np.array(
    [[1, 2, 1],
     [2, 4, 2],
     [1, 2, 1]])

emboss = np.array(
    [[-2, -1,  0],
     [-1,  1,  1],
     [ 0,  1,  2]])

square = np.array(
    [[ 0,  2,  0],
     [-2, -1,  2],
     [ 0, -2,  0]])

# construct average blurring kernels used to smooth an image
smallBlur = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))
largeBlur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))

# construct a sharpening filter
sharpen = np.array((
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]))

laplacian = (1.0 / 16) * np.array(
    [[ 0,  0, -1,  0,  0],
     [ 0, -1, -2, -1,  0],
     [-1, -2, 16, -2, -1],
     [ 0, -1, -2, -1,  0],
     [ 0,  0, -1,  0,  0]])

sobelX = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]))

sobelY = np.array((
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]))

img_out = cnn.convolve_np4(img, square)

img_out = cv2.convertScaleAbs(img_out)

cv2.imshow('Blur', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()