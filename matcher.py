import nltk
from nltk.stem.porter import *

def getPositions(words, sentence):
    positions = {}
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word).lower() for word in words if word[0] != "*"]
    stemmed_sentence = [stemmer.stem(word).lower() for word in sentence]
    for i in range(len(stemmed_sentence)):
        for j in range(len(stemmed_words)):
            if stemmed_sentence[i] == stemmed_words[j]:
                positions[words[j]] = i
    return positions


words = ["clear", "sky"]
sentence = nltk.word_tokenize("Clear blue skies are more common, and the air is fresher.")

print(getPositions(words, sentence))
                    
