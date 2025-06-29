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


# Step-by-Step Execution of city.state.name

"""
1, load a City obj from the database, e.g., city = session.query(City).filter_by(name="Austin").first()
   now the python obj will look like: <City id=1, name='Austin', state_id=5> (at this point, city.state not loaded yet)

2, access city.state
   city.state: is a State obj, established via the relationship('State') ORM mapping

   what happens internally:
   - SQLAlchemy sees the City obj has a relationship("State")
   - it looks at city.state_id (which is 5) 
   - it will automatically issues this SQL query behind scenes: SELECT * FROM states WHERE id = 5;
   - it returns a State obj, e.g., <State id=5, name='Texas'>
   - SQLAlchemy caches this result as city.state

3, access city.state.name: simply access the .name attribute of the cached State obj
   city.state.name: state name as a string, access the name field of the associated State instance


"""

# Visual Flow
"""
1. city.state_id == 5
       │
       ▼
2. SQLAlchemy runs:
   SELECT * FROM states WHERE id = 5
       │
       ▼
3. Loads State(id=5, name="Texas")
       │
       ▼
4. city.state.name → "Texas"

"""
