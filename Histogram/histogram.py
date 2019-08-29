import numpy as np

def histogram(img):
    height = img.shape[0]
    width = img.shape[1]

    hist = np.zeros(256)

    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i, j)
            hist[a] += 1

    return hist
