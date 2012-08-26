#!/usr/bin/env python

import re
import hashlib
from collections import defaultdict


words = defaultdict(int)
for l in open("changes.py", "r"):
    #if re.search("project\.", l):
    l = l.strip()
    for token in l.split():
        words[token] += 1
    hash = hashlib.sha1(l)
    print hash.hexdigest(), l
print "-------------------------------"
for word in sorted(words, key=words.get, reverse = True):
    print "%4d: %s" % (words[word], word)
