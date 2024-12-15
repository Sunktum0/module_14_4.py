# add_products.py
import sqlite3
from aifc import Error

DATABASE = ("products.db")

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except Error as e:
        print(e)

def add_product(title, description, price):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?);",
                           (title, description, price))
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

# Добавьте записи
add_product("Product1", "Описание продукта 1", 100)
add_product("Product2", "Описание продукта 2", 200)
add_product("Product3", "Описание продукта 3", 300)
add_product("Product4", "Описание продукта 4", 400)