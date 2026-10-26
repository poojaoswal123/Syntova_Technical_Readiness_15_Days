# E-Commerce Order Management and Sales Analysis

## Project Overview
This project uses an e-commerce dataset to retrieve order information and analyse sales. I used Python, SQL, SQLite, Pandas, and FastAPI.

## Dataset
The project uses an Amazon e-commerce dataset containing 100,000 records and 20 columns.

The dataset includes:
- Order ID and order date
- Customer and product details
- Product category and brand
- Quantity, unit price, discount, and tax
- Total amount
- Payment method and order status
- Location and seller information

## Technologies Used
- Python
- SQL
- SQLite
- Pandas
- FastAPI
- Uvicorn

## Project Features
1. Dataset inspection using Pandas.
2. Checking missing values and duplicate records.
3. Importing the dataset into SQLite.
4. Counting orders using SQL.
5. Calculating total sales and average order amount.
6. Analysing sales by product category.
7. Retrieving order details through API endpoints.
8. Testing endpoints using Swagger UI.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Checks whether the API is running |
| GET | `/orders/count` | Counts total orders |
| GET | `/orders` | Retrieves the first 10 orders |
| GET | `/analytics/summary` | Shows sales statistics |
| GET | `/analytics/categories` | Shows category-wise analysis |

## How to Run

### 1. Install dependencies
```bash
python -m pip install -r requirements.txt
```

### 2. Import the dataset
Ensure `Amazon(2).csv` is inside the `data` folder.

```bash
python import_data.py
```

### 3. Run dataset analysis
```bash
python dataset_analysis.py
```

### 4. Run SQL analysis
```bash
python sql_analysis.py
```

### 5. Start the API
```bash
python -m uvicorn main:app --reload
```

### 6. Open Swagger UI
Open `http://127.0.0.1:8000/docs` in your browser.

## Conclusion
This project helped me practise SQL queries, database operations, data analysis, and API development using Python.