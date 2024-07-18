'''
    The database_model.py file constructs the model structure for querying
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Creating the declarative
Base = declarative_base()

# Defining Users
class User(Base):
    __tablename__='users'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'{self.id}\t{self.name}'
    
    # Establishing relation with tasks model
    tasks = relationship('Task', back_populates='users')

# Defining Tasks
class Task(Base):
    __tablename__='tasks'
    id = Column('id', Integer, primary_key=True)
    description = Column('description', String)
    user_id = Column('user_id', Integer, ForeignKey('users.id'))

    def __init__(self, id, description, user_id):
        self.id = id
        self.description = description
        self.user_id = user_id

    def __repr__(self):
        return f'{self.id}\t{self.description}\t{self.user_id}'

    # Establishing relationship to user model
    users = relationship('User', back_populates='tasks')
