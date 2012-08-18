#!/usr/bin/env python

a = {}
for x in range(2,11,2):
	a[x] = " ".join(("foo", str(x)))

for k in sorted(a.keys()):
	print "%4d" % k
