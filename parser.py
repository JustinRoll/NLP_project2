import re
from nltk import bigrams, trigrams, ngrams
from nltk.tokenize import word_tokenize, sent_tokenize 
from nltk.corpus import stopwords, wordnet
import csv

class ANPair:
    def __init__(self):
        self.adj = ""
        self.noun = ""
        self.label = ""
        self.sentence = ""
    def __str__(self):
        return "adj: %s noun: %s label: %s sentence: %s" % (self.adj, self.noun, self.label, self.sentence)
class SVO:
    def __init__(self):
        self.subject = ""
        self.verb = ""
        self.obj = ""
        self.sentence = "" 
        self.label = ""
    def __str__(self):
        return "subject: %s verb: %s object: %s label:%s sentence: %s" % (self.subject, self.verb, self.obj, self.label, self.sentence) 

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

def parseTroFiCSV():
    ANList = []
    SVOList = []

    with open('data/LIT_AN_EN.csv', newline='', encoding="utf8") as csvfile:
        dataReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in dataReader:
            newAn = ANPair()
            adj = row[5]
            noun = row[6]
            sentence = row[7].replace('\xa0', ' ')
            newAn.adj = adj
            newAn.noun = noun
            newAn.sentence = sentence
            newAn.label = "L"
            ANList.append(newAn)

    with open('data/MET_AN_EN.csv', newline='', encoding="utf8") as csvfile:
        dataReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in dataReader:
            newAn = ANPair()
            adj = row[5]
            noun = row[6]
            sentence = row[7].replace('\xa0', ' ')
            newAn.adj = adj
            newAn.noun = noun
            newAn.sentence = sentence
            newAn.label = "M"
            ANList.append(newAn) 


    with open('data/LIT_SVO_EN.csv', newline='', encoding="utf8") as csvfile:
        dataReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in dataReader:
            newSvo = SVO()
            subject = row[5]
            verb = row[6]
            obj = row[7]
            sentence = row[8].replace('\xa0', ' ')
            newSvo.subject = subject 
            newSvo.verb = verb
            newSvo.obj = obj
            newSvo.label = "L"
            newSvo.sentence = sentence
            SVOList.append(newSvo) 

    with open('data/MET_SVO_EN.csv', newline='', encoding="utf8") as csvfile:
        dataReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in dataReader:
            newSvo = SVO()
            subject = row[5]
            verb = row[6]
            obj = row[7]
            sentence = row[8].replace('\xa0', ' ')
            newSvo.subject = subject 
            newSvo.verb = verb
            newSvo.obj = obj
            newSvo.label = "M"
            newSvo.sentence = sentence
            SVOList.append(newSvo) 

    return ANList, SVOList
#anList, svoList = parseTroFiCSV()

#for an in anList:
#    print(an)

#for svo in svoList:
#    print(svo)
    #for line in text:
#    line = re.sub(r"wsj[0-9]*:[0-9]*", "", line)
#    print(line)
#    #wsj06:1157
