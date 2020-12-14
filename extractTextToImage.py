import cv2 as cv
import pytesseract
import sys
import webbrowser
import urlToImg
import extractAllImgWeb
import numpy as np


def extractTextToImage(UrlToScrap, wordWanted):

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    counterImgsFounded = 0

    imgUrls = extractAllImgWeb(UrlToScrap)

    for imgUrl in imgUrls:

        img = urlToImg(imgUrl)

        if img is None:
            continue
        wResize = 1
        hResize = 1

        if img.shape[1] < 250:
            wResize = 1.5
            hResize = 1.5
        elif img.shape[1] > 599:
            wResize = .5
            hResize = .5

        resized = cv.resize(img, None, fx=wResize, fy=hResize,
                            interpolation=cv.INTER_CUBIC)
        # gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
        kernel = np.ones((1, 1), np.uint8)
        finalImg = cv.dilate(resized, kernel, iterations=1)
        finalImg = cv.erode(resized, kernel, iterations=1)

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

        text = pytesseract.image_to_string(
            finalImg)

    # ignore img without text

        if len(text) < 1:
            continue

        for word in text.split():

            if wordWanted.lower() in word.lower():

                # open in a browser the url of the imgs that contains the desired word
                webbrowser.open(imgUrl, new=0, autoraise=True)
                counterImgsFounded = counterImgsFounded + 1

    if(counterImgsFounded < 1):
        return'Not found any images that contains "{word}".'.format(word=wordWanted)
    else:
        return'Founded {counter} images that contains "{word}".'.format(counter=counterImgsFounded, word=wordWanted)


sys.modules[__name__] = extractTextToImage
