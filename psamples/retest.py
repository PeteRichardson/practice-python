import re
from fileinput import FileInput

files = ["/usr/share/misc/flowers"]
p = re.compile("love")

for line in FileInput(files):
    if p.search(line):
        print line.strip()
