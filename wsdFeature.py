import matcher
import nltk
from nltk.corpus import wordnet
from nltk.wsd import lesk
from nltk import word_tokenize

#Credit: http://stackoverflow.com/questions/15586721/wordnet-lemmatization-and-pos-tagging-in-python
def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return '' 

def getSenseLocs(words, sentence):
    senseLocs = {}
    token_sent = nltk.word_tokenize(sentence)
    positions = matcher.getPositions(words, token_sent)
    tagged = [(word, get_wordnet_pos(pos)) for word, pos in nltk.pos_tag(token_sent)]
    for key, value in positions.items():
        
        word = tagged[value][0]
        pos = tagged[value][1]
        #print(word)
        #print(pos)
        syns = wordnet.synsets(word, pos=pos)
        #print(syns)
        #print(token_sent)
        if len(syns) > 0:
            sense = lesk(token_sent, word, pos)
            if sense:
                senseLocs[str(pos)+"_senseLoc"] = syns.index(sense)
    return senseLocs

#words = ("breezy", "veranda")
#sentence = "Each has its own breezy veranda for a peaceful moment before starting your day."

#print(getSenseLocs(words, sentence))
    

