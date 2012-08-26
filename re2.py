#!/usr/bin/env python

from collections import Counter


class Count_Chars():
    item_type = "Chars"

    @staticmethod
    def split_line(line):
        '''return chars in a line'''
        return line


class Count_Words():
    item_type = "Words"

    @staticmethod
    def split_line(line):
        '''return words in a line'''
        return line.split()


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


def count_items(input_file, strategy):
    items = Counter()
    for l in open(options.input_file, "r"):
        items.update(strategy.split_line(l.strip()))
    print_report(items, options, strategy.item_type)


if __name__ == '__main__':
    options, args = get_options()
    counting_strategies = [Count_Chars, Count_Words]

    for counting_strategy in counting_strategies:
        count_items(options.input_file, counting_strategy)
