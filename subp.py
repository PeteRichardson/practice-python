#!/usr/bin/env python

""" subp - demonstrates calling a subprocess """

import subprocess

COMMAND = ["/usr/bin/python -V"]

p = subprocess.Popen(COMMAND, shell=True, stdout=subprocess.PIPE)
stdout, stderr = p.communicate()
r = p.wait()