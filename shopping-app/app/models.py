import sqlite3


db = sqlite3.connect('database.db')


cursor = db.cursor()


cursor.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price INTEGER)')
cursor.execute('CREATE TABLE IF NOT EXISTS cart (id INTEGER PRIMARY KEY, product_id INTEGER)')


cursor.execute('INSERT INTO products (name, price) VALUES ("Laptop", 800)')
cursor.execute('INSERT INTO products (name, price) VALUES ("Phone", 400)')




db.commit()
db.close()