from pathlib import Path

import cv2


def main():
    window_name = ('Sobel Demo - Simple Edge Detector')
    scale = 1
    delta = 0
    ddepth = cv2.CV_16S

    # Load the image
    img_path = str(Path(__file__).parent.parent / 'Images/cat.jpg')

    src = cv2.imread(img_path, cv2.IMREAD_COLOR)

    src = cv2.GaussianBlur(src, (3, 3), 0)

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    grad_x = cv2.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)

    grad_y = cv2.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)

    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)

    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    cv2.imshow(window_name, grad)
    cv2.waitKey(0)
    return 0


if __name__ == "__main__":
    main()
