from pathlib import Path

import cv2
import numpy as np

img_path = str(Path(__file__).parent.parent / 'Images/6by6.png')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
Hx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])


def convolve_np(X, F):
    X_height = X.shape[0]
    X_width = X.shape[1]

    F_height = F.shape[0]
    F_width = F.shape[1]

    H = int((F_height - 1) / 2)
    W = int((F_width - 1) / 2)

    out = np.zeros((X_height, X_width))

    for i in np.arange(H, X_height - H):
        for j in np.arange(W, X_width - W):
            out[i, j] = np.tensordot(X[i - H:i + H + 1, j - W:j + W + 1], F, axes=((0, 1), (0, 1)))
    return out


img_x = convolve_np(img, Hx) / 8.0
print(img_x)
cv2.imwrite(str(Path(__file__).parent / 'out.png'), img_x)
cv2.imshow('image', img_x)
cv2.waitKey(0)
cv2.destroyAllWindows()

