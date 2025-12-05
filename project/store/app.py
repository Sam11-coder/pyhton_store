from flask import Flask, render_template,url_for,request,redirect
from pathlib import Path
from db import db
from models import Product,Category,Customer,Order,ProductOrder
from sqlalchemy import select

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"

app.instance_path = Path(".").resolve()


db.init_app(app)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/products")
def product():

    statement = select(Product).order_by(Product.name)
    records = db.session.execute(statement)
    new_record = records.scalars()
    
    return render_template("products.html", products=new_record)


@app.route("/category")
def category():

    statement = select(Category).order_by(Category.name)
    records = db.session.execute(statement)
    new_record = records.scalars()
    
    return render_template("category.html", categories=new_record)

@app.route("/customer")
def customer():

    statement = select(Customer).order_by(Customer.name)
    records = db.session.execute(statement)
    new_record = records.scalars()
    
    return render_template("customer.html", customers=new_record)


@app.route("/categories/<string:name>")
def catagories(name):
    caty = select(Category).where(Category.name == name)
    new_caty = db.session.execute(caty).scalar()
    return render_template("category_detail.html", category=new_caty)

@app.route("/customers_id/<int:id>")

def customer_id(id):
    cus_id = select(Customer).where(Customer.id == id)
    new_cus_id = db.session.execute(cus_id).scalar()
    return render_template("customer_id.html", customer=new_cus_id)


@app.route("/orders")
def orders():
    orders = select(Order).order_by(Order.created)
    new_order = db.session.execute(orders).scalars()
    return render_template("order.html",orders=new_order)


@app.route("/orders/<int:id>")
def order_detail(id):
    order_detail = select(Order).where(Order.id == id)
    new_order_detail = db.session.execute(order_detail).scalar()
    return render_template("order_detail.html", order=new_order_detail)


@app.route("/orders/<int:id>/complete", methods=["POST"])
def complete_order(id):
    order = db.session.execute(select(Order).where(Order.id == id)).scalar()
    
    if order is None:
        return render_template("error.html", message="Order not found."), 404
        
    try:
        order.complete()
        
        db.session.add(order)
        db.session.commit()
        
        return redirect(url_for("order_detail", id=id))

    except ValueError as e:
        db.session.rollback()
        return render_template("error.html", message=str(e)), 409




if __name__ == "__main__":
    app.run(debug=True, port=8888)