
import pandas as pd
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="E-Commerce Order Management API")


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
        database=os.getenv("DB_NAME", "ecommerce_db"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "YOUR_POSTGRES_PASSWORD")
    )


@app.get("/")
def home():
    return {"message": "E-Commerce API is running"}

@app.get("/orders")
def get_orders():
    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("""
                    SELECT *
                    FROM orders
                    ORDER BY order_date DESC
                    LIMIT 20
                """)
                return [dict(row) for row in cursor.fetchall()]
    except psycopg2.Error as error:
        raise HTTPException(
            status_code=500,
            detail="Database query failed. Check your database connection."
        ) from error


@app.get("/orders/count")
def get_order_count():
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM orders")
                total = cursor.fetchone()[0]
                return {"total_orders": total}
    except psycopg2.Error as error:
        print("Database error:", error)
        raise HTTPException(
            status_code=500,
            detail=str(error)
        ) from error


@app.get("/analytics/summary")
def sales_summary():
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT
                        COUNT(*),
                        SUM(total_amount),
                        AVG(total_amount)
                    FROM orders
                """)
                result = cursor.fetchone()

        return {
            "total_orders": result[0],
            "total_sales": float(result[1] or 0),
            "average_order_amount": float(result[2] or 0)
        }

    except psycopg2.Error as error:
        raise HTTPException(
            status_code=500,
            detail="Could not calculate sales summary."
        ) from error


@app.get("/analytics/categories")
def category_sales():
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT
                        category,
                        COUNT(*) AS total_orders,
                        SUM(quantity) AS units_sold,
                        SUM(total_amount) AS total_sales
                    FROM orders
                    GROUP BY category
                    ORDER BY total_sales DESC
                """)

                rows = cursor.fetchall()

        return [
            {
                "category": row[0],
                "total_orders": row[1],
                "units_sold": row[2],
                "total_sales": float(row[3] or 0)
            }
            for row in rows
        ]

    except psycopg2.Error as error:
        raise HTTPException(
            status_code=500,
            detail="Could not retrieve category sales."
        ) from error



class OrderCreate(BaseModel):
    order_id: str
    order_date: str
    customer_id: str
    customer_name: str
    product_id: str
    product_name: str
    category: str
    brand: str
    quantity: int
    unit_price: float
    discount: float = 0
    tax: float = 0
    shipping_cost: float = 0
    total_amount: float
    payment_method: str
    order_status: str
    city: str
    state: str
    country: str
    seller_id: str


@app.post("/orders", status_code=201)
def create_order(order: OrderCreate):
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO orders (
                        order_id, order_date, customer_id, customer_name,
                        product_id, product_name, category, brand, quantity,
                        unit_price, discount, tax, shipping_cost, total_amount,
                        payment_method, order_status, city, state, country, seller_id
                    )
                    VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                    )
                    RETURNING order_id
                """, (
                    order.order_id, order.order_date, order.customer_id,
                    order.customer_name, order.product_id, order.product_name,
                    order.category, order.brand, order.quantity, order.unit_price,
                    order.discount, order.tax, order.shipping_cost, order.total_amount,
                    order.payment_method, order.order_status, order.city,
                    order.state, order.country, order.seller_id
                ))

                new_order_id = cursor.fetchone()[0]

        return {"message": "Order created successfully", "order_id": new_order_id}

    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Order ID already exists")
    except psycopg2.Error as error:
        raise HTTPException(status_code=500, detail="Could not create order") from error



@app.put("/orders/{order_id}/status")
def update_order_status(order_id: str, new_status: str):
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    UPDATE orders
                    SET order_status = %s
                    WHERE order_id = %s
                    RETURNING order_id, order_status
                """, (new_status, order_id))

                updated_order = cursor.fetchone()

        if updated_order is None:
            raise HTTPException(
                status_code=404,
                detail="Order not found"
            )

        return {
            "message": "Order status updated successfully",
            "order_id": updated_order[0],
            "order_status": updated_order[1]
        }

    except psycopg2.Error as error:
        raise HTTPException(
            status_code=500,
            detail="Could not update order status"
        ) from error



@app.delete("/orders/{order_id}")
def delete_order(order_id: str):
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM orders
                    WHERE order_id = %s
                    RETURNING order_id
                """, (order_id,))

                deleted_order = cursor.fetchone()

        if deleted_order is None:
            raise HTTPException(
                status_code=404,
                detail="Order not found"
            )

        return {
            "message": "Order deleted successfully",
            "order_id": deleted_order[0]
        }

    except psycopg2.Error as error:
        raise HTTPException(
            status_code=500,
            detail="Could not delete order"
        ) from error


@app.get("/analytics/status")
def order_status_summary():
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT
                        order_status,
                        COUNT(*) AS total_orders
                    FROM orders
                    GROUP BY order_status
                    ORDER BY total_orders DESC
                """)
                rows = cursor.fetchall()

        return [
            {
                "order_status": row[0],
                "total_orders": row[1]
            }
            for row in rows
        ]

    except psycopg2.Error as error:
        raise HTTPException(
            status_code=500,
            detail="Could not retrieve order status summary."
        ) from error



@app.get("/analytics/pandas")
def pandas_analytics():
    try:
        with get_connection() as conn:
            df = pd.read_sql_query("""
                SELECT category, quantity, total_amount
                FROM orders
            """, conn)

        if df.empty:
            return {
                "total_orders": 0,
                "total_sales": 0,
                "average_order_amount": 0,
                "top_category": None
            }

        category_sales = df.groupby("category")["total_amount"].sum()
        top_category = category_sales.idxmax()

        return {
            "total_orders": int(len(df)),
            "total_sales": float(df["total_amount"].sum()),
            "average_order_amount": float(df["total_amount"].mean()),
            "top_category": str(top_category),
            "top_category_sales": float(category_sales.max())
        }

    except (psycopg2.Error, ValueError) as error:
        raise HTTPException(
            status_code=500,
            detail="Could not calculate Pandas analytics."
        ) from error
