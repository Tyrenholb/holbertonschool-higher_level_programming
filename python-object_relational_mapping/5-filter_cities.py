#!/usr/bin/python3
"""takes an arguement lists all cities of that state hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name "
        "FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id;",
        (sys.argv[4],)
    )
    listr = [city[0] for city in cursor.fetchall()]
    result = ", ".join(listr)
    print(result)
    cursor.close()
    db.close()
