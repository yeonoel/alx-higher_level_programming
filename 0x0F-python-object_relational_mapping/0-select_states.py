#!/usr/bin/python3
""" This script lists all states from database htbn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    [print(state) for state in cur.fetchall()]
