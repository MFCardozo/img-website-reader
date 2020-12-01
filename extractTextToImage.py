import cv2 as cv
import pytesseract
import sys
import re


def extractTextToImage(imageFile):
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    img = cv.imread(imageFile)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    boxes = pytesseract.image_to_data(img)

    words = ''

    for x, b in enumerate(boxes.splitlines()):
        # prevent null lines

        if x != 0:
            b = b.split()

            # only we get the lines that have words
            if len(b) == 12 and re.search('\w', b[11]):

                words = words + b[11] + ' '

    return words


sys.modules[__name__] = extractTextToImage
