''' tokenizer2 -- use fileinput module to tokenize stuff 

    Seems to be much faster than tokenize.   Invoked with the following
    command line it only takes .5 seconds:

    time find ~/projects/practice/ -iname '*.py'  | xargs python tokenize2.py

    where as tokenize.py takes between 1 and 2 seconds!!!

'''

import fileinput
import nltk
from pprint import pprint

allwords = set()
tokenizer = nltk.tokenize.regexp.RegexpTokenizer('[.!\(\)\[\]*&^%=|\,\{\}\s\'\:\"]+', gaps=True)
for line in fileinput.input():
    allwords.update(tokenizer.tokenize(line))
pprint(allwords)
