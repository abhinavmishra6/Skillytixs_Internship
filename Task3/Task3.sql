SELECT * FROM superstoredataset LIMIT 10;
SELECT `Order ID`, `Customer ID`, Sales FROM superstoredataset;
SELECT * FROM superstoredataset WHERE State = 'California';
SELECT `Order ID`, Sales, Profit FROM superstoredataset ORDER BY Profit DESC;
SELECT Category, SUM(Sales) AS TotalSales FROM superstoredataset GROUP BY Category ORDER BY TotalSales DESC;
SELECT MONTH(`Order Date`) AS Month, SUM(Sales) AS MonthlySale FROM superstoredataset GROUP BY MONTH(`Order Date`) ORDER BY Month;
SELECT `Order ID`, `Product Name`, Profit FROM superstoredataset ORDER BY Profit DESC LIMIT 5;
SELECT a.`Order ID` AS Order1, b.`Order ID` AS Order2, a.`Customer ID`, a.`Customer Name` FROM superstoredataset a INNER JOIN superstoredataset b ON a.`Customer ID` = b.`Customer ID` AND a.`Order ID` <> b.`Order ID` LIMIT 10;
