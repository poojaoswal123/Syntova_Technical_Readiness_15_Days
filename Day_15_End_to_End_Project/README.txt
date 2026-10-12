# E-Commerce Order Management & Sales Analytics API

## Project Overview
This project uses an Amazon-style e-commerce orders dataset containing 100,000 records. It provides REST API endpoints for retrieving, creating, updating, and deleting orders, along with sales analytics.

## Technologies Used
- Python
- FastAPI
- PostgreSQL
- Pandas
- SQL
- Docker
- Git and GitHub

## Dataset
The project uses `amazon.csv`, containing 100,000 rows and 20 columns, including order details, customer information, product categories, prices, payment methods, order statuses, and locations.

## Features
- View recent orders and total order count
- Create new orders
- Update order status
- Delete orders
- Calculate total sales and average order amount
- Analyse sales by product category
- Summarise orders by status
- Perform Pandas-based sales analytics

## API Endpoints

 Method  Endpoint  Purpose 
---------
 GET  ``  Check API status 
 GET  `orders`  Retrieve recent orders 
 GET  `orderscount`  Count all orders 
 POST  `orders`  Create an order 
 PUT  `orders{order_id}status`  Update order status 
 DELETE  `orders{order_id}`  Delete an order 
 GET  `analyticssummary`  Overall sales summary 
 GET  `analyticscategories`  Category-wise sales 
 GET  `analyticsstatus`  Order-status summary 
 GET  `analyticspandas`  Pandas-based analytics 

## Run Locally

1. Install the packages
   `python -m pip install -r requirements.txt`
2. Set the `DB_PASSWORD` environment variable to your PostgreSQL password.
3. Create the `ecommerce_db` database and import `amazon.csv` into the `orders` table.
4. Start the API
   `python -m uvicorn mainapp --reload`
5. Open `http127.0.0.18000docs` to test the endpoints.

## Project Outcome
The application connects FastAPI to PostgreSQL and uses SQL and Pandas to retrieve, manage, and analyse e-commerce order data.