#!/usr/bin/env python

from collections import Counter


def count_items(input_file, strategy):
    '''return a collections.Counter with item counts for the
       specified file, where items are parsed from a line
       using the given strategy funciton'''
    items = Counter()
    for l in open(options.input_file, "r"):
        items.update(strategy(l))
    return items


def count_chars(line):
    '''return a chars in a line'''
    return(line.strip())


def count_words(line):
    '''return words in a line'''
    return(line.strip().split())


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


def do_one_strategy(input_file, strategy, item_type):
    items = count_items(options.input_file, count_chars)
    print_report(items, options, item_type)


if __name__ == '__main__':
    options, args = get_options()
    for strategy, item_type in [(count_chars, "Chars"),
                                (count_words, "Words")]:
        do_one_strategy(options.input_file, strategy, item_type)
