from pprint import pprint
import nltk.tokenize.regexp
import os
import contextlib
import mmap
import sys

def get_file_list(top):
    for (root, _, files) in os.walk(top):
        for filename in files:
            (basename, ext) = os.path.splitext(filename)
            if ext.lower() == ".py":
                yield os.path.join(root, filename)


def parse_one_file_small(filename, tokenizer):
    words = set()
    if os.stat(filename).st_size:
        f = open(filename, "r+")
        with contextlib.closing(mmap.mmap(f.fileno(), 0)) as mapped_file:
            words.update(tokenizer.tokenize(mapped_file))
    return words


def parse_one_file(filename, tokenizer):
    words = set()
    if os.stat(filename).st_size:
        for line in open(filename, "r").readlines():
            words.update(tokenizer.tokenize(line))
    return words

def main(top):
    assert os.path.exists(top), "# FATAL ERROR: No such path as {top}"
    allwords = set()
    tokenizer = nltk.tokenize.regexp.RegexpTokenizer('[.!\(\)\[\]*&^%=|\,\{\}\s\'\:\"]+', gaps=True)
    for filename in get_file_list(top):
        filewords = parse_one_file_small(filename, tokenizer)
        allwords |= set(filewords)
    pprint(allwords)
    return 0

if __name__ == '__main__':
    top = "/Users/pete/projects/practice/"
    sys.exit(main(top))
