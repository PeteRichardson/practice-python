#!/usr/bin/env python


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
    options = parser.parse_args()[0]
    return options.input_file, options.n


def print_report(items, input_file, item_type):
    '''dump the most popular items in a counter'''
    item_count = len(items)
    print "Top %d Popular %s in %s" % (item_count, item_type, input_file)
    for char, count in items:
        print "%7d: %s" % (count, char)


def top_n_items(input_file, n, strategy):
    ''' Do the real counting work.   This is the only
        function that knows we're using collections.Counter'''
    from collections import Counter

    items = Counter()
    for l in open(input_file, "r"):
            items.update(strategy.split_line(l.strip()))
    return items.most_common(n)


if __name__ == '__main__':
    file, n = get_options()
    counting_strategies = [Count_Chars, Count_Words]

    for counting_strategy in counting_strategies:
        items = top_n_items(file, n, counting_strategy)
        print_report(items, file, counting_strategy.item_type)
