# Python - Object-relational mapping

This is a Python-based ORM (Object-Relational Mapping) project that allows users to interact with a database using Python classes and objects. This project uses the SQLAlchemy library for database connectivity and management. ALSO(SQLdb)

## Installation
To install this project, you can either clone the repository or download the source code as a zip file.
```
git clone https://github.com/your_username/python-orm-project.git
```
After cloning the repository, you can create a virtual environment and install the dependencies using pip.
```
cd python-orm-project
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Usage
To use this project, you need to create a database and configure the connection settings in config.py. You can use any database supported by SQLAlchemy (such as MySQL, PostgreSQL, SQLite, etc.).

Once you have configured the database connection settings, you can define your models in models.py. A model is a Python class that represents a table in the database. You can define the columns of the table as attributes of the class.

Here's an example of a simple model:
```
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
```
To interact with the database using this model, you can use the Session object provided by SQLAlchemy. Here's an example:
```
from sqlalchemy.orm import sessionmaker
from models import User
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

session = Session()

# Create a new user
user = User(name='John', email='john@example.com')
session.add(user)
session.commit()

# Query all users
users = session.query(User).all()
for user in users:
    print(user.name, user.email)
```
For more information on how to use SQLAlchemy and create models, please refer to the [official documentation](https://docs.sqlalchemy.org/en/14/orm/)

