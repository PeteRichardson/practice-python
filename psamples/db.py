#!/usr/bin/env python

'''Sample code for creating a sqlite3 db in python'''

import sqlite3
import logging
from pprint import pformat

def create_db():
    '''simple function to demonstrate creating a sqlite3 db'''
    conn = sqlite3.connect('people.db')

    curs = conn.cursor()

    curs.execute('''CREATE TABLE IF NOT EXISTS people 
        (id int UNIQUE, name text, age int)''')
    try:
        curs.execute('''INSERT INTO people VALUES (1, 'pete',  46)''')
        curs.execute('''INSERT INTO people VALUES (2, 'wendy', 45)''')
        conn.commit()
    except sqlite3.IntegrityError as err:
        logging.error(pformat(err))

    curs.close()


if __name__ == "__main__":
    create_db()
