#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <mysql username>\
            <mysql password> <database name>")
        sys.exit(1)

    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables defined in the metadata
    Base.metadata.create_all(engine)

    # Create a configured Session class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query and delete all State objects with a name containing 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)

    # Commit the session to persist the changes
    session.commit()
