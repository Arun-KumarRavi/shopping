from flask import Flask, render_template, redirect
import sqlite3

app = Flask(__name__)


def get_db():
    return sqlite3.connect("database.db")


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
    app.run(host="0.0.0.0", port=5000)
