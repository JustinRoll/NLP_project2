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
#get number of synsets, tagged POS, path similarity, conceptNet relations
#any other ideas?

collector = ConceptNetCollector()
pickledPairs = pickle.load(open("pairs.p", "rb")) 

def getConceptNetScores(term1, term2):
    for assoc, item in resultDict.items():
        if item and item[0] and len(item[0]) > 1:
            if assoc == 'similar':
                for score in item:
                    resultScore += item[0][1]  
 
    except:
        print("throttled")
        
    return resultScore  

def getAdjNounFigurativeFeatures(pair):
    featureDict = {}
    pairList = pair.split(" ")
    associationScore = pickledPairs[pair] 
    print("%s score: %f" % (str(pairList), associationScore))
    

    featureDict["association_score"] = associationScore-1
    tags = pos_tag(word_tokenize(pair))
    adjSyns = synonyms(pairList[0], wn.ADJ) #these features suck. just an example
    nounSyns = synonyms(pairList[1], wn.NOUN)
    #featureDict["adjSyns"] = len(adjSyns)
    #featureDict["nounSyns"] = len(nounSyns)
    adjVsm  = vsmFeatures.getVector(pairList[0])
    nounVsm = vsmFeatures.getVector(pairList[1])
    if len(adjVsm) > 0:
        for i in range(len(adjVsm)):
            featureDict["adjVsm"+str(i)] = adjVsm[i]

    if len(nounVsm) > 0:
        for i in range(len(nounVsm)):
            featureDict["nounVsm"+str(i)] = nounVsm[i]
    
    featureDict["adjAbs"] = abstractness.getAbstractness(pairList[0]) #> .5
    featureDict["nounAbs"] = abstractness.getAbstractness(pairList[1]) #> .5
    featureDict["adjImg"] = abstractness.getImageability(pairList[0]) #> .5
    featureDict["nounImg"] = abstractness.getImageability(pairList[1]) #> .5
    return featureDict
