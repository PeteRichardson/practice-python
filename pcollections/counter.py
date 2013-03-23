from collections import Counter

c = Counter()
c.update("pete")
print [(x,y) for x,y in sorted(c.items())]
