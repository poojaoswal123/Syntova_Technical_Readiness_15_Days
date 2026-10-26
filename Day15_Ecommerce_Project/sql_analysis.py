import sqlite3
from pathlib import Path

# Connect to the project database
BASE_DIR = Path(__file__).resolve().parent
connection = sqlite3.connect(BASE_DIR / "ecommerce.db")
cursor = connection.cursor()

# 1. Total orders
print("\n1. Total Orders")
cursor.execute("SELECT COUNT(*) FROM orders")
print(cursor.fetchone()[0])

# 2. Total sales
print("\n2. Total Sales")
cursor.execute('SELECT SUM("TotalAmount") FROM orders')
print(cursor.fetchone()[0])

# 3. Average order amount
print("\n3. Average Order Amount")
cursor.execute('SELECT AVG("TotalAmount") FROM orders')
print(cursor.fetchone()[0])

# 4. Orders by category
print("\n4. Orders by Category")
cursor.execute("""
    SELECT Category, COUNT(*)
    FROM orders
    GROUP BY Category
    ORDER BY COUNT(*) DESC
""")

for row in cursor.fetchall():
    print(row)

# 5. Order status summary
print("\n5. Orders by Status")
cursor.execute("""
    SELECT OrderStatus, COUNT(*)
    FROM orders
    GROUP BY OrderStatus
    ORDER BY COUNT(*) DESC
""")

for row in cursor.fetchall():
    print(row)

connection.close()