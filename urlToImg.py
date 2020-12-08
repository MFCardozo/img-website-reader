import sys
import cv2 as cv
from urllib.request import urlopen
import numpy as np


def urlToImg(url, readFlag=cv.IMREAD_GRAYSCALE):

    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv.imdecode(image, readFlag)

    # return the image
    return image


sys.modules[__name__] = urlToImg
