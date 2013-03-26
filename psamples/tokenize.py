import glob
from pprint import pprint
import nltk.tokenize.regexp


def parse_one_file(filename, tokenizer):
    words = set()
    for line in open(filename, "r").readlines():
        words.update(tokenizer.tokenize(line))
        #words.update(nltk.word_tokenize(line))
    return words

allwords = set()
tokenizer = nltk.RegexpTokenizer('[.!\(\)\[\]*&^%=|\,\{\}\s\'\:\"]+', gaps=True)
for filename in glob.glob("*.py"):
    filewords = parse_one_file(filename, tokenizer)
    allwords |= set(filewords)
pprint(allwords)
