from sqlalchemy import create_engine, ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase, relationship

engine = create_engine(url='postgresql://postgres:664053@localhost/lessons')


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class User(Base):
    __tablename__ = "users"

    name: Mapped[str]
    age: Mapped[int]
    email: Mapped[str] = mapped_column(unique=True)

    producrs: Mapped[list["Products"]] = relationship(userlist=True, secondary="products_user", back_populates="user")

class Products(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[float]

    producrs: Mapped[list["User"]] = relationship(userlist=True, secondary="products_user", back_populates="products")

class Products_User(Base):
    __tablename__ = "products_user"

    User_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), primary_key=True)
    Product_id: Mapped[int] = mapped_column(ForeignKey("product.id", ondelet="CASCADE"), primary_key=True)
Base.metadata.create_all(engine)

