''' filter.py - a grep-like tool. 

    takes a pattern and a list of files '''

import fileinput
import re
import sys
import glob 

pattern = ".*"+sys.argv[1]+".*"

for line in fileinput.input(sys.argv[2:]):
    if re.match(pattern, line):
        print "{0:20}: {1}".format(fileinput.filename(), line.strip())
