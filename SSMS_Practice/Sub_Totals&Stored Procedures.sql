/*SUB-TOTALS*/
CREATE TABLE
SalesList
(SalesMonth NVARCHAR(20), SalesQuartes  VARCHAR(5), SalesYear  SMALLINT, SalesTotal MONEY)
GO
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'March','Q1',2019,60);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'March','Q1',2020,50);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'May','Q2',2019,30);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'July','Q3',2020,10);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'November','Q4',2019,120);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'October','Q4',2019,150);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'November','Q4',2019,180);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'November','Q4',2020,120);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'July','Q3',2019,160);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'March','Q1',2020,170);
GO
SELECT  * FROM SalesList

/*ROLL UP - SUMS UP ACCORDING TO THE YEARS SPECIFIED  */
SELECT  SalesYear, SUM(SalesTotal) AS SalesTotal FROM SalesList
GROUP BY ROLLUP(SalesYear)
/*BELOW QUERY SUMS UP ACCORDING TO THE	QUARTERS SPECIFIED */
SELECT  SalesYear,SalesQuartes ,SUM(SalesTotal) AS SalesTotal FROM SalesList
GROUP BY ROLLUP (SalesYear, SalesQuartes) 
/*BELOW QUERY SUMS UP ACCORDING TO THE	MONTHS SPECIFIED */
SELECT  SalesYear,SalesQuartes , SalesMonth,SUM(SalesTotal) AS SalesTotal FROM SalesList
GROUP BY ROLLUP ( SalesYear, SalesQuartes,SalesMonth) 


/*GROUPING - determines whether the columns in the GROUP BY list have been aggregated (1) or (0)*/

SELECT SalesYear,
SalesQuartes, 
SUM(SalesTotal) AS SalesTotal ,
GROUPING(SalesQuartes) AS SalesQuarterGrp,
GROUPING(SalesYear) AS SYearGrp
FROM SalesList
GROUP BY ROLLUP(SalesYear, SalesQuartes);

/*GROUPING*/
SELECT 
CASE
WHEN GROUPING(SalesQuartes)=1 AND GROUPING(SalesYear)=0
THEN 'SubTotal'
WHEN GROUPING(SalesQuartes)=1 AND GROUPING(SalesYear)=1
THEN 'GrandTotal'
ELSE
CAST(SalesYear AS varchar(10)) /*CAST IS USED TO CONVERT ONE DATATYPE TO OTHER*/
END 
AS SalesYear,
SalesQuartes,
SUM(SalesTotal) AS SalesTotal 
FROM SalesList
GROUP BY ROLLUP(SalesYear,SalesQuartes)


/*ROW_NUMBER*/
WITH CTE AS (
SELECT SalesMonth,SalesTotal , 
ROW_NUMBER() OVER(ORDER BY NEWID())
AS RowNumber FROM SalesList 
)
SELECT 
    RowNumber ,SalesMonth,SUM(SalesTotal) AS SalesTotal 
FROM CTE 
GROUP BY ROLLUP(SalesMonth, RowNumber)


/*USING ROLL_NUMBER, GROUPING, ROLL_UP*/
WITH CTE AS (
SELECT SalesMonth,SalesTotal , 
ROW_NUMBER() OVER(ORDER BY NEWID())
AS RowNumber FROM SalesList 
)
 
SELECT  
CASE WHEN GROUPING(RowNumber) =1 THEN 'SubTotal'
ELSE SalesMonth
    END AS SalesMonth,SUM(SalesTotal) AS SalesTotal 
FROM CTE 
GROUP BY ROLLUP(SalesMonth, RowNumber)


/*USING ROLL_NUMBER, GROUPING, ROLL_UP  - WITHOUT ROLLING UP SALESMONTH*/
WITH CTE AS (
SELECT SalesMonth,SalesTotal , 
ROW_NUMBER() OVER(ORDER BY NEWID())
AS RowNumber FROM SalesList 
)
 
SELECT  
CASE WHEN GROUPING(RowNumber) =1 THEN 'SubTotal'
ELSE
    SalesMonth
    END AS SalesMonth,SUM(SalesTotal) AS SalesTotal 
FROM CTE 
GROUP BY ROLLUP(SalesMonth, RowNumber)
HAVING GROUPING(SalesMonth) = 0



/*STORED PROCEDURES*/

CREATE PROCEDURE SALES_MAN AS 
SELECT SALESMONTH, SALESQUARTES, SALESYEAR
FROM SalesList
WHERE SalesTotal=50;

EXEC SALES_MAN;


/*STORED PROCEDURES WITH MULTIPLE PARAMETERS*/

CREATE TABLE CUSTOMERS1 (CITY NVARCHAR(10), POSTALCODE NVARCHAR(10));
INSERT INTO CUSTOMERS1 VALUES ('VIZAG',535004);
INSERT INTO CUSTOMERS1 VALUES ('HYYD',535006);
INSERT INTO CUSTOMERS1 VALUES ('VJY',540098);
INSERT INTO CUSTOMERS1 VALUES ('LONDON','WA1 1DP');

CREATE PROCEDURE SelectAllCustomers @City nvarchar(30), @PostalCode nvarchar(10)
AS
SELECT * FROM Customers1 WHERE City = @City AND PostalCode = @PostalCode;

EXEC SelectAllCustomers @City = 'London', @PostalCode = 'WA1 1DP';

