#!/usr/bin/python3
"""
Updates the name of the State object with given id in a MySQL database
using SQLAlchemy ORM.

Usage:
    ./12-model_state_update_id_2 <username> <password> <database>
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def update_a_state(username, password, database):
    """
    Updates the name of the State object with given id.
    If the object does not exist, prints an informative message.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
    else:
        print("State with id 2 does not exist.")
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2 <username> <password> "
              "<database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    update_a_state(username, password, database)
