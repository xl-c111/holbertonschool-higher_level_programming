#!/usr/bin/python3
"""
Fetches and lists all State objects from a MySQL database using SQLAlchemy.

Usage:
    ./7-model_state_fetch_all.py <username> <password> <database>
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_all_states(username, password, database):
    """
    Connects to the specified MySQL database and fetches all State objects.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc()).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py <username> <password> "
              "<database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    fetch_all_states(username, password, database)


"""
1, build database URL: dialect+driver://username:password@host:port/database
   - mysql+mysqldb: the dialect(mysql) and DBAPI(mysqldb)
   - username, password: used as user credentials
   - host:port: hostname and port
   - database: the name of database

"""
