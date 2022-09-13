#!/usr/bin/python3

""" Define city model.
    inherits from Base (imported from model_state).
    links to the MySQL table cities.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents the table of city in MySQL database.

    __tablename__(str) : the table name to store states in databases.
    id (sqlalchemy.Integer) : id city.
    name (sqlalchemy.String) : city name.
    state_id (sqlalchemy.Integer) : state id like foreign key.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
