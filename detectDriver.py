from classifier import *
from tagger import *

def getAllPairs(fileName):
    pairs = []
    file=open(fileName,'r') 

    text = file.readlines()

    for line in text:
        pairs.append(line.strip())
    return pairs

def main():
    literalPairs = getAllPairs('data/adjnoun_fig.txt')
    figPairs = getAllPairs('data/adjnoun_lit.txt')
    classifier = Classifier()
    print("Overall Score Average accuracy: %f" % (classifier.classifyAdjNounFigurativeFeatures(literalPairs, figPairs)))
main() 
