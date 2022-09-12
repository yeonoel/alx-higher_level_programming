#!/usr/bin/python3
"""This script lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id\
                ORDER BY cities.id ASC")
    search = cur.fetchall()
    text = [citie[2] for citie in search if citie[4] == argv[4]]
    print(', '.join(text))
    cur.close()
    db.close()
