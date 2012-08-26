#!/usr/bin/env python

from collections import Counter


def count_chars(input_file):
    '''return a collections.Counter with char counts for the
       specified file'''
    chars = Counter()
    for l in open(options.input_file, "r"):
        chars.update(l.strip())
    return chars, "Chars"

def count_words(input_file):
    '''return a collections.Counter with word counts for the
       specified file'''
    words = Counter()
    for l in open(options.input_file, "r"):
        words.update(l.strip().split())
    return words, "Words"


def get_options():
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option('-n', dest="n", default=5, action="store")
    parser.add_option('-f', '--file', dest="input_file",
        default="/usr/share/dict/words", action="store")
    return parser.parse_args()


def print_report(char_counter, options, item_type):
    '''dump the most popular items in a counter'''
    print "Top %d Popular %s in %s" % (options.n, item_type, options.input_file)
    for char, count in char_counter.most_common(options.n):
        print "%7d: %s" % (count, char)

if __name__ == '__main__':
    options, args = get_options()
    items, item_type = count_chars(options.input_file)
    print_report(items, options, item_type)
    print "-----------------"
    items, item_type = count_words(options.input_file)
    print_report(items, options, item_type)
