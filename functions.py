from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from db import engine, User, Products
from shema import UserPydantic, ProductPydantic
import random

Sessiona = sessionmaker(bind=engine)

session = Sessiona()

# def creat_user():
#     session.connection()

#     for i in range(100):
#         user = Users(name=f'Jil{i}', age=2+i, email=f'duck{i}@duck.com')
#         session.add(user)
#     session.commit()
#     print('Users add')

# функция для получения списка всех пользователей
def list_users():
    all_users = session.query(User).all()
    for i in all_users:
        user_pydantic = UserPydantic.from_orm(i)
        print(user_pydantic.model_dump())

# функция для добавления пользователя в базу данных
def add_user():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    email = input("Enter e-mail: ")
    user = User(name=name, age=age, email=email)
    session.add(user)
    session.commit()
    return print("Product added")

# функция для получения пользователя по его id
def get_user():
    id = input("Enter id: ")
    data = session.scalar(select(User).filter_by(id = id))
    user_pydantic = UserPydantic.from_orm(data)
    return print(user_pydantic.model_dump())

# функция для получения списка пользователей по возрасту
def order_users():
    queri = session.execute(select(User.id, User.name, User.age).order_by(User.age))
    rez = queri.all()
    for i in rez:
        user_age = {'id': i[0], 'name': i[1], 'age': i[2]}
        print(user_age)

# def creat_product():
#     session.connection()
#     list_product = ["SmartTV", "PC", "Fridge", "Kettle", "Microwave", "Headphones", "Monitor"]
#     for i in range(10):
#         name_product = random.choice(list_product)
#         product = Product(name=f'{name_product+str(i)}', price=float(1000+i))
#         session.add(product)
#     session.commit()
#     print('Product creat')

# функция для добавления продукта в базу данных
def add_product():
    name = input("Enter name product: ")
    price = float(input("Enter price: "))
    product = Products(name=name, price=price)
    session.add(product)
    session.commit()
    return print("Product added")

# функция для получения списка всех продуктов
def list_product():
    all_products = session.query(Products).all()
    for i in all_products:
        product_pydantic = ProductPydantic.from_orm(i)
        print(product_pydantic.model_dump())

# функция для обновления данных продукта по его id
def update_product():
    id = int(input("Enter product id to change: "))
    product = session.get(Products, id)
    if product:
        product.name = input("Enter a new product name: ")
        product.price = float(input("Enter a new price for the product: "))
        data = session.scalar(select(Products).filter_by(id = id))
        product_pydantic = ProductPydantic.from_orm(data)
        return session.commit(), print(product_pydantic.model_dump()), print("Changes made11")
    return print("Product with this id was not found")

def product_to_profiel():
    user_id = int(input())
    product_id = int(input("Enter the id of the product you want to add: "))
    user = session.scalar(select(User)).where(User.id == user_id)
    products = session.scalar(select(Products).where(Products.id == product_id))
    user.products.append(products)
    session.commit()
    return print("Product added to profile")

# update_product()
# list_product()
product_to_profiel()