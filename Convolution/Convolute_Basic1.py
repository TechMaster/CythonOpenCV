import numpy as np

import convolute_lib as cnn


in_img = np.array([[1, 0, 0, 1, 0],
                   [0, 1, 1, 0, 1],
                   [1, 0, 1, 0, 1],
                   [1, 0, 0, 1, 1],
                   [0, 1, 1, 0, 1]
                   ])

kernel = np.array([[1, 0, 0],
                   [0, 1, 1],
                   [1, 0, 1]])

identity = np.array([[0, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]])

out_img = cnn.convolve_np4(in_img, identity)
with np.printoptions(suppress=True):
    print(out_img)
