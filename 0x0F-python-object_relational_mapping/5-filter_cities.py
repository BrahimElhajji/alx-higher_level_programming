#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa

"""
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    cursor = db.cursor()

    sql_query = "SELECT cities.id, cities.name FROM cities JOIN states \
                 ON cities.state_id = states.id WHERE \
                 states.name = %s ORDER BY cities.id ASC"

    cursor.execute(sql_query, (sys.argv[4],))

    res = cursor.fetchall()

    for row in res:
        print(", ".join(row[1] for row in res))

    cursor.close()
    db.close()
