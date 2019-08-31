import numpy as np

import convolute_lib as cnn


'''
Code demo cho ví dụ trong bài viết này
https://towardsdatascience.com/image-classification-in-10-minutes-with-mnist-dataset-54c35b77a38d
'''
in_img = np.array([[1, 0, 0, 1, 0],
                   [0, 1, 1, 0, 1],
                   [1, 0, 1, 0, 1],
                   [1, 0, 0, 1, 1],
                   [0, 1, 1, 0, 1]
                   ])

kernel = np.array([[1, 0, 0],
                   [0, 1, 1],
                   [1, 0, 1]])

identity = np.array((
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]))

out_img = cnn.convolve_np2(in_img, identity)
with np.printoptions(suppress=True):
    print(out_img)

in_img2 = np.array([[5, 1, 3, 6],
                    [2, 3, 2, 2],
                    [2, 2, 4, 2],
                    [5, 1, 3, 1]])

out_img2 = cnn.pool(in_img2, 2, 2)
print(out_img2)

# Thêm một cột nữa, nhưng không được tính vì cột này lẻ
in_img3 = np.array([[5, 1, 3, 6, 7],
                    [2, 3, 2, 2, 8],
                    [2, 2, 4, 2, 6],
                    [5, 1, 3, 1, 2]])


# Demo Max Pooling
out_img3 = cnn.pool(in_img3, 2, 2)
print(out_img3)
