#!/usr/bin/python3
"""
Lists all cities of a given state from the database.

Usage:
    ./5-filter_cities.py <username> <password> <database> 'state_name'
"""
import MySQLdb
import sys


def get_cities_by_state(username, password, database, state_name):
    """
    Fetches and prints city names of a given state, ordered by city ID.
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
        cursor.execute(
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "JOIN states ON states.id = cities.state_id "
            "WHERE BINARY states.name = %s "
            "ORDER BY cities.id ASC", (state_name,)
        )
        cities = [row[1] for row in cursor.fetchall()]
        print(", ".join(cities))
    except MySQLdb.MySQLError as e:
        print("Database Error: {}".format(e))
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <username> <password> "
              "<database> 'state_name'")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    get_cities_by_state(username, password, database, state_name)


"""
1, cities = [row[1] for row in cursor.fetchall()]
   - cursor.fetchall() retrieves all rows returned by the last SQL query. it returns a list of tuple
   - for loop iterates each row (which is a tuple)
   - row[1] refers to the second column in each row(index 1), which is city's name 
   - cities = [] collects all cities'name into a new list
   
2, (", ".join(cities))
   Syntax: "separator".join(list) ---> returns a single string made by joining all elements of the list using the given seperator
   e.g.,  ", ".join(['New York', 'Los Angeles', 'Chicago'])
   Output: 'New York, Los Angeles, Chicago'


"""
