#!/usr/bin/python3
"""Defines a State class that links to the MySQL table `states`
using SQLAlchemy ORM."""


from sqlalchemy.orm import relationship
from relationship_city import City
from sqlalchemy import Column, Integer, String
from model_state import Base


class State(Base):
    """State class mapped to the MySQL table `states`."""
    # tell SQLALchmy which table this class maps to
    __tablename__ = "states"

    # id, name: class attributes mapped to table columns
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state",
                          cascade="all, delete")
