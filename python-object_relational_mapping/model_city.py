#!/usr/bin/python3
"""Defines a City class that links to the MySQL table `cities`
using SQLAlchemy ORM."""


from sqlalchemy.orm import declarative_base, relationship
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
state = relationship("State", back_populates="cities")

- state =: Defines a Python attribute on the City class.
           It represents the ORM-level link from a City object to its related State object.
           It can be accessed like: city_obj.state.name

- relationship("State", ...): "State" is the target class name.
           It tells SQLAlchemy that each City is linked to a State via a foreign key.

- back_populates="cities": Enables bidirectional access. The State class must define
           the other side of the relationship: cities = relationship("City", back_populates="state")
"""
