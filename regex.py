#!/usr/bin/env python
''' script to search for regex matching lines in a file '''

import re
from pprint import pprint


FILENAME = "changes.txt"

pprint([l.strip() for l in open(FILENAME, "r") if re.search("project", l)])

