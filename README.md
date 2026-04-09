# Flask Store

A simple e-commerce admin app built with Flask. It lets you manage products, customers, and orders  with inventory tracking baked in.

## What it does

- **Products & Categories**  Browse the catalog, filter by category.
- **Customers**  View customer profiles and their order history (pending and completed).
- **Orders**  See order details, complete orders with a single click. The app checks stock before completing a sale and rolls back if there's not enough inventory.
- **Data Seeding**  A management script generates realistic test data so you can try things out immediately.

## Tech

- Python / Flask
- SQLAlchemy ORM with SQLite
- Jinja2 templates, plain CSS

## Getting Started

### With Docker (recommended)

```bash
docker compose up --build
```

The app will be available at `http://localhost:8888`. The database gets seeded automatically on first run.

### Without Docker

1. Clone the repo and `cd` into `project/store`:
   ```bash
   git clone <your-repo-url>
   cd project/store
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # on Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install flask sqlalchemy flask-sqlalchemy
   ```

4. Seed the database:
   ```bash
   python manage.py
   ```

5. Run the app:
   ```bash
   python app.py
   ```

6. Open `http://127.0.0.1:8888` in your browser.

## Project Structure

```
project/store/
  app.py        — Routes and Flask app setup
  models.py     — SQLAlchemy models and business logic
  db.py         — Database initialization
  manage.py     — DB seeding script
  templates/    — Jinja2 HTML templates
  static/       — CSS stylesheets
  data/         — CSV seed files (products, customers)
```
