#!/usr/bin/python3
"""
Adds the State object "Louisiana" to a MySQL database using SQLAlchemy ORM.
If exists, the script prints its id without inserting a duplicate.

Usage:
    ./11-model_state_insert.py <username> <password> <database>
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def add_a_state(username, password, database):
    """
    Adds 'Louisiana' to the states table if it doesn't exist;
    otherwise, prints its existing id.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    existing = session.query(State).filter(State.name == "Louisiana").first()
    if existing:
        print("{}".format(existing.id))
    else:
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()
        print("{}".format(new_state.id))

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <username> <password> "
              "<database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    add_a_state(username, password, database)
