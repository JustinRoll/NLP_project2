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
import abstractness, featureExtractor
from conceptmap import ConceptNetCollector

class Classifier:

    def __init__(self):
        pass


    def classifyFigurativeFeatures(self, pairs, folds=10, met_type="an", judge=None):
        #docs = [(pair, 'lit') for pair in literalPairs] + [(pair, 'fig') for pair in figPairs]
        if judge is None:
            docs = [(pair, pair.label) for pair in pairs]
        else:
            docs = [(pair, pair.judges[judge]) for pair in pairs]
            print("woo")
        print(docs[0])
        random.shuffle(docs)
        #print(docs)
        if met_type == "an":
            featureSets = [(featureExtractor.getAdjNounFigurativeFeatures(d),label) for (d, label) in docs]
        else:
            featureSets = [(featureExtractor.getSVOFeatures(d),label) for (d, label) in docs]    
        totalAcc = 0.0
        for i in range(folds):
            print("Fold", i)
            random.shuffle(featureSets)
            firstThird = int(len(featureSets)/3)
            test, train = featureSets[:firstThird], featureSets[firstThird:]
            classifier = SklearnClassifier(RandomForestClassifier(n_estimators=50), sparse=False).train(train)
            #classifier = SklearnClassifier(MultinomialNB()).train(train)
            #print(classifier.show_most_informative_features(20))
            acc = nltk.classify.accuracy(classifier,test)
            print("Acc", acc)
            totalAcc += acc
        return float(totalAcc)/folds
    
    not_used = """
    def classifyAdjNounFigurativeFeaturesString(self, literalPairs, figPairs):
        docs = [(pair, 'lit') for pair in literalPairs] + [(pair, 'fig') for pair in figPairs]
        random.shuffle(docs)
        #print(docs)
        featureSets = [(featureExtractor.getAdjNounFigurativeFeaturesString(d),label) for (d, label) in docs]
        firstThird = int(len(featureSets)/3)
        train, test = featureSets[:firstThird], featureSets[firstThird:]
        classifier = SklearnClassifier(RandomForestClassifier(), sparse=False).train(train)
        #classifier = SklearnClassifier(MultinomialNB()).train(train)
        #print(classifier.show_most_informative_features(20))
        return nltk.classify.accuracy(classifier,test)
        """

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
    

