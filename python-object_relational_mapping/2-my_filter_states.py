#!/usr/bin/python3
"""
Script to display all values in the states table of hbtn_0e_0_usa
where name matches the argument passed.

Usage:
    ./2-my_filter_states.py <username> <password> <database> 'state_name'
"""
import MySQLdb
import sys


def get_states_by_name(username, password, database, state_name):
    """
    Connects to MySQL and fetches states where name matches the state_name.
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
        cursor.execute("SELECT * FROM states "
                       "WHERE BINARY name = %s "
                       "ORDER BY states.id ASC", (state_name,))
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
    if len(sys.argv) != 5:
        print(
            "Usage: ./2-my_filter_states.py <username> <password> <database> "
            "'state_name'"
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    get_states_by_name(username, password, database, state_name)
