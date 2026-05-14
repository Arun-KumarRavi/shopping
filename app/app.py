from flask import Flask, render_template, redirect
import sqlite3

import os

app = Flask(__name__)
DB_PATH = "database.db"

def get_db():
    return sqlite3.connect(DB_PATH)

def init_db():
    if not os.path.exists(DB_PATH):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price INTEGER)')
        cursor.execute('CREATE TABLE IF NOT EXISTS cart (id INTEGER PRIMARY KEY, product_id INTEGER)')
        cursor.execute('INSERT INTO products (name, price) VALUES ("High-End Laptop", 1200)')
        cursor.execute('INSERT INTO products (name, price) VALUES ("Pro Smartphone", 800)')
        cursor.execute('INSERT INTO products (name, price) VALUES ("Wireless Headphones", 250)')
        db.commit()
        db.close()


@app.route("/")
def index():
    db = get_db()
    products = db.execute("SELECT * FROM products").fetchall()
    return render_template("index.html", products=products)


@app.route("/add/<int:product_id>")
def add_to_cart(product_id):
    db = get_db()
    db.execute(
        "INSERT INTO cart(product_id) VALUES (?)",
        (product_id,)
    )
    db.commit()
    return redirect("/")


@app.route("/cart")
def cart():
    db = get_db()
    items = db.execute("""
        SELECT p.name, p.price
        FROM cart c
        JOIN products p ON c.product_id = p.id
    """).fetchall()
    return render_template("cart.html", items=items)


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
