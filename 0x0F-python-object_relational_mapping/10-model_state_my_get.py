#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy.orm import sessionmaker
from model_state import State
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3],
                                   pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()

    test = False
    for state in session.query(State).order_by(State.id):
        if sys.argv[4] == state.name:
            print("{}".format(state.id))
            test = True
    if test is False:
        print("Not found")
