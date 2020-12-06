import cv2 as cv
import pytesseract
import sys
import webbrowser
import urlToImg
import extractAllImgWeb
import numpy as np
import atexit

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

UrlToScrap = input('Enter te URL - ')
WordWanted = input('Search a Word - ')
counterImgsFounded = 0

imgUrls = extractAllImgWeb(UrlToScrap)

for imgUrl in imgUrls:
    img = urlToImg(imgUrl)

    if img is None:
        continue

    resized = cv.resize(img, None, fx=1.2, fy=1.2,
                        interpolation=cv.INTER_CUBIC)
    gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    finalImg = cv.dilate(gray, kernel, iterations=1)
    finalImg = cv.erode(gray, kernel, iterations=1)

    cv.threshold(cv.GaussianBlur(finalImg, (5, 5), 0), 0, 255,
                 cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

    cv.threshold(cv.bilateralFilter(finalImg, 5, 75, 75), 0,
                 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

    cv.threshold(cv.medianBlur(finalImg, 3), 0, 255,
                 cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

    cv.adaptiveThreshold(cv.GaussianBlur(finalImg, (5, 5), 0), 255,
                         cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 31, 2)

    cv.adaptiveThreshold(cv.bilateralFilter(finalImg, 9, 75, 75), 255,
                         cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 31, 2)

    cv.adaptiveThreshold(cv.medianBlur(finalImg, 3), 255,
                         cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 31, 2)

    text = pytesseract.image_to_string(finalImg)

# ignore img without text

    if len(text) < 1:
        continue

    for word in text.split():

        if WordWanted.lower() in word.lower():

            # open in a browser the url of the imgs that contains the desired word
            webbrowser.open(imgUrl, new=0, autoraise=True)
            counterImgsFounded = counterImgsFounded + 1


def exit_handler():
    if(counterImgsFounded < 1):
        print('--Not found any images that contains "%s".--' % (WordWanted))
    else:
        print('--Founded % 2d images that contains "%s".--' %
              (counterImgsFounded, WordWanted))


atexit.register(exit_handler)
