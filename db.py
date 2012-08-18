#!/usr/bin/env python

import sqlite3
import sys
import logging
from pprint import pformat

conn = sqlite3.connect('people.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS people (id int UNIQUE, name text, age int)''')
try:
	c.execute('''INSERT INTO people VALUES (1, 'pete',  46)''')
	c.execute('''INSERT INTO people VALUES (2, 'wendy', 45)''')
	conn.commit()
except sqlite3.IntegrityError as e:
	logging.error(pformat(e))

c.close()