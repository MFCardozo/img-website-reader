import extractTextToImage
import scrapWebImg
# imgPath = {'1.jpg', '2.jpeg', '3.png', '4.jpg', '5.jpg'}
# UrlToScrap = input('Enter te URL - ')
WordWanted = input('Search a Word - ')

# imgPath = scrapWebImg(UrlToScrap)


words = ''
# for path in imgPath:
words = words + extractTextToImage(
    'https://1.bp.blogspot.com/-IvBrs4FW2SM/X8twuT1i3vI/AAAAAAABpSM/YAkdYJg9h74ahSPQIOy-mz6GtUTHlRS2wCLcBGAsYHQ/s1024/Bolsa%2Bde%2BTrabajo%2BParaguay%2B5%2Bde%2BDiciembre%2Bde%2B2020.jpg', WordWanted)

mostAppearWords = dict()
# find the count on every word
for word in words.split():

    mostAppearWords[word] = mostAppearWords.get(word, 0) + 1

# Sort mostAppearWords by value
mostAppearWordsSorted = list()

for k, v in mostAppearWords.items():
    mostAppearWordsSorted.append((v, k))

mostAppearWordsSorted.sort(reverse=True)

for k, v in mostAppearWordsSorted:
    if v == WordWanted:
        print(k, v)
