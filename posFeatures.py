import matcher
import nltk

def getPartOfSpeechData(words, sentence):
    data = {}
    token_sent = nltk.word_tokenize(sentence)
    positions = matcher.getPositions(words, token_sent)
    tagged = nltk.pos_tag(token_sent)
    if words[0] in positions.keys():
        firstPos = positions[words[0]]
    else:
        firstPos = 0
    if words[-1] in positions.keys():
        lastPos = positions[words[-1]]
    else:
        lastPos = len(token_sent)
    #print(tagged)
    if firstPos == 0:
        data["beforeFirst"] = "None"
    else:
        data["beforeFirst"] = tagged[firstPos-1][1]
    if lastPos >= len(token_sent)-1:
        data["afterLast"] = "None"
    else:
        data["afterLast"] = tagged[lastPos+1][1]
    return data

#words = ("breezy", "veranda")
#sentence = "Each has its own breezy veranda for a peaceful moment before starting your day."

#print(getPartOfSpeechData(words, sentence))
