import string

for line in open("/usr/share/misc/flowers", "r").readlines():
    if line[0] == '#':
        continue
    (flower, meaning) = line.strip().split(":")
    if "," in flower:
        (fname, fadjective) = flower.split(",", 1)
        fadjective = string.capwords(fadjective.strip().replace(",", ""))
        if fadjective:
            fname = " ".join([fadjective, fname])
        flower = fname
    print "'{0}' means '{1}'".format(flower, meaning)
