#!/usr/bin/python3
"""
Deletes all State objects from a MySQL database whose name contains
the letter 'a', using SQLAlchemy ORM.

Usage:
    ./13-model_state_delete_a.py <username> <password> <database>
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_a_state(username, password, database):
    """
    Connects to the MySQL database and deletes all State objects
    whose name contains the letter 'a'.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).all()
    if not states:
        print("State with a name containing the letter 'a' does not exist.")
    else:
        for state in states:
            session.delete(state)
        session.commit()

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <username> <password> "
              "<database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    delete_a_state(username, password, database)
