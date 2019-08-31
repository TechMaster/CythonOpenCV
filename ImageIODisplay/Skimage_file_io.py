import matplotlib.pylab as plt
from skimage import color
from skimage.io import imread, imsave, imshow, show

im = imread("../images/parrot.png")  # read image from disk, provide the correct path
print(im.shape, im.dtype, type(im))
# (362, 486, 3) uint8 <class 'numpy.ndarray'>
hsv = color.rgb2hsv(im)  # from RGB to HSV color space
hsv[:, :, 1] = 0.5  # change the saturation
im1 = color.hsv2rgb(hsv)  # from HSV back to RGB
imsave('../images/parrot_hsv.png', im1)  # save image to disk
im = imread("../images/parrot_hsv.png")
plt.axis('off'), imshow(im), show()
