import extractTextToImage

imgPath = {'1.jpg', '2.jpeg'}
words = ''
for path in imgPath:
    words = words + extractTextToImage(path)

# for word in words.split():
print(words.split())
