from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from db import engine, Users
from shema import User


Sessiona = sessionmaker(bind=engine)

session:Session = Sessiona()


def list_users():
    data = session.scalars(select(Users))
    return print(data.all())

def add_user():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    email = input("Enter e-mail: ")
    user = Users(name=name, age=age, email=email)
    session.add(user)
    session.commit()
    return print("User created")

def get_user():
    id = input("Enter id: ")
    data = session.scalar(select(Users).filter_by(id = id))
    return print(data.__dict__)

def order_users():
    data = session.execute(select(Users).order_by (Users.age))
    return print(data.all())