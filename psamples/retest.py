import re
from fileinput import FileInput
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-p', dest="pattern", action="store")
parser.add_option('-i', action="store_true")
options = parser.parse_args()[0]

flags = re.IGNORECASE if options.i else 0

files = ["/usr/share/misc/flowers"]
p = re.compile(options.pattern, flags)

for line in FileInput(files):
    if p.search(line):
        print line.strip()
