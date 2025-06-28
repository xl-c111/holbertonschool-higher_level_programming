#!/usr/bin/python3
"""
Fetches and displays all cities from a MySQL database,
along with their corresponding state names.

Usage:
    ./4-cities_by_state.py <username> <password> <database>
"""
import MySQLdb
import sys


def fetch_cities(username, password, database):
    """
    Connects to the MySQL database and prints all cities with their state
    names, ordered by city ID.
    """
    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()
        cursor.execute("""
                       SELECT cities.id, cities.name, states.name
                       FROM cities
                       JOIN states ON states.id = cities.state_id
                       ORDER BY cities.id ASC;
                       """)
        for row in cursor.fetchall():
            print(row)
    except MySQLdb.MySQLError as e:
        print("Database Error: {}".format(e))
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    fetch_cities(username, password, database)
