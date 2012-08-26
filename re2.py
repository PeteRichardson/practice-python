#!/usr/bin/env python

from collections import Counter

n = 5
input_file = "/usr/share/dict/words"

words = Counter()
for l in open(input_file, "r"):
    words.update(l.strip())

print "Top %d Popular Chars in %s" % (n, input_file)
for word, count in words.most_common(n):
    print "%7d: %s" % (count, word)
