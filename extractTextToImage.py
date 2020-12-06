import cv2 as cv
import pytesseract
import sys
import urlToImg
import scrapWebImg

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

UrlToScrap = input('Enter te URL - ')
WordWanted = input('Search a Word - ')


imgPaths = scrapWebImg(UrlToScrap)
checkWordInImg = False
for path in imgPaths:
    img = urlToImg(path)

    # extracting data from img
    heigthImg, widthImg, _ = img.shape
    boxes = pytesseract.image_to_data(img)

    for x, b in enumerate(boxes.splitlines()):
        # prevent null lines
        checkWordInImg = False

        if x != 0:
            b = b.split()

            # only we get the lines that have words and transforms for a better word lecture

            if len(b) == 12 and WordWanted.lower() in b[11].lower():
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 3)

    if(checkWordInImg):
        cv.imshow('result', img)
        cv.waitKey(500)

# return words


# sys.modules[__name__] = extractTextToImage
