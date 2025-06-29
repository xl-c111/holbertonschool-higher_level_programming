#!/usr/bin/python3
"""
Fetches and displays the ID of the State object from a MySQL database
(using SQLAlchemy ORM) where the state's name matches the provided name.

Usage:
    ./10-model_state_my_get.py <username> <password> <database> 'state_name'
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_state_by_name(username, password, database, state_name):
    """
    Connects to the specified MySQL database and searches for a State object
    whose name matches the given `state_name`.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()
    if not state:
        print("Not found")
        return
    print("{}".format(state.id))

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <username> <password> "
              "<database> 'state_name'")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    get_state_by_name(username, password, database, state_name)
