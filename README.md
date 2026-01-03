# Flask E-Commerce Store

A full-stack e-commerce administration application built with Python and Flask. This system manages products, customers, and processes orders with inventory tracking.

## 🚀 Features

* **Product Management:** Browse products and categories.
* **Customer Profiles:** View customer details and their full transaction history.
* **Order Processing:**
    * View detailed order manifests.
    * **Transactional Logic:** "Complete Order" button that deducts inventory and finalizes the sale.
    * **Stock Safety:** Prevents transactions if inventory is insufficient (custom error handling).
* **Database:** Complex SQL relationships (Many-to-Many) using SQLAlchemy and SQLite.
* **Management Script:** CLI tool to generate realistic test data.

## 🛠️ Technology Stack

* **Backend:** Python, Flask
* **Database:** SQLite, SQLAlchemy ORM
* **Frontend:** HTML5, Jinja2 Templates, CSS3

## ⚙️ Setup & Installation

1.  **Clone the project:**
    ```bash
    git clone <your-repo-url>
    cd store
    ```

2.  **Create and Activate a Virtual Environment:**
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # Mac/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If you don't have a requirements file yet, install manually: `pip install flask sqlalchemy flask-sqlalchemy`)*

4.  **Initialize the Database:**
    Run the management script to wipe the DB and generate fresh data:
    ```bash
    python manage.py
    ```

## 🏃‍♂️ How to Run

1.  Start the Flask server:
    ```bash
    python app.py
    ```
2.  Open your browser and navigate to:
    `http://127.0.0.1:8888`

## 📂 Project Structure

* `app.py` - Main application entry point and routes.
* `models.py` - Database classes (User, Product, Order) and business logic.
* `manage.py` - Script for database creation and data seeding.
* `templates/` - HTML files (Jinja2).
* `static/` - CSS files and images.
* `instance/store.db` - The SQLite database file.# Flask E-Commerce Store

A full-stack e-commerce administration application built with Python and Flask. This system manages products, customers, and processes orders with inventory tracking.

## 🚀 Features

* **Product Management:** Browse products and categories.
* **Customer Profiles:** View customer details and their full transaction history.
* **Order Processing:**
    * View detailed order manifests.
    * **Transactional Logic:** "Complete Order" button that deducts inventory and finalizes the sale.
    * **Stock Safety:** Prevents transactions if inventory is insufficient (custom error handling).
* **Database:** Complex SQL relationships (Many-to-Many) using SQLAlchemy and SQLite.
* **Management Script:** CLI tool to generate realistic test data.

## 🛠️ Technology Stack

* **Backend:** Python, Flask
* **Database:** SQLite, SQLAlchemy ORM
* **Frontend:** HTML5, Jinja2 Templates, CSS3

## ⚙️ Setup & Installation

1.  **Clone the project:**
    ```bash
    git clone <your-repo-url>
    cd store
    ```

2.  **Create and Activate a Virtual Environment:**
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # Mac/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If you don't have a requirements file yet, install manually: `pip install flask sqlalchemy flask-sqlalchemy`)*

4.  **Initialize the Database:**
    Run the management script to wipe the DB and generate fresh data:
    ```bash
    python manage.py
    ```

## 🏃‍♂️ How to Run

1.  Start the Flask server:
    ```bash
    python app.py
    ```
2.  Open your browser and navigate to:
    `http://127.0.0.1:8888`

## 📂 Project Structure

* `app.py` - Main application entry point and routes.
* `models.py` - Database classes (User, Product, Order) and business logic.
* `manage.py` - Script for database creation and data seeding.
* `templates/` - HTML files (Jinja2).
* `static/` - CSS files and images.
* `instance/store.db` - The SQLite database file.