#!/usr/bin/python3
"""script that takes in the name of a state and lists all cities"""


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM cities INNER JOIN states
                      ON states.id=cities.state_id WHERE
                      states.name=%s""", (sys.argv[4]))
    rows = cursor.fetchall()
    value = list(row[0] for row in rows)
    print(*value, sep=", ")
    cursor.close()
    db.close()
