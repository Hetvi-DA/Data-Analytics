create database Superstore_DB2;

use Superstore_DB2;

CREATE TABLE Orders_Raw (
    Customer_Name VARCHAR(255),
    Customer_ID VARCHAR(50),
    Row_ID VARCHAR(50),
    Order_Priority VARCHAR(50),
    Discount VARCHAR(50),
    Unit_Price VARCHAR(50),
    Shipping_Cost VARCHAR(50),
    Ship_Mode VARCHAR(100),
    Customer_Segment VARCHAR(100),
    Product_Category VARCHAR(100),
    Product_Sub_Category VARCHAR(100),
    Product_Container VARCHAR(100),
    Product_Name TEXT,
    Product_Base_Margin VARCHAR(50),
    Country VARCHAR(100),
    Region VARCHAR(100),
    State_or_Province VARCHAR(100),
    City VARCHAR(100),
    Postal_Code VARCHAR(50),
    Order_Date date,
    Ship_Date VARCHAR(50),
    Profit VARCHAR(50),
    Quantity_ordered_new VARCHAR(50),
    Sales VARCHAR(50),
    Order_ID VARCHAR(50),
);

SHOW VARIABLES LIKE 'secure_file_priv';

LOAD DATA INFILE'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/SuperStoreUS-2015 1 (3).csv'
INTO TABLE Orders_Raw
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '/r/n'
IGNORE 1 ROWS
(
    Customer_Name,
    Customer_ID,
    Row_ID,
    Order_Priority,
    Discount,
    Unit_Price,
    Shipping_Cost,
    Ship_Mode,
    Customer_Segment,
    Product_Category,
    Product_Sub_Category,
    Product_Container,
    Product_Name,
    Product_Base_Margin,
    Country,
    Region,
    State_or_Province,
    City,
    Postal_Code,
    Order_Date,
    Ship_Date,
    Profit,
    Quantity_ordered_new,
    Sales,
    Order_ID,
    @dummy1,
    @dummy2,
    @dummy3
);


SELECT * 
FROM Orders_Raw;

SELECT COUNT(*) 
FROM Orders_Raw;

-- 1. Display All Records
select * from Orders_Raw;

-- Select Specific Columns
SELECT Customer_Name, Product_Name, Sales, Profit
FROM Orders_Raw;	
 
-- Filter by State
select * from Orders_Raw
where state_or_province = 'california';

-- 4. Negative Profit Orders
select * from Orders
where profit < 0;

-- 5. Discount Based Filtering
select * from Orders_Raw
where Discount > 2;

-- 6. Sort Data
select * from Orders_Raw
order by sales desc;

-- 7. Top Selling Orders
select * from Orders_Raw
order by sales desc
limit 10;

-- 8. Unique Customer Segments
select DISTINCT Customer_Segment FROM Orders_Raw;

-- 9. Sales Range Filtering
select * from Orders
where sales between 500 and 2000;

-- 10. Customer Name Pattern
select * from Orders_Raw
where Customer_Name like 'A%';

-- Intermediate Level SQL Questions

-- 11. Total Sales
SELECT SUM(Sales) AS Total_Sales FROM Orders_Raw;

-- 12. Average Profit
select avg(profit) AS Average_profit from Orders_Raw;

-- 13. Maximum Sales
select max(sales) as Highest_Sales from Orders_Raw;

-- 14. Minimum Profit
select min(profit) as Lowest_Profit from Orders_Raw;

-- 15. Total Number of Orders
select count(*) as Total_Orders from Orders_Raw;

-- 16. Sales by Region
select sum(sales) as Total_Sales
from Orders_Raw
group by Region;

-- 17. Profit by State
select sum(Profit) as Total_Profit
from Orders_Raw
group by state_or_province;

-- 18. Average Sales by Segment
select Avg(sales) as Average_sales
from Orders_Raw
group by Customer_Segment;

-- 19. Customer Count by Region
select Count(*) As Total_Customers
from Orders_Raw
group by region;

-- 20. Quantity Sold by Category
select SUM(Quantity_ordered_new) AS Total_Quantity
FROM Orders_Raw
GROUP BY Product_Category;

-- Advanced Level SQL Questions

-- 21. High Sales Regions
select sum(sales) as Total_sales
from Orders_Raw
group by region
having Total_sales > 50000;

-- 22. High Profit Categories
select avg(Profit) as average_profit
from Orders_Raw 
group by product_category
having average_profit > 100;

-- 23. Monthly Orders
select Month(Order_Date) AS Month_No, Count(*) As Total_Orders
from Orders
Group by Month(Order_Date)
Order by Month_No;

-- 24. Shipping Delay Analysis

-- 25. Date Filtering
SELECT *
FROM Orders
WHERE Order_Date > '2015-06-01';

-- JOIN Practice Questions

-- 26. Returned Orders

create table Returns(
Order_Id int primary key,
status varchar(50)
);

SHOW VARIABLES LIKE 'secure_file_priv';

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Returns.csv'
INTO TABLE Returns
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
	Order_ID,
    status 
);

select * from Returns;

-- 27. Non-Returned Orders


-- 28. Returned Orders by Region


-- Business Scenario Based Questions

-- 29. Top Customers
SELECT Customer_Name,
SUM(Sales) AS Total_Sales
FROM Orders
GROUP BY Customer_Name
ORDER BY Total_Sales DESC
LIMIT 5;

-- 30. Most Profitable Category
SELECT Product_Category,
SUM(Profit) AS Total_Profit
FROM Orders
GROUP BY Product_Category
ORDER BY Total_Profit DESC
LIMIT 1;

