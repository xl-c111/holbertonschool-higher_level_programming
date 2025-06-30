#!/usr/bin/python3
"""
Lists all State objects and their associated City objects
from a MySQL database using SQLAlchemy ORM.

Usage:
    ./101-relationship_states_cities_list.py <username> <password> <database>


"""
import sys
from model_state import Base
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_all_State_and_City_objs(username, password, database):
    """Connects to the MySQL database and lists all State and City objects."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc()).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py <username> "
              "<password> <database>")
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_all_State_and_City_objs(username, password, database)
