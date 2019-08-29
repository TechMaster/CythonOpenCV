import cv2
from pathlib import Path

img_path = str(Path(__file__).parent.parent / 'Images/african_leopard_low.jpg')


# -----Reading the image-----------------------------------------------------
img = cv2.imread(img_path, 1)
cv2.imshow("img", img)

# -----Converting image to LAB Color model-----------------------------------
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("lab", lab)

# -----Splitting the LAB image to different channels-------------------------
l, a, b = cv2.split(lab)
cv2.imshow('l_channel', l)
cv2.imshow('a_channel', a)
cv2.imshow('b_channel', b)

# -----Applying CLAHE to L-channel-------------------------------------------
clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
cl = clahe.apply(l)
cv2.imshow('CLAHE output', cl)

# -----Merge the CLAHE enhanced L-channel with the a and b channel-----------
limg = cv2.merge((cl, a, b))
cv2.imshow('limg', limg)

# -----Converting image from LAB Color model to RGB model--------------------
final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
cv2.imshow('final', final)
cv2.waitKey(0)
cv2.destroyAllWindows()
