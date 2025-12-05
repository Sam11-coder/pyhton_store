from db import db
from sqlalchemy import String, DECIMAL, Integer,ForeignKey, select,func
from sqlalchemy.orm import mapped_column,DeclarativeBase,relationship

class Category(db.Model):
    __tablename__ = "categories"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    products = relationship("Product", back_populates="category")


class Product(db.Model):
    __tablename__ = "Product"
    id = mapped_column(Integer,primary_key=True)
    name = mapped_column(String)
    price = mapped_column(DECIMAL(10, 2))
    available = mapped_column(Integer, default=0)
    category = mapped_column(String)
    category_id = mapped_column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")

class Customer(db.Model):
    __tablename__ = "Customer"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    phone = mapped_column(String,unique=True)
    orders = db.relationship('Order', back_populates='customer')
    def get_pending_orders(self):
        return [order for order in self.orders if order.completed is None]

    def get_completed_orders(self):
        return [order for order in self.orders if order.completed is not None]



class Order(db.Model):
    __tablename__ = "Order"
    id = db.mapped_column(Integer, primary_key=True, autoincrement=True)
    customer_id = mapped_column(Integer, ForeignKey("Customer.id"))
    customer = relationship("Customer",back_populates="orders")
    amount = mapped_column( DECIMAL,default=0)
    created = mapped_column(db.DateTime,default=func.now())
    completed = mapped_column(db.DateTime)
    items = relationship("ProductOrder")
    def estimate(self):
        new_estimate = 0
        for item in self.items:
            new_estimate +=  item.quantity * item.product.price    

        return round(new_estimate, 2)

    def complete(self):
        for item in self.items:
            if item.product.available < item.quantity:
                raise ValueError("We dont have enough")
            else:
                item.product.available =- item.quantity
        self.completed = db.func.now()
        self.amount = round(self.estimate(), 2)        

class ProductOrder(db.Model):
    __tablename__ = "ProductOrder"    
    product_id = mapped_column(
        Integer, 
        ForeignKey("Product.id"), 
        primary_key=True
    )
    product = relationship("Product") 
    order_id = mapped_column(
        Integer, 
        ForeignKey("Order.id"), 
        primary_key=True
    )
    order = relationship("Order", back_populates="items") 

    quantity = mapped_column(Integer)