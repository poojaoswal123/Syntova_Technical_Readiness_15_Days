import pandas as pd
import sqlite3
from pathlib import Path

# SQLite is a database system that stores data in a database file.
# We used it to connect Python to our SQLite database and execute SQL queries.

# Find the project folder
BASE_DIR = Path(__file__).resolve().parent

# Read the dataset
csv_path = BASE_DIR / "data" / "Amazon.csv"
df = pd.read_csv(csv_path)

# Connect to the database in the project folder
db_path = BASE_DIR / "ecommerce.db"
connection = sqlite3.connect(db_path)
# Python connects to the ecommerce.db database.

# Import the dataset into SQL
df.to_sql("orders", connection, if_exists="replace", index=False)

# Verify the imported records
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM orders")
print("Total orders imported:", cursor.fetchone()[0])

# Show actual column names
cursor.execute("PRAGMA table_info(orders)")
print("Database columns:", [row[1] for row in cursor.fetchall()])

connection.close()