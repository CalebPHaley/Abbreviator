#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE WORDS
         (
         ABRV           TEXT    NOT NULL,
         Long            TEXT     NOT NULL);''')
print("Table created successfully")

conn.close()