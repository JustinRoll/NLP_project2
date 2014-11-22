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


class Classifier:

    def __init__(self):
        pass
    #get number of synsets, tagged POS, path similarity, conceptNet relations
    #any other ideas?
    def getAdjNounFigurativeFeatures(self, pair):
        featureDict = {}
        pairList = pair.split(" ")
        print(pairList)
        tags = pos_tag(word_tokenize(pair))
        adjSyns = synonyms(pairList[0], wn.ADJ) #these features suck. just an example
        nounSyns = synonyms(pairList[1], wn.NOUN)
        featureDict["adjSyns"] = len(adjSyns)
        featureDict["nounSyns"] = len(nounSyns)
        return featureDict


    def classifyAdjNounFigurativeFeatures(self, literalPairs, figPairs):
        docs = [(pair, 'lit') for pair in literalPairs] + [(pair, 'fig') for pair in figPairs]
        random.shuffle(docs)
        #print(docs)
        featureSets = [(self.getAdjNounFigurativeFeatures(d),label) for (d, label) in docs]
        firstThird = int(len(featureSets)/3)
        train, test = featureSets[:firstThird], featureSets[firstThird:]
        classifier = SklearnClassifier(MultinomialNB()).train(train)
        #print(classifier.show_most_informative_features(20))
        return nltk.classify.accuracy(classifier,test) 


    def incrementDictCount(self, item, incDict):
        if item in incDict:
                incDict[item] += 1
        else:
                incDict[item] = 1        


   
    def getAverages(self, function):
        accuracyTotal = 0.0
        accuracies = []
        for i in range(0, 5):
            rmse, accuracy = function()
            accuracies.append(accuracy)
            accuracyTotal += accuracy
            rmseTotal += rmse
        print(accuracies)
        return accuracyTotal / 5.0
    

