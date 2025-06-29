#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)


"""
Base.metadata.create_all(engine): scan all ORM models that inherit from Base and 
                                  create corresponding tables in the database 

- Base: the declarative base class used to define ORM models
- Base.metadata: a container that holds all table metadata(table names, columns, constrains) collected from models
- .create_all(engine): create an actual table in the target database, using provided engine connection

"""
