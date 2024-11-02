from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase


engine = create_engine(url='postgresql://postgres:664053@localhost/lessons')


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class Users(Base):
    __tablename__ = "users"

    name: Mapped[str]
    age: Mapped[int]
    email: Mapped[str] = mapped_column(unique=True)

Base.metadata.create_all(engine)

