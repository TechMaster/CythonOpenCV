import matplotlib.image as mpimg
import matplotlib.pylab as plt

im = mpimg.imread("../images/lena_small.jpg")  # read the image from disk as a numpy ndarray
methods = ['none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'lanczos']

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8),
                         subplot_kw={'xticks': [], 'yticks': []})
fig.subplots_adjust(hspace=0.05, wspace=0.05)
for ax, interp_method in zip(axes.flat, methods):
    ax.imshow(im, interpolation=interp_method)
    ax.set_title(str(interp_method), size=20)
plt.tight_layout()
plt.show()
