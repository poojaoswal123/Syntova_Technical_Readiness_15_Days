import sqlite3
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="E-Commerce Order Management API")

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "ecommerce.db"


def get_connection():
    return sqlite3.connect(DB_PATH)

class OrderCreate(BaseModel):
    Category: str
    TotalAmount: float
    OrderStatus: str

@app.get("/")
def home():
    return {"message": "E-Commerce API is running"}


@app.get("/orders/count")
def count_orders():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM orders")
    total = cursor.fetchone()[0]

    connection.close()

    return {"total_orders": total}


@app.get("/orders")
def get_orders():
    connection = get_connection()
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT rowid AS order_rowid, * FROM orders LIMIT 10")
    orders = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return {"orders": orders}


@app.get("/analytics/summary")
def sales_summary():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COUNT(*) AS total_orders,
            SUM(TotalAmount) AS total_sales,
            AVG(TotalAmount) AS average_order_amount
        FROM orders
    """)

    row = cursor.fetchone()
    connection.close()

    return {
        "total_orders": row[0],
        "total_sales": row[1],
        "average_order_amount": row[2]
    }


@app.get("/analytics/categories")
def category_summary():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT Category, COUNT(*) AS order_count,
               SUM(TotalAmount) AS total_sales
        FROM orders
        GROUP BY Category
        ORDER BY total_sales DESC
    """)

    results = cursor.fetchall()
    connection.close()

    return {
        "categories": [
            {
                "category": row[0],
                "order_count": row[1],
                "total_sales": row[2]
            }
            for row in results
        ]
    }

@app.post("/orders")
def create_order(order: OrderCreate):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO orders (Category, TotalAmount, OrderStatus)
        VALUES (?, ?, ?)
    """, (order.Category, order.TotalAmount, order.OrderStatus))

    new_rowid = cursor.lastrowid
    connection.commit()
    connection.close()

    return {
        "message": "Order created successfully",
        "order_rowid": new_rowid
    }


@app.put("/orders/{order_rowid}")
def update_order(order_rowid: int, order: OrderCreate):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE orders
        SET Category = ?, TotalAmount = ?, OrderStatus = ?
        WHERE rowid = ?
    """, (
        order.Category,
        order.TotalAmount,
        order.OrderStatus,
        order_rowid
    ))

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(status_code=404, detail="Order not found")

    connection.commit()
    connection.close()

    return {"message": "Order updated successfully"}


@app.delete("/orders/{order_rowid}")
def delete_order(order_rowid: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM orders WHERE rowid = ?",
        (order_rowid,)
    )

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(status_code=404, detail="Order not found")

    connection.commit()
    connection.close()

    return {"message": "Order deleted successfully"}


# {
#  "Category": "Electronics",
#  "TotalAmount": 1500,
#  "OrderStatus": "Pending"
# }

# {
#  "Category": "Electronics",
#  "TotalAmount": 2000,
#  "OrderStatus": "Shipped"
# }