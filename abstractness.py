import nltk
absConDict = {}
imgDict = {}

def loadWords():
    f = open("data/abstractness.predictions")
    for line in f.readlines():
        parts = line.split()
        absConPair = (parts[1], float(parts[3][:-1]), float(parts[5][:-1]))
        absConDict[parts[0]] = absConPair
    f.close()
    
    f = open("data/imageability.predictions")
    for line in f.readlines():
        parts = line.split()
        imgPair = (parts[1], float(parts[3][:-1]), float(parts[5][:-1]))
        imgDict[parts[0]] = imgPair
    f.close()
    

def getAbsConDict():
    if absConDict == {}:
        loadWords()
    return absConDict

def getImgDict():
    if imgDict == {}:
        loadWords()
    return imgDict

    
def getAbstractness(word):
    dic = getAbsConDict()
    if word in dic.keys():
        return dic[word][1]
    else:
        return -.1

def getImageability(word):
    dic = getImgDict()
    if word in dic.keys():
        return dic[word][1]
    else:
        return -.1

def getSentenceAbstractness(sentence):
     total = 0
     count = 0
     for word in nltk.word_tokenize(sentence):
         abstr = getAbstractness(word)
         if abstr > 0:
             total += abstr
             count += 1
     if count > 0:
         return float(total)/count
     else:
         return -.1

def getSentenceImageability(sentence):
     total = 0
     count = 0
     for word in nltk.word_tokenize(sentence):
         abstr = getImageability(word)
         if abstr > 0:
             total += abstr
             count += 1
     if count > 0:
         return float(total)/count
     else:
         return -.1

