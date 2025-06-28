#!/usr/bin/python3
"""
This script connects to a MySQL database using credentials provided
via command-line arguments, retrieves all rows from the 'states' table,
and prints them ordered by the 'id' column in ascending order.

Usage:
    ./0-select_states.py <username> <password> <database>

Arguments:
    username    MySQL username
    password    MySQL password
    database    Name of the database to connect to

Example:
    ./0-select_states.py root mypassword hbtn_0e_0_usa
"""
import MySQLdb
import sys


def fetch_states(username, password, database):
    """Connects to a MySQL database and prints all rows from the 'states' table
    ordered by the 'id' column in ascending order."""
    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()
        cursor.execute('SELECT * FROM states ORDER BY states.id ASC')
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
        print("Usage: ./0-select_states.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    fetch_states(username, password, database)
