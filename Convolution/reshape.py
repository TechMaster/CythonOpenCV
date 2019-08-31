import numpy as np

kernel = np.array([[1, 0, 0],
                   [0, 1, 1],
                   [1, 0, 1]])

out = kernel.reshape(3, 3, 1)
print(out[1])