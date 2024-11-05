from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from db import engine, User
from shema import UserPydantic


Sessiona = sessionmaker(bind=engine)

session = Sessiona()

# def creat_user():
#     session.connection()

#     for i in range(100):
#         user = Users(name=f'Jil{i}', age=2+i, email=f'duck{i}@duck.com')
#         session.add(user)
#     session.commit()
#     print('Users add')

def list_users():
    all_users = session.query(User).all()
    for i in all_users:
        user_pydantic = UserPydantic.from_orm(i)
        print(user_pydantic.model_dump())

def add_user():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    email = input("Enter e-mail: ")
    user = User(name=name, age=age, email=email)
    session.add(user)
    session.commit()
    return print("User created")

def get_user():
    id = input("Enter id: ")
    data = session.scalar(select(User).filter_by(id = id))
    user_pydantic = UserPydantic.from_orm(data)
    return print(user_pydantic.model_dump())

def order_users():
    queri = session.execute(select(User.id, User.name, User.age).order_by(User.age))
    rez = queri.all()
    for i in rez:
        user_age = {'id': i[0], 'name': i[1], 'age': i[2]}
        print(user_age)