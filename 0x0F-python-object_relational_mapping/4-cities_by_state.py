#!/usr/bin/python3
"""This script lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities INNER JOIN states\
                ON state_id = states.id ORDER BY id ASC")
    cities = cur.fetchall()
    for citie in cities:
        print(citie)
    cur.close()
    db.close()
