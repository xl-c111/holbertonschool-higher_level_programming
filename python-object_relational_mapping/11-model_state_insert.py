#!/usr/bin/python3
"""
Adds the State object "Louisiana" to a MySQL database using SQLAlchemy ORM.
If exists, the script prints its id without inserting a duplicate.

Usage:
    ./11-model_state_insert.py <username> <password> <database>
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def add_a_state(username, password, database):
    """
    Adds 'Louisiana' to the states table if it doesn't exist;
    otherwise, prints its existing id.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # this queries the states table for the first row where name is 'Louisiana'
    # .first() returns a single State obj if found
    existing = session.query(State).filter(State.name == "Louisiana").first()
    if existing:
        print("{}".format(existing.id))
    else:
        # create a new State obj, assign the string 'Louisiana' to its name attribute
        # equals to State.name = 'Louisiana'
        new_state = State(name="Louisiana")
        # add this new State obj to the session, staging it for insertion into database
        session.add(new_state)
        # commit all pending changes in the session. The new State obj is saved in the database, id will be generated automatically
        session.commit()
        print("{}".format(new_state.id))

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <username> <password> "
              "<database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    add_a_state(username, password, database)


"""
State(name = 'Louisiana') means:
- State.__init__() is called
- internally: self.name = 'Louisiana' is set
- equals to new_state.name = "Louisiana"
"""
