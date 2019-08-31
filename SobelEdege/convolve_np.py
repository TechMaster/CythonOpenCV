import numpy as np


# X and F are numpy matrices
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
            '''
            sum = 0
            for k in np.arange(-H, H + 1):
                for l in np.arange(-W, W + 1):
                    a = X[i + k, j + l]
                    w = F[H + k, W + l]
                    sum += (w * a)
            out[i, j] = sum
            '''
            out[i, j] = np.tensordot(X[i - H:i + H + 1, j - W:j + W + 1], F, axes=((0, 1), (0, 1)))
    return out
