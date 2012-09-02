#!/usr/bin/env python

import re
from pprint import pprint


fname = "changes.py"

pprint([l.strip() for l in open(fname, "r") if re.search("project", l)])

