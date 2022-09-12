#!/usr/bin/python3
"""
    Define State model .
    nherits from Base
    links to the MySQL table states
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Represents a the Table of state in MySQL database

    __tablename__ (str): the table name to store states in database
    id (sqlalchemy.Integer): the id od a state
    name (sqlalchemy.String): the name of the a state.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
