#!/usr/bin/python3
"""python file that contains the class definition of a State
   python file that contains the class definition of a State
"""

import sys
from model_state import Base, States

from sqlalchemy import create_engine

if __name__ == "__main__":
     engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
     Base.metadata.create_all(engine)
