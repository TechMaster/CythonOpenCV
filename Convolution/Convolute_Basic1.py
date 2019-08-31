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


out_img = cnn.convolve_nest_loop(in_img, kernel)
with np.printoptions(suppress=True):
    print(out_img)
