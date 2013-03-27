''' imports.py - find all imports and list the 20 most frequent '''

import os
import sys
from collections import Counter
import logging
import re
import mmap
import contextlib


def get_file_list(top):
    for (root, _, files) in os.walk(top):
        for filename in files:
            (basename, ext) = os.path.splitext(filename)
            if ext.lower() == ".py":
                yield os.path.join(root, filename)


def imports_from_file(filename):
    logging.debug("# parsing {}".format(filename))
    if not os.stat(filename).st_size:
        return []

    f = open(filename, "r+")
    with contextlib.closing(mmap.mmap(f.fileno(), 0)) as mapped_file:
        results = [tup[0] or tup[1] for tup in re.findall(r"from\s+(\w+)\s+import|import\s+(\w+)", mapped_file)]
    return results


def main(top):
    counter = Counter()
    assert os.path.exists(top), "# FATAL ERROR: {top} doesn't exist!"
    for filename in get_file_list(top):
        logging.debug("# parsing {}".format(filename))
        assert os.path.exists(filename), "# FATAL ERROR: {filename} doesn't exist!"
        imports = imports_from_file(filename)
        counter.update(imports)
    print counter.most_common(5)
    return 0


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    sys.exit(main("/Users/pete/projects/practice/"))
