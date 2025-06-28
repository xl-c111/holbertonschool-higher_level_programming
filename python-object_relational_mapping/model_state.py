#!/usr/bin/python3
"""Defines a State class that links to the MySQL table `states`
using SQLAlchemy ORM."""


from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String

# Base class for SQLAlchemy models
Base = declarative_base()


class State(Base):
    """State class mapped to the MySQL table `states`."""
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state")
