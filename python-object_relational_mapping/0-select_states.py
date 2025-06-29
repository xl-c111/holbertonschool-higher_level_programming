#!/usr/bin/python3
"""
This script connects to a MySQL database using credentials provided
via command-line arguments, retrieves all rows from the 'states' table,
and prints them ordered by the 'id' column in ascending order.

Usage:
    ./0-select_states.py <username> <password> <database>

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


# Workflow
"""
1, Connect to database Using MySQLdb.connect(
    host, port, user, passwd, db, charset
)

2, create a cursor obj used to execute SQL statement
Syntax: cursor_obj = db.cursor()

3, execute raw SQL query using cursor.execute(query)

4, fetch data using cursor.fetchall()
- fetchall(): retrieve all remaining rows of a query result at once
              each row is returened as a tuple
              all rows are return as a list of tuple
- fetchone(): fetch the next single row as tuple
- fetchmany(n): fetch next n rows(as a list of tuple)

5, close cursor and database using cursor.close() and db.close()

"""
