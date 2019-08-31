from PIL import Image

im = Image.open("../images/parrot.png")  # read the image, provide the correct path
print(im.width, im.height, im.mode, im.format, type(im))
# 453 340 RGB PNG <class 'PIL.PngImagePlugin.PngImageFile'>
im.show()  # display the image

im_g = im.convert('L')  # convert the RGB color image to a grayscale image
im_g.save('../images/parrot_gray.png')  # save the image to disk
Image.open("../images/parrot_gray.png").show()  # read the grayscale image from disk and show
