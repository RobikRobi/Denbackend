from sqlalchemy import create_engine, ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase, relationship

engine = create_engine(url='postgresql://postgres:664053@localhost/lessons')


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    email: Mapped[str] = mapped_column(unique=True)

    product: Mapped[list["Products"]] = relationship(
            uselist=True, 
            secondary="products_user",
            back_populates="users")

class Products(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[float]

    users: Mapped[list["User"]] = relationship(
            uselist=True, 
            secondary="products_user",
            back_populates="product")

class Products_User(Base):
    __tablename__ = "products_user"

    User_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    Product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"), primary_key=True)


Base.metadata.create_all(engine)

