import nltk
from nltk import load_parser
parser = load_parser('grammars/large_grammars/atis.cfg', trace=0)
#problem: this grammar is not big enough
#try stat parser at https://github.com/emilmont/pyStatParser
sentence = 'big car'
tokens = sentence.split()
for tree in parser.parse(tokens):
    print(tree)
