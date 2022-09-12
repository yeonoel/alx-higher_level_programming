#!/usr/bin/python3
""" This script that takes in an argument and
    displays all values in the states table o
    f hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id""")
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]
