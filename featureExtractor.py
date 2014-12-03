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
import abstractness

#get number of synsets, tagged POS, path similarity, conceptNet relations
#any other ideas?
def getAdjNounFigurativeFeatures(pair):
    featureDict = {}
    pairList = pair.split(" ")
    print(pairList)
    tags = pos_tag(word_tokenize(pair))
    adjSyns = synonyms(pairList[0], wn.ADJ) #these features suck. just an example
    nounSyns = synonyms(pairList[1], wn.NOUN)
    featureDict["adjSyns"] = len(adjSyns)
    featureDict["nounSyns"] = len(nounSyns)
    featureDict["adjAbs"] = abstractness.getAbstractness(pairList[0]) > .5
    featureDict["nounAbs"] = abstractness.getAbstractness(pairList[1]) > .5
    featureDict["adjImg"] = abstractness.getImageability(pairList[0]) > .5
    featureDict["nounImg"] = abstractness.getImageability(pairList[1]) > .5
    return featureDict
