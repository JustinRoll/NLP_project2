from conceptmap import ConceptNetCollector
import pickle 
import time
import sys
import trofiparser
from nltk import bigrams, trigrams, ngrams
collector = ConceptNetCollector()


def getConceptNetScoresMaster(term1, term2):
    try:
        return getConceptNetScores(term1, term2)
    except:
        for i in range(0, 10):
            while True:

                time.sleep(5)
                try:
                    return getConceptNetScores(term1, term2)
                except:
                    e = sys.exc_info()[0]
                    print(e)
                    continue
                break

def getConceptNetNumrelationsMaster(term1, term2):
    try:
        return collector.countRelations(term1 + " " + term2)
    except:
        for i in range(0, 10):
            while True:

                time.sleep(5)
                try:
                    return collector.countRelations(term1 + " " + term2)
                except:
                    e = sys.exc_info()[0]
                    print(e)
                    continue
                break 



def getConceptNetScores(term1, term2):
    resultDict = collector.getAssociations(term1, term2).result
    resultScore = 0
    term1 = term1.replace("é", "e")
    term2 = term2.replace("é", "e")
    for assoc, item in resultDict.items():
        if item and item[0] and len(item[0]) > 1:
            if assoc == 'similar':
                for score in item:
                    resultScore += score[1]   
    return resultScore   


def getAllPairs(fileName):
    pairs = []
    file=open(fileName,'r') 

    text = file.readlines()

    for line in text:
        pairs.append(line.strip())
    return pairs

#class SVO:
#def __init__(self):
#        self.subject = ""
#        self.verb = ""
#        self.obj = ""
#        self.sentence = "" 
#        self.label = "" 

def svoMain():
    anList, svoList = trofiparser.parseTroFiCSV()
    numRelationsSavedDict = {}
    scoreSavedDict = {}
    for svo in svoList:
        svoList = []
        if svo.subject != "":
            svoList.append(svo.subject)
        if svo.verb != "":
            svoList.append(svo.verb)
        if svo.obj != "":
            svoList.append(svo.obj)
        bgrams = bigrams(svoList)
        for bgram in list(bgrams):
            relationScore = getConceptNetNumrelationsMaster(bgram[0], bgram[1])
            numRelationsSavedDict[" ".join(bgram)] =  relationScore
            scoreSavedDict[" ".join(bgram)] = getConceptNetScoresMaster(bgram[0], bgram[1])

    print(numRelationsSavedDict)
    print(scoreSavedDict)
    pickle.dump(numRelationsSavedDict, open( "SVORelationsResults.p", "wb" ))
    pickle.dump(scoreSavedDict, open("SVOScoresResults.p", "wb"))


def anmain():
    literalPairs = getAllPairs('data/adjnoun_fig.txt')
    figPairs = getAllPairs('data/adjnoun_lit.txt')
    savedDict = {}
    anPairs, svoPairs = trofiparser.parseTroFiCSV() 
    
    for pair in anPairs:
        print(pair.adj + " " + pair.noun)
        associationScore =  getConceptNetNumrelationsMaster(pair.adj, pair.noun)
        savedDict[pair.adj + " " + pair.noun] = associationScore
        print(associationScore)

    for pair in figPairs:
        pairList = pair.split(" ")
        print(pairList)
        associationScore = getConceptNetNumrelationsMaster(pairList[0], pairList[1])
        savedDict[pair] = associationScore
    for pair in literalPairs:
        pairList = pair.split(" ")
        print(pairList)
        associationScore = getConceptNetNumrelationsMaster(pairList[0], pairList[1])
        savedDict[pair] = associationScore
    pickle.dump(savedDict, open( "pairsRelationsResults.p", "wb" ))
    print(savedDict)
svoMain() 
