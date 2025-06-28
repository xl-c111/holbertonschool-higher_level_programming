#!/usr/bin/python3
"""
This script connects to a MySQL database using credentials provided
via command-line arguments, retrieves all rows from the 'states' table
where the name starts with an uppercase 'N', and prints them ordered
by the 'id' column in ascending order.


Usage:
    ./1-filter_states.py <username> <password> <database>
"""
import MySQLdb
import sys


def fetch_states(username, password, database):
    """
    Connects to a MySQL database and prints all rows from the 'states' table
    where the state name starts with 'N', ordered by 'id' in ascending order.
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
        cursor.execute("""SELECT * FROM states
                       WHERE BINARY name LIKE 'N%'
                       ORDER BY states.id ASC""")
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
        print("Usage: ./1-filter_states.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    fetch_states(username, password, database)


"""
1, BINARY: force comparison to be case-sensitive by treating name as a binary
           string

WHERE name LIKE 'N%': select all names starting with n or N
WHERE BINARY name LIKE 'N%': select only names starting with uppercase 'N'
WHERE BINARY name LIKE 'n%': select only names starting with lowercase 'n'
"""
