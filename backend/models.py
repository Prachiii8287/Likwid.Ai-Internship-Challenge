
import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        country TEXT,
        product TEXT,
        sales REAL
    )
    """)
    conn.commit()
    conn.close()

init_db()

def insert_or_update_customer(name, country, product, sales):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("""
        SELECT id FROM customers WHERE name=? AND country=? AND product=?
    """, (name, country, product))
    result = cur.fetchone()

    if result:
        cur.execute("""
            UPDATE customers SET sales = sales + ? WHERE id = ?
        """, (sales, result[0]))
    else:
        cur.execute("""
            INSERT INTO customers (name, country, product, sales) VALUES (?, ?, ?, ?)
        """, (name, country, product, sales))

    conn.commit()
    conn.close()

def fetch_all_customers():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers")
    rows = cur.fetchall()
    conn.close()
    return rows
