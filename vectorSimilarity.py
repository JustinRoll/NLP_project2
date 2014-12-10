import matcher
import nltk
import vsmFeatures

def getVectorSimilarity(words, sentence):
    similarities = {}
    token_sent = nltk.word_tokenize(sentence)
    positions = matcher.getPositions(words, token_sent)
    filtered_sent = [token_sent[i] for i in range(len(token_sent)) if i not in positions.values()]
    filtered_sent = [word.lower() for word in filtered_sent if word.isalpha()]
    sent_vects = [vsmFeatures.getVector(word) for word in filtered_sent]
    sent_vects = [vect for vect in sent_vects if len(vect) > 0]
    avgVector = []
    for vect in sent_vects:
        if len(avgVector) == 0:
            avgVector = vect
        else:
            for i in range(len(vect)):
                avgVector[i] += vect[i]
    avgVector = [float(item)/len(sent_vects) for item in avgVector]
    for i in range(len(words)):
        word = words[i]
        wordVector = vsmFeatures.getVector(word)
        if len(wordVector) > 0 and len(avgVector) > 0:
            for j in range(len(wordVector)):
                 dist = wordVector[j] - avgVector[j] + 1 #ensure non-negative
                 similarities["word"+str(i)+"vecFeat"+str(j)] = dist
    return similarities


def getAverageVector(sentence):
    token_sent = nltk.word_tokenize(sentence)
    sent_vects = [vsmFeatures.getVector(word) for word in token_sent]
    sent_vects = [vect for vect in sent_vects if len(vect) > 0]
    avgVector = []
    for vect in sent_vects:
        if len(avgVector) == 0:
            avgVector = vect
        else:
            for i in range(len(vect)):
                avgVector[i] += vect[i]
    avgVector = [float(item)/len(sent_vects) for item in avgVector]
    dic = {}
    for i in range(len(avgVector)):
        dic["AvgVect"+str(i)] = avgVector[i]
    return dic

#words = ("breezy", "veranda")
#sentence = "Each has its own breezy veranda for a peaceful moment before starting your day."

#print(getAverageVector(sentence))
