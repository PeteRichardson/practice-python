''' filter.py - a grep-like tool. 

    takes a pattern and a list of files '''

import fileinput
import re
import sys
import optparse


parser = optparse.OptionParser()
parser.add_option('-p', action="store", dest="pattern")
options, remainder = parser.parse_args(sys.argv)

for line in fileinput.input(remainder):
    if re.match(options.pattern, line):
        print "{0:20}: {1}".format(fileinput.filename(), line.strip())
