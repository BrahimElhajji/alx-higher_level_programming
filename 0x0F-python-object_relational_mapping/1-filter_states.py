#!/usr/bin/python3
""" script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    res = cursor.fetchall()

    for row in res:
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close
