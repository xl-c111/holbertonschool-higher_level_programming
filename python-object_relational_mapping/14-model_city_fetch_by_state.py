#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa
using SQLAlchemy ORM, sorted by city ID.

Usage:
    ./14-model_city_fetch_by_state.py <username> <password> <database>


"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def fetch_city_by_state(username, password, database):
    """
    Connects to the MySQL database and prints all City objects,
    displaying their ID, name, and associated State name.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id.asc()).all()
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <username> <password> "
              "<database>")
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    fetch_city_by_state(username, password, database)
