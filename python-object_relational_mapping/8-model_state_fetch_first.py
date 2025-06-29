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
    # create a SQLalchemy engine to connect to a local MySQL database using mysqldb driver
    # pool_pre_ping=True  checks the connection before using it to avoid timeout errors
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    # create a session factory class
    Session = sessionmaker(bind=engine)
    # create an actual session obj
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


# Workflow
"""
1, define a ORM model using __tablename__ and column attributes

2, create an engine using create_engine()
   - build the database URL: dialect+driver://username:password@host:port/database
       - mysql+mysqldb: the dialect(mysql) and DBAPI driver(mysqldb)
       - username, password: used as user credentials
       - host:port: hostname and port
       - database: the name of database

3, bind the session class via Session = sessionmaker(bind=engine)
   - Session = sessionmaker(bind=engine): create a session factory class
   - session = Session(): create a concrete session instance

4, use .query()+.filter()+.order_by()+.all() to construct queries

5, use all() or first() to fetch results 

6, session.close() to end the session
"""
