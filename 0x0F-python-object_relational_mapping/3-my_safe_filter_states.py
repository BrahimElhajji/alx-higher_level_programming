#!/usr/bin/python3
""" script that takes in an argument anddisplays all values
in the states table of hbtn_0e_0_usawhere name matches the argument. """
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = %s \
                    ORDER BY id ASC", (sys.argv[4],))

    res = cursor.fetchall()

    for row in res:
        print(row)
    cursor.close()
    db.close()
