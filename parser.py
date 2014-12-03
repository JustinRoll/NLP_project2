import re
from nltk import bigrams, trigrams, ngrams
from nltk.tokenize import word_tokenize, sent_tokenize 
from nltk.corpus import stopwords, wordnet

def parseTroFi(fileName):

    f = open(fileName)
    text = "\n".join(f.readlines())

    clusters = text.split(r"********************")
    wordDict = {} #word dict will contain a word mapping to a list of tuples containing the sentence and label

    for cluster in clusters:
        leadWordGroup = re.search(r"\*\*\*([a-z]+)\*\*\*", cluster)
        if (leadWordGroup):
            leadWord = leadWordGroup.group(1)
            if leadWord not in wordDict:
                wordDict[leadWord] = []
            for line in cluster.split("\r\n"):
                if "wsj" in line: 
                    labelGroup = re.search(r"wsj[0-9]*:[0-9]*[ \n\t]+(L|N)", cluster) 
                    if labelGroup:
                        label = labelGroup.group(1)
                    sentenceGroup = re.search(r"wsj[0-9]*:[0-9]*[ \n\t]+(L|N)[ \n\t]+(.*)", cluster)  
                    if sentenceGroup and labelGroup:
                        tokenizedSent = [word for word in word_tokenize(sentenceGroup.group(2)) if ',' not in word and '.' not in word]
                        wordDict[leadWord].append( (tokenizedSent, label))
                        #print("label: %s sentence: %s" % (label, sentenceGroup.group(2)))

    return wordDict
#print(parseTroFi("TroFiExampleBase.txt"))
    #for line in text:
#    line = re.sub(r"wsj[0-9]*:[0-9]*", "", line)
#    print(line)
#    #wsj06:1157
