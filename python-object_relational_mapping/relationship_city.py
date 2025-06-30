#!/usr/bin/python3
"""Defines a City class that links to the MySQL table `cities`
using SQLAlchemy ORM."""


from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """City class mapped to the MySQL table `cities`."""
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    # define a class attribute that represents the ORM level link from a City obj to its related State obj
    state = relationship("State", back_populates="cities")


"""
Base.metadata.create_all(engine): scan all ORM models that inherit from Base and 
                                  create corresponding tables in the database 

- Base: the declarative base class used to define ORM models
- Base.metadata: a container that holds all table metadata(table names, columns, constrains) collected from models
- .create_all(engine): create an actual table in the target database, using provided engine connection

"""
