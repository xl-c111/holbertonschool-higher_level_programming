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
        cursor.execute("SELECT * FROM states "      # add a space at the end when concatenating
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


"""
Syntax: cursor.execute(query, parameters)
        - parameters must be a sequence(tuple or list) or a dict
        - when the SQL uses %s placeholders, the parameters must be a tuple or a list
        e.g.,
            query = "SELECT * FROM states WHERE name = %s AND id = %s"
            params = ("Texas", 3)
            cursor.execute(query, params)
        - when the SQL uses %(name)s placeholders, the parameters must be a dict
        e.g.,
            query = "SELECT * FROM states WHERE name = %(state_name)s AND id = %(state_id)s"
            params = {"state_name": "Texas", "state_id": 3}
            cursor.execute(query, params)
"""
