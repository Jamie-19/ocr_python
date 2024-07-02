import cv2
import numpy as np


def image_conv(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    cv2.imwrite('preprocessed_image.png', thresh)
    return 'preprocessed_image.png'