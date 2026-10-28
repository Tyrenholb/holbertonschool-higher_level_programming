#!/ure/bin/python3
"""Prints all city objects from database"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    search = session.query(State, City).join(
        City, State.id == City.state_id
        ).order_by(City.id.asc()).all()

    for state, city in search:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
