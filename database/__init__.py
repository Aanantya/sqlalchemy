from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .model import Task, User, Base

# creating a database connection
engine = create_engine('sqlite:///employee.db', echo=True)

# initializing the database
Base.metadata.create_all(bind=engine)

# creating session for transaction and query management
Session = sessionmaker(bind=engine)