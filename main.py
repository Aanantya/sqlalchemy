'''
This main.py file handles the database query and transaction via session
'''
from database import Session, Task, User

session = Session()

#create new users
user1 = User(1, 'Alice')
user2 = User(2, 'Bob')
user3 = User(3, 'Charlie')
user4 = User(4, 'David')

session.add(user1)
session.add(user2)
session.add(user3)
session.add(user4)
session.commit()

task1 = Task(1, 'Debug the existing code.', user1.id)
task2 = Task(2, 'Troubleshoot the errors.', user1.id)
task3 = Task(3, 'DB query with sqlalchemy.', user2.id)
task4 = Task(4, 'Write hello world program.', user2.id)
task5 = Task(5, 'Create query document', user3.id)

session.add(task1)
session.add(task2)
session.add(task3)
session.add(task4)
session.add(task5)
session.commit()

# Implementing queries

# Get all users
results = session.query(User).all()
for result in results:
    print(result)

# Get user by id
result = session.query(User).get(1)
print(result)

# Get user by name = Bob
result = session.query(User).filter_by(name = 'Bob').all()
print(result)

# Get user by name starting with 'A'
result = session.query(User).filter(User.name.startswith('A')).all()
print(result)

# Get all tasks
results = session.query(Task).all()
for result in results:
    print(result)

# Order tasks by the user id
result = session.query(Task).order_by(Task.user_id).all()
print(result)

# Group tasks by user id
result = session.query(Task.description).group_by(Task.user_id).all()
print(result)

# Join User with Task
result = session.query(User, Task.description).join(User).all()
print(result)

# Update Task description
task = session.query(Task).get(5)
task.description = 'Document queries'
session.commit()

# Update using Atomic transaction
task = session.query(Task).get(5)
try:
    session.begin()
    # update
    task.description = 'Document all queries'
    session.commit()
except:
    # rollback if error occured
    session.rollback()

# Delete user by id
user = session.query(User).filter(User.id == 4).delete()
session.commit()

# Get all users
results = session.query(User).all()
for result in results:
    print(result)
