/*Data Cleaning*/
CREATE TABLE companies (
    datasetid INT PRIMARY KEY,
    name VARCHAR(255),
    industry VARCHAR(255),
    year_founded INT,
    employees INT,
    state VARCHAR(2),
    city VARCHAR(255)
);

INSERT INTO companies VALUES
(1, 'Over-Hex', 'Software', 2006, 25, 'TX', 'Franklin'),
(2, 'Unimattax', 'IT Services', 2009, 36, 'TX', 'Newtown Square'),
(3, 'Lexila', 'Real Estate', 2032, 38, 'IL', 'Tinley Park'),
(4, 'Greenfax', 'Retail', 2012, 320, 'SC', 'Greenville'),
(5, 'Saoace', 'Energy', 2009, 24, 'WI', 'New Holstein'),
(6, 'Donplus', 'Advertising & Marketing', 2009, 26, 'CA', 'Los Angeles'),
(7, 'Blacklane', 'IT Services', 2011, 9, 'CA', 'Orange'),
(8, 'Toughtam', 'Logistics & Transportation', 2011, 20, 'AL', 'Birmingham'),
(9, 'Toughtam', 'Logistics & Transportation', 2011, 20, 'AL', 'Birmingham'),
(10, 'Quotelane', 'Advertising & Marketing', NULL, 4, 'SC', 'Greenville'),
(11, 'Ganzzap', 'Advertising & Marketing', 2011, 133, 'CA', 'San Francisco'),
(12, 'Yearflex', NULL, 2013, 45, 'WI', 'Madison');


/* Step-1:Deleting duplicate rows*/
/*checking if there are duplicate rows*/
SELECT NAME, COUNT(NAME) AS count_n
FROM COMPANIES
GROUP BY NAME
HAVING COUNT(NAME)>1;
/*DELETING DUPLICATE ROWS BY ORDERING DATA  (partition by gives unique values to each unique row , order by gives unique consecutive values to each unique row)*/
WITH CTE AS
(SELECT NAME, ROW_NUMBER() OVER (PARTITION BY NAME ORDER BY DATASETID DESC)AS RN
FROM COMPANIES)
DELETE FROM CTE WHERE RN>1;


SELECT * FROM companies;

/*STEP-2:REMOVING NULL VALUES*/
SELECT *
FROM companies
WHERE industry IS NULL

DELETE
FROM companies
WHERE year_founded IS NULL

/*STEP-3:UPDATING WITH MEANINGFUL VALUES*/
UPDATE COMPANIES
SET INDUSTRY = 'OTHER'
WHERE INDUSTRY IS NULL

UPDATE companies
SET state = UPPER(state)

/*STEP-4:CORRECT LOGICAL ERRORS*/
SELECT *
FROM companies
WHERE year_founded > YEAR(GETDATE());

UPDATE COMPANIES
SET YEAR_FOUNDED= YEAR(GETDATE())
WHERE year_founded > YEAR(GETDATE());


/*creating a procedure for order table (order_num, item_price, quantity) given an ordernum procedure has to give its total amount. calculate 10% tax for the amount greater than 1000
*/

CREATE TABLE ORDERS(ORDER_NUM INT, ITEM_PRICE DECIMAL, QUANTITY INT);

INSERT INTO ORDERS (ORDER_NUM, ITEM_PRICE, QUANTITY) VALUES
(1, 10.50, 5),
(2, 25.00, 3),
(3, 30.75, 2);

CREATE PROCEDURE ORDER_PROC @ORDER_NUM INT, @ITEM_PRICE INT
AS
DECLARE @SUBTOTAL DECIMAL(10, 2)
DECLARE @TOTAL_AMOUNT DECIMAL(10,2) 
SET @SUBTOTAL = @ORDER_NUM * @ITEM_PRICE
IF @SUBTOTAL >1000
SET @TOTAL_AMOUNT = @SUBTOTAL + (@SUBTOTAL*0.10);
ELSE
SET @TOTAL_AMOUNT = @SUBTOTAL; 
SELECT @TOTAL_AMOUNT;

EXEC ORDER_PROC @ORDER_NUM= 1,@ITEM_PRICE=10.50;


/*OVER, PARTITION BY*/
CREATE DATABASE CarDatabase;

USE CARDATABASE;

CREATE TABLE CAR_LIST_PRICES (
    car_make VARCHAR(50),
    car_model VARCHAR(50),
    car_type VARCHAR(50),
    car_price INT
);

INSERT INTO CAR_LIST_PRICES (car_make, car_model, car_type, car_price) VALUES
('Ford', 'Mondeo', 'premium', 18200),
('Renault', 'Fuego', 'sport', 16500),
('Citroen', 'Cactus', 'premium', 19000),
('Ford', 'Falcon', 'low cost', 8990),
('Ford', 'Galaxy', 'standard', 12400),
('Renault', 'Megane', 'standard', 14300),
('Citroen', 'Picasso', 'premium', 23400);

SELECT * FROM CAR_LIST_PRICES;
SELECT
    car_make,
    car_model,
	car_type,
    car_price,
    AVG(car_price) OVER() AS "overall average price",
    AVG(car_price) OVER (PARTITION BY car_type) AS "car type average price"
FROM car_list_prices


SELECT car_make,
       car_model,
       car_price,
       AVG(car_price) OVER (PARTITION BY car_make) AS average_make
FROM   car_list_prices
