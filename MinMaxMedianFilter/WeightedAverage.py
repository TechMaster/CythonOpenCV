import numpy as np

weights = np.array(
    [[1, 1, 1],
     [6, 100, 1],
     [1, 1, 1],
     ])

data = np.array(
    [[1, 1, 1],
     [1, 2, 1],
     [1, 1, 1],
     ])

res = np.average(data, weights=weights)
print(res)

total = np.tensordot(data, weights, axes=((0, 1), (0, 1)))
print(total)
sum_weight = np.sum(weights)
print(sum_weight)
print(total/sum_weight)

# Xem công thức tính weighted average ở đây
# https://stackoverflow.com/questions/38241174/weighted-average-using-numpy-average