from app import app
from db import db
from models import Category, Product, Customer,Order,ProductOrder
import csv
from sqlalchemy import select,func
import random
from random import randint
from datetime import datetime as dt, timedelta

def create_tables():
    db.create_all()
    print("Tables created !.")

def drop_tables():
    db.drop_all()
    print("Tables dropped !.")

def import_data():
    print("Importing data one sec....")
    
    with open("/home/sameer/python_project/project/products.csv", mode="r") as file:
        product_reader = csv.DictReader(file)
        
        for row in product_reader:
            cat_name = row["category"]
            existing_category = db.session.execute(
                select(Category).where(Category.name == cat_name)
            ).scalar()

            if existing_category:
                category_obj = existing_category
            else:
                category_obj = Category(name=cat_name)
                db.session.add(category_obj)

            product_obj = Product(
                name = row["name"],
                price = float(row["price"]),
                available = int(row["available"]), 
                category = category_obj
            )
            db.session.add(product_obj)


    with open("/home/sameer/python_project/project/customers.csv", mode="r") as file:
        customer_reader = csv.DictReader(file)
        
        for row in customer_reader:
            customer_obj = Customer(
                name = row["name"],
                phone = row["phone"]
            )
            db.session.add(customer_obj)

    db.session.commit()
    print("Data is HERE !!!")

def generate_orders():
    
        for count in range(5): 
            
            random_customer = db.session.execute(
                select(Customer).order_by(func.random())
            ).scalar()
            
            if not random_customer:
                print("No customers found. Cannot generate orders.")
                return

            random_created_date = dt.now() - timedelta(
                days=randint(1, 3), 
                hours=randint(0, 15), 
                minutes=randint(0, 30)
            )

            new_order = Order(
                customer=random_customer,
                created=random_created_date
            )
            db.session.add(new_order) 

            num_prods = randint(4, 6)
            random_prods = db.session.execute(
                select(Product).order_by(func.random()).limit(num_prods)
            ).scalars()

            for product in random_prods:
                line_item = ProductOrder(
                    product=product,
                    quantity=randint(1, 10),
                    order=new_order
                )
                db.session.add(line_item)

        db.session.commit()
        print("Successfully generated 5 random orders.")

if __name__ == "__main__":
    with app.app_context():
        drop_tables()
        create_tables() 
        import_data()
        generate_orders()