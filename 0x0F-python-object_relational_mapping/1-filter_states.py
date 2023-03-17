#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)
   from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhos",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.arv[3],
            port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N' BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
