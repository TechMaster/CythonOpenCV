import matplotlib.pylab as plt
from skimage import color
from skimage.io import imread

im = imread("../images/parrot.png")
im_hsv = color.rgb2hsv(im)
plt.gray()
plt.figure(figsize=(10, 8))
plt.subplot(221), plt.imshow(im_hsv[..., 0]), plt.title('Hue', size=20), plt.axis('off')
plt.subplot(222), plt.imshow(im_hsv[..., 1]), plt.title('Saturation', size=20), plt.axis('off')
plt.subplot(223), plt.imshow(im_hsv[..., 2]), plt.title('Value', size=20), plt.axis('off')
plt.subplot(224), plt.axis('off')
plt.show()
