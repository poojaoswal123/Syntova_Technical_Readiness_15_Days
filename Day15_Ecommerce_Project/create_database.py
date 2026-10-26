import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("ecommerce.db")

# Create a cursor to execute SQL queries
cursor = connection.cursor()

# Create a table for storing orders
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date TEXT,
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Save changes and close the connection
connection.commit()
connection.close()

print("Database and orders table created successfully!")