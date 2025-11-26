USE sales_db;
CREATE TABLE online_sales AS SELECT
    order_id, order_date, product_id, total_amount AS amount
FROM ecommerce_raw
WHERE total_amount IS NOT NULL AND order_date IS NOT NULL;

SELECT
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    DATE_FORMAT(order_date, '%Y-%m') AS month_label,
    SUM(amount) AS total_revenue,
    COUNT(DISTINCT order_id) AS total_orders
FROM online_sales 
GROUP BY year, month, month_label 
ORDER BY year, month;

SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month_label,
    SUM(amount) AS total_revenue
FROM online_sales
GROUP BY month_label
ORDER BY total_revenue DESC
LIMIT 5;

SELECT
    SUM(amount) / COUNT(DISTINCT order_id) AS avg_revenue_per_order
FROM online_sales;
