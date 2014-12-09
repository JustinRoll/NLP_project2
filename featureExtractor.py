from sklearn.naive_bayes import MultinomialNB
from nltk.classify.scikitlearn import SklearnClassifier
import random,operator,nltk
import functools
from nltk.corpus import udhr
from nltk import bigrams, trigrams, ngrams
from nltk.tokenize import word_tokenize, sent_tokenize 
from nltk.corpus import stopwords, wordnet
from nltk.stem.snowball import SnowballStemmer
from tagger import *
from sklearn.ensemble import RandomForestClassifier
import abstractness, vsmFeatures
from conceptmap import ConceptNetCollector
import pickle
import abstractness, vsmFeatures, wsdFeature, posFeatures, vectorSimilarity
import babynames


#get number of synsets, tagged POS, path similarity, conceptNet relations
#any other ideas?

collector = ConceptNetCollector()
pickledPairs = pickle.load(open("data/ANPairScoresResults.p", "rb"))

pickledSvoRelations = pickle.load(open( "data/SVORelationsResults.p", "rb"))
pickledSvoScores = pickle.load(open( "data/SVOScoresResults.p", "rb"))
babyNames = babynames.extract_names("data/baby1994.html")


#for item, value in pickledSvoRelations.items():
#    print("%s : %f" % (item, value))

#for item, value in pickledSvoScores.items():
#    print("%s : %f" % (item, value)) 

def isName(subject):
    if subject in babyNames:
        return True
    else:
        return False


#for item, score in pickledSvoScores.items():
#    pair = item.split(" ")

#    if isName(pair[0]) or isName(pair[1]):
#        print("NAME in %s %s" % (pair[0], pair[1])) 

def getConceptNetScores(term1, term2):
    resultDict = collector.getAssociations(term1, term2).result
    resultScore = 0
    for assoc, item in resultDict.items():
        if item and item[0] and len(item[0]) > 1:
            if assoc == 'similar':
                for score in item:
                    resultScore += score[1]   
    return resultScore  

def getAdjNounFigurativeFeaturesString(pairString):
    featureDict = {}
    pairList = pairString.split(" ")
    print(pairList)
    if " ".join(pairList) in pickledPairs:
        associationScore = pickledPairs[" ".join(pairList)]
        print(associationScore)
        featureDict["association_score"] = associationScore
    tags = pos_tag(word_tokenize(" ".join(pairList)))
    
    adjVsm  = vsmFeatures.getVector(pairList[0])
    nounVsm = vsmFeatures.getVector(pairList[1])
    #if len(adjVsm) > 0:
    #    for i in range(len(adjVsm)):
    #        featureDict["adjVsm"+str(i)] = adjVsm[i]

    #if len(nounVsm) > 0:
    #    for i in range(len(nounVsm)):
    #        featureDict["nounVsm"+str(i)] = nounVsm[i]
    
    #featureDict["adjAbs"] = abstractness.getAbstractness(pairList[0]) #> .5
    #featureDict["nounAbs"] = abstractness.getAbstractness(pairList[1]) #> .5
    #featureDict["adjImg"] = abstractness.getImageability(pairList[0]) #> .5
    #featureDict["nounImg"] = abstractness.getImageability(pairList[1]) #> .5

    return featureDict 


def getAdjNounFigurativeFeatures(pair):
    featureDict = {}
    pairList = [pair.adj, pair.noun]
    #if " ".join(pairList) in pickledPairs:
    #    associationScore = pickledPairs[" ".join(pairList)]
    #    print(associationScore)
    #    featureDict["association_score"] = associationScore
    #tags = pos_tag(word_tokenize(" ".join(pairList)))
    print(pairList, pair.sentence)
    
    #adjVsm  = vsmFeatures.getVector(pairList[0])
    #nounVsm = vsmFeatures.getVector(pairList[1])
    #if len(adjVsm) > 0:
    #    for i in range(len(adjVsm)):
    #        featureDict["adjVsm"+str(i)] = adjVsm[i]

    #if len(nounVsm) > 0:
    #    for i in range(len(nounVsm)):
    #        featureDict["nounVsm"+str(i)] = nounVsm[i]
    
    featureDict["adjAbs"] = abstractness.getAbstractness(pairList[0]) #> .5
    featureDict["nounAbs"] = abstractness.getAbstractness(pairList[1]) #> .5
    featureDict["adjImg"] = abstractness.getImageability(pairList[0]) #> .5
    featureDict["nounImg"] = abstractness.getImageability(pairList[1]) #> .5

    abstr = abstractness.getSentenceAbstractness(pair.sentence)
    img = abstractness.getSentenceImageability(pair.sentence)
    if abstr > 0:
        featureDict["totAbstr"] = abstr
    if img > 0:
        featureDict["totImg"] = img

    #featureDict.update(vectorSimilarity.getVectorSimilarity((pair.adj, pair.noun), pair.sentence))
    #featureDict.update(vectorSimilarity.getAverageVector(pair.sentence))
    #featureDict.update(wsdFeature.getSenseLocs((pair.adj, pair.noun), pair.sentence))
    #featureDict.update(posFeatures.getPartOfSpeechData((pair.adj, pair.noun), pair.sentence))
    return featureDict
