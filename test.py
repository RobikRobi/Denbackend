from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

engine = create_engine(url='postgresql://postgres:664053@localhost/lessons')


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class User(Base):
    __tablename__ = "users"

    name: Mapped[str]
    age: Mapped[int]
    email: Mapped[str] = mapped_column(unique=True)

Base.metadata.create_all(engine)

Sessiona = sessionmaker(bind=engine)
session:Session = Sessiona()

user = User()

def list_users():
    data = session.scalars(select(Users))
    # data = user.model_dump()
    return print(data)

list_users()