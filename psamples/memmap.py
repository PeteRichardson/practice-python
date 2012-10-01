#!/usr/bin/env python

''' memmap.py - mmap sample'''

import mmap
import contextlib

FILE = open("changes.txt", "r+")

# Use contextlib to automatically close the file when it's done
with contextlib.closing(mmap.mmap(FILE.fileno(),
                                 0, prot=mmap.PROT_READ)) as mapped_file:
    FILE_SIZE = mapped_file.size()
    while mapped_file.tell() < FILE_SIZE:
        print mapped_file.readline().strip()
