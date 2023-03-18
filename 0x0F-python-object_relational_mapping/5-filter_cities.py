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
    cities = sys.argv[4]
    cursor.execute("""SELECT cities.id cities.name states.name
                      FROM cities JOIN states ON cities.id WHERE
                      states.name LIKE %s ORDER BY cities.id ASC
                   """)
    rows = cursor.fetchall()
    value = list(row[0] for row in rows)
    print(*value, sep=", ")
    cursor.close()
    db.close()
