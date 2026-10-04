-- DAY 7: TIME-SERIES DATA
-- PostgreSQL Practice

-- 1. CREATE TABLE
-- DATE stores date only
-- TIMESTAMP stores date and time
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    sale_date DATE,
    sale_time TIMESTAMP,
    product_name VARCHAR(100),
    quantity INT,
    amount NUMERIC(10,2)
);

-- 2. INSERT TIME-SERIES DATA
INSERT INTO sales
(sale_id, sale_date, sale_time, product_name, quantity, amount)
VALUES
(1, '2026-09-01', '2026-09-01 10:15:00', 'Laptop', 2, 120000),
(2, '2026-09-02', '2026-09-02 11:30:00', 'Mouse', 5, 5000),
(3, '2026-09-03', '2026-09-03 14:20:00', 'Keyboard', 3, 9000),
(4, '2026-09-05', '2026-09-05 16:10:00', 'Laptop', 1, 60000),
(5, '2026-09-07', '2026-09-07 12:45:00', 'Monitor', 2, 40000),
(6, '2026-09-10', '2026-09-10 09:30:00', 'Mouse', 10, 10000),
(7, '2026-09-15', '2026-09-15 13:15:00', 'Laptop', 3, 180000),
(8, '2026-09-20', '2026-09-20 15:40:00', 'Keyboard', 4, 12000),
(9, '2026-09-25', '2026-09-25 17:00:00', 'Monitor', 3, 60000),
(10, '2026-09-30', '2026-09-30 18:20:00', 'Laptop', 2, 120000);

-- 3. VIEW TIME-SERIES DATA
SELECT *
FROM sales
ORDER BY sale_date;

-- 4. CURRENT DATE AND TIME
SELECT
    CURRENT_DATE AS today,
    CURRENT_TIMESTAMP AS current_time;

-- 5. FILTER DATA BY DATE
SELECT *
FROM sales
WHERE sale_date >= '2026-09-10';

-- 6. FILTER DATA BETWEEN TWO DATES
SELECT *
FROM sales
WHERE sale_date BETWEEN '2026-09-01' AND '2026-09-15';

-- 7. EXTRACT YEAR, MONTH AND DAY
SELECT
    sale_date,
    EXTRACT(YEAR FROM sale_date) AS year,
    EXTRACT(MONTH FROM sale_date) AS month,
    EXTRACT(DAY FROM sale_date) AS day
FROM sales;

-- 8. EXTRACT HOUR FROM TIMESTAMP
SELECT
    sale_time,
    EXTRACT(HOUR FROM sale_time) AS hour
FROM sales;

-- 9. FORMAT DATE USING TO_CHAR
SELECT
    sale_date,
    TO_CHAR(sale_date, 'DD-MM-YYYY') AS formatted_date
FROM sales;

-- 10. FORMAT TIMESTAMP
SELECT
    sale_time,
    TO_CHAR(sale_time, 'DD-MM-YYYY HH24:MI:SS') AS formatted_time
FROM sales;

-- 11. DAILY SALES
-- Converts individual transactions into daily totals
SELECT
    sale_date,
    SUM(amount) AS daily_sales
FROM sales
GROUP BY sale_date
ORDER BY sale_date;

-- 12. DAILY TRANSACTION COUNT
SELECT
    sale_date,
    COUNT(*) AS transaction_count
FROM sales
GROUP BY sale_date
ORDER BY sale_date;

-- 13. MONTHLY SALES
SELECT
    DATE_TRUNC('month', sale_date) AS month,
    SUM(amount) AS monthly_sales
FROM sales
GROUP BY DATE_TRUNC('month', sale_date)
ORDER BY month;

-- 14. SALES BY PRODUCT
SELECT
    product_name,
    SUM(amount) AS total_sales
FROM sales
GROUP BY product_name
ORDER BY total_sales DESC;

-- 15. AVERAGE SALE AMOUNT
SELECT
    AVG(amount) AS average_sale
FROM sales;

-- 16. HIGHEST-SALES DAY
SELECT
    sale_date,
    SUM(amount) AS daily_sales
FROM sales
GROUP BY sale_date
ORDER BY daily_sales DESC
LIMIT 1;

-- 17. LOWEST-SALES DAY
SELECT
    sale_date,
    SUM(amount) AS daily_sales
FROM sales
GROUP BY sale_date
ORDER BY daily_sales
LIMIT 1;

-- 18. FILTER BY TIME
-- Find sales after 5 PM
SELECT *
FROM sales
WHERE EXTRACT(HOUR FROM sale_time) >= 17
ORDER BY sale_time;

-- 19. DATE_TRUNC BY DAY
-- Useful when working with TIMESTAMP data
SELECT
    DATE_TRUNC('day', sale_time) AS day,
    COUNT(*) AS transactions
FROM sales
GROUP BY DATE_TRUNC('day', sale_time)
ORDER BY day;

-- 20. DATE_TRUNC BY HOUR
-- Groups timestamp records by hour
SELECT
    DATE_TRUNC('hour', sale_time) AS hour,
    COUNT(*) AS transactions
FROM sales
GROUP BY DATE_TRUNC('hour', sale_time)
ORDER BY hour;

-- 21. DATE INTERVAL
-- Add 7 days to a date
SELECT
    sale_date,
    sale_date + INTERVAL '7 days' AS next_week
FROM sales;

-- 22. DATE DIFFERENCE
-- Number of days between sale date and today
SELECT
    sale_date,
    CURRENT_DATE - sale_date AS days_difference
FROM sales;

-- 23. SALES FOR A SPECIFIC PRODUCT OVER TIME
SELECT
    sale_date,
    amount
FROM sales
WHERE product_name = 'Laptop'
ORDER BY sale_date;

-- 24. SALES GREATER THAN A VALUE
SELECT *
FROM sales
WHERE amount > 50000
ORDER BY sale_date;

-- 25. COMPLETE DAILY TIME-SERIES SUMMARY
SELECT
    sale_date,
    SUM(amount) AS daily_sales,
    COUNT(*) AS transactions,
    AVG(amount) AS average_sale
FROM sales
GROUP BY sale_date
ORDER BY sale_date;

-- 26. FIND THE DAY WITH MOST TRANSACTIONS
SELECT
    sale_date,
    COUNT(*) AS transaction_count
FROM sales
GROUP BY sale_date
ORDER BY transaction_count DESC
LIMIT 1;

-- 27. FIND TOTAL QUANTITY SOLD PER DAY
SELECT
    sale_date,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY sale_date
ORDER BY sale_date;

-- 28. PRACTICAL TIME-SERIES ANALYSIS
-- Compare sales and transactions over time
SELECT
    sale_date,
    SUM(amount) AS daily_sales,
    COUNT(*) AS transactions,
    SUM(quantity) AS quantity_sold
FROM sales
GROUP BY sale_date
ORDER BY sale_date;