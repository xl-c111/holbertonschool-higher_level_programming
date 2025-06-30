#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
in a MySQL database using SQLAlchemy ORM.

Usage:
    ./100-relationship_states_cities.py <username> <password> <database>


"""
import sys
from model_state import Base
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_a_state_with_city(username, password, database):
    """Connects to the MySQL database and adds a new State and City
    using SQLAlchemy."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # create all tables in the database that are defined by your models
    # associated with Base if thet don't exist
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    session.add(new_state)
    session.commit()

    # create a City obj with name and linked state
    new_city = City(name="San Francisco", state=new_state)
    session.add(new_city)
    session.commit()

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <username> "
              "<password> <database>")
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    create_a_state_with_city(username, password, database)


"""
state=new_state: assign the state relationship of the city to a State obj(named new_state)
                 City has a Foreign_key(state_id) and a relationship to State
                 this line will establish the ORM link between new_state and new_city
                 
"""
