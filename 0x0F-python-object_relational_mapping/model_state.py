#!/usr/bin/python3
"""python file that contains the class definition of a State
   python file that contains the class definition of a State
"""

from sqlalchemy import column, Integer, string
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('mysql:///localhost:3306')

Base = declarative_base()


class User(Base):
    """states class"""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
