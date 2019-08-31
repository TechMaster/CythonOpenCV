import matplotlib.image as mpimg
import matplotlib.pylab as plt

im = mpimg.imread("../images/alps.png")  # read the image from disk as a numpy ndarray
print(im.shape, im.dtype, type(im))  # this image contains an α channel, hence num_channels= 4
# (960, 1280, 4) float32 <class 'numpy.ndarray'>
plt.figure(figsize=(10, 10))
plt.imshow(im)  # display the image
plt.axis('off')

im1 = im
im1[im1 < 0.5] = 0  # make the image look darker
plt.imshow(im1)
plt.axis('off')
plt.tight_layout()
plt.savefig("../images/alps_dark.png")  # save the dark image
im = mpimg.imread("../images/alps_dark.png")  # read the dark image
plt.figure(figsize=(10, 10))
plt.imshow(im)
plt.axis('off')  # no axis ticks
plt.tight_layout()
plt.show()
