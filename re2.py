#!/usr/bin/env python

from collections import Counter
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-n', dest="n", default=5, action="store")
parser.add_option('-f', '--file', dest="input_file",
    default="/usr/share/dict/words", action="store")
options, args = parser.parse_args()

words = Counter()
for l in open(options.input_file, "r"):
    words.update(l.strip())

print "Top %d Popular Chars in %s" % (options.n, options.input_file)
for word, count in words.most_common(options.n):
    print "%7d: %s" % (count, word)
