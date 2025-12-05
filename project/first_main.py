from first_database import Session, engine
from first_models import Base,Product,Customer, Category
from sqlalchemy import select
import sys
import csv

def create_tables():
    Base.metadata.create_all(engine)
    print (f"All tables are created ")

def drop_table():
    Base.metadata.drop_all(engine)
    print(f"Data base is emtpy now")

def import_data():
    session = Session()
    with open("products.csv", mode="r") as file:
        product_reader = csv.DictReader(file)
        
        for row in product_reader:
            cat_name = row["category"]

            existing_category = session.execute(
                select(Category).where(Category.name == cat_name)
            ).scalar()

            if existing_category:
                category_obj = existing_category
            else:
                category_obj = Category(name=cat_name)
                session.add(category_obj)

            product_obj = Product(
                name = row["name"],
                price = float(row["price"]),
                available = int(row["available"]), 
                category = category_obj            
            )
            session.add(product_obj)

    with open ("customers.csv", mode="r") as file:
        customer = csv.DictReader(file)
        for row in customer:
            customer_obj = Customer(
                name = row["name"],
                phone = row["phone"]
            )

            session.add(customer_obj)
    print("all files are added to data base")
    session.commit()

        
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'import':
            import_data()

        elif sys.argv[1] == 'drop':
            drop_table()
        elif sys.argv[1] == 'create':
            create_tables()
    else:
        print("Please provide a command: import, drop, or create")
