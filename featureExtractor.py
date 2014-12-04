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
import abstractness, vsmFeatures, wsdFeature

#get number of synsets, tagged POS, path similarity, conceptNet relations
#any other ideas?
def getAdjNounFigurativeFeatures(pair):
    featureDict = {}
    pairList = [pair.adj, pair.noun]
    
    print(pairList, pair.sentence)

    
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

    featureDict.update(wsdFeature.getSenseLocs((pair.adj, pair.noun), pair.sentence))
    return featureDict
