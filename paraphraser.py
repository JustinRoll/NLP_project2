from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn
from sys import argv

def tag(sentence):
  words = word_tokenize(sentence)
  words = pos_tag(words)
  return words

def paraphraseable(tag):
  #return tag.startswith('NN') or tag == 'VB' or tag.startswith('JJ')
  return True

def pos(tag):
  if tag.startswith('NN') or tag.startswith('VBN'):
    return wn.NOUN if len(wn.NOUN) > 0 else wn.ADJ
  elif tag.startswith('V'):
    return wn.VERB if len(wn.VERB) > 0 else wn.NOUN
  elif tag.startswith('J'):
      return wn.ADJ
  else:
    return wn.NOUN

def synonyms(word, tag):
  #print(wn.synsets(word, pos(tag)))
  e = [ss.lemmas() for ss in wn.synsets(word, pos(tag))]
  return set([lemma.name() for lemma in sum([ss.lemmas() for ss in wn.synsets(word, pos(tag))],[])])

def synonymIfExists(sentence):
  for (word, t) in tag(sentence):
    if paraphraseable(t):
      syns = synonyms(word, t)
      if syns:
        if len(syns) > 1:
          yield [word, list(syns)]
          continue
    yield [word, []]

def paraphrase(sentence):
  return [x for x in synonymIfExists(sentence)]

#if __name__ == '__main__':
#  sentence = "Biting cold"
 # print(pos_tag(word_tokenize(sentence)))
#  sentence = "Her raw intelligence was astounding"
#  print(pos_tag(word_tokenize(sentence))) 
#
#  print(paraphrase(sentence))
