#!/usr/bin/python3
"""
Prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <mysql username>\
            <mysql password> <database name> <state name>")
        sys.exit(1)

    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured Session class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the State object with the given name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Display the result
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()    
