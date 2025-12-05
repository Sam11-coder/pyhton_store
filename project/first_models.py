from sqlalchemy import String, DECIMAL, Integer,ForeignKey, select
from sqlalchemy.orm import mapped_column,DeclarativeBase,relationship

# base 
class Base (DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = "categories"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "Product"
    id = mapped_column(Integer,primary_key=True)
    name = mapped_column(String)
    price = mapped_column(DECIMAL(10, 2))
    available = mapped_column(Integer, default=0)
    category = mapped_column(String)
    category_id = mapped_column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")

class Customer(Base):
    __tablename__ = "Customer"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    phone = mapped_column(String,unique=True)

