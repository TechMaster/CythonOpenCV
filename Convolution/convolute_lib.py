import cv2
import numpy as np


def convolve_nest_loop(img, kernel):
    img_height = img.shape[0]
    img_width = img.shape[1]

    kernel_height = kernel.shape[0]
    kernel_width = kernel.shape[1]

    H = (kernel_height - 1) // 2
    W = (kernel_width - 1) // 2

    out = np.zeros((img_height, img_width))

    for i in np.arange(H, img_height - H):
        for j in np.arange(W, img_width - W):
            sum = 0
            for k in np.arange(-H, H + 1):
                for l in np.arange(-W, W + 1):
                    a = img[i + k, j + l]
                    w = kernel[H + k, W + l]
                    sum += (w * a)
            out[i, j] = sum
    return out


# img and F are numpy matrices
def convolve_np(img, kernel):
    img_height = img.shape[0]
    img_width = img.shape[1]

    kernel_height = kernel.shape[0]
    kernel_width = kernel.shape[1]

    H = (kernel_height - 1) // 2
    W = (kernel_width - 1) // 2

    out = np.zeros((img_height, img_width))

    for i in np.arange(H, img_height - H):
        for j in np.arange(W, img_width - W):
            out[i, j] = np.tensordot(img[i - H:i + H + 1, j - W:j + W + 1], kernel, axes=((0, 1), (0, 1)))
    return out


'''
Khác với convolve_np, hàm này sẽ loại bỏ viền zero
'''


def convolve_np2(img, kernel):
    img_height = img.shape[0]
    img_width = img.shape[1]

    kernel_height = kernel.shape[0]
    kernel_width = kernel.shape[1]

    H = (kernel_height - 1) // 2
    W = (kernel_width - 1) // 2

    # Loại bỏ viền zero ở đây
    out = np.zeros((img_height - H * 2, img_width - W * 2))

    for i in np.arange(H, img_height - H):
        for j in np.arange(W, img_width - W):
            out[i - H, j - W] = np.tensordot(img[i - H:i + H + 1, j - W:j + W + 1], kernel, axes=((0, 1), (0, 1)))
    return out


'''
Khác với convolve_np3 ở chỗ có padding zero ở viền ảnh gốc để đảm bảo ảnh đầu ra không bị thu nhỏ
'''


def convolve_np4(img, kernel):
    img_height = img.shape[0]
    img_width = img.shape[1]

    kernel_height = kernel.shape[0]
    kernel_width = kernel.shape[1]

    H = (kernel_height - 1) // 2
    W = (kernel_width - 1) // 2

    out = np.zeros((img_height, img_width))

    img = cv2.copyMakeBorder(img, H, H, W, W, cv2.BORDER_REPLICATE)

    for i in np.arange(H, img_height + 1):
        for j in np.arange(W, img_width + 1):
            out[i - H, j - W] = np.tensordot(img[i - H:i + H + 1, j - W:j + W + 1], kernel, axes=((0, 1), (0, 1)))

    return out


# https://stackoverflow.com/questions/36243479/2dpooling-in-keras-doesnt-pool-last-column
def pool(img, w=2, h=2):
    img_height = img.shape[0]
    img_width = img.shape[1]
    new_height = int(img_height / h)
    new_width = int(img_width / w)
    out = np.zeros((new_height, new_width))

    for i in np.arange(0, new_height):
        for j in np.arange(0, new_width):
            top = i * h
            left = j * w
            out[i, j] = np.max(img[top:top + h, left: left + w])

    return out


def scale0_255(img):
    low = np.min(img)
    high = np.max(img)
    return np.array((img - low) * 255 / (high - low), dtype='uint8')
