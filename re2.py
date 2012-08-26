#!/usr/bin/env python

from collections import Counter


words = Counter()
for l in open("changes.py", "r"):
    words.update(l.split())
for word, count in words.most_common(10):
    print "%4d: %s" % (count, word)
