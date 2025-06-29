#!/usr/bin/python3
"""
Fetches and displays all State objects that contain the letter 'a' from a MySQL
database using SQLAlchemy ORM.

Usage:
    ./9-model_state_filter_a.py <username> <password> <database>
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_state_with_a(username, password, database):
    """
    Connects to the specified MySQL database and fetches all State objects
    that contain the letter 'a'
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id.asc()).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./9-model_state_filter_a.py <username> <password> "
              "<database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    get_state_with_a(username, password, database)


"""
states = session.query(State).filter(State.name.like('%a%')).order_by(State.id.asc()).all()

- State: a SQLALchemy ORM model class --> represents 'states' table in the database

- State.name: column attributes (represents name column) defined on the model(for filtering and ordering)

- State.id.asc(): ASC order by id column 

- session.query(State): 
        - Syntax: session.query(obj)
        - create a SQL query obj for the State class
        - it doesn't run the query yet, it's just a query blueprint that you can later refine with .filter() .order_by()

- .like('%a%'): matches the string that contains 'a'
        - .like(...): string pattern matching method
        - '%a%': % means any chars, %a% means 'contains a' 

- .filter(...) WHERE clause

- .order_by(...) ORDER BY clause

- .all(): run the query and return a list of State insctances 
"""
