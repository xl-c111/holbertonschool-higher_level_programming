#!/usr/bin/python3
"""
Fetches and displays the first State object from a MySQL database
using SQLAlchemy ORM.

Usage:
    ./8-model_state_fetch_first.py <username> <password> <database>
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_first_state(username, password, database):
    """
    Connects to the specified MySQL database and fetches the first State object
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id.asc()).first()
    if not state:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py <username> <password> "
              "<database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    fetch_first_state(username, password, database)
