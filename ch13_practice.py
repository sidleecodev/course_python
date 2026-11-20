# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:02:14 2026

@author: user
"""
import sqlite3
con = sqlite3.connect('school.db')
cur = con.cursor()

cur.execute("INSERT INTO stu VALUES(104001, 'Claire', 'B342222', '1245667')")
cur.execute('SELECT * FROM stu')
rows = cur.fetchall()
print(rows)
cur.close()