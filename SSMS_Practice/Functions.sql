/*FUNCTIONS*/

/*STRING FUNCTIONS*/
/*GIVES THE ASCII VALUE OF LEFT-MOST CHARACTER*/
SELECT ASCII('AB');

/*GIVES THE CHARACTER EQUVALENT TO ASCII*/
SELECT CHAR(66);

/*GIVES THE LENGTH OF THE CHARACTERS*/
SELECT len ('WIDESKILLS');

/*LOWERS THE CHARACTERS*/
SELECT LOWER('KAVYA');

/*REPLACES Y WITH IES*/
SELECT REPLACE('COUNTRY','Y','IES');

/*REVERSE*/
SELECT REVERSE('INDIA');

/*STR-(NUMBER,LENGTH,DECIMAL)*/
SELECT STR(134.97,5,1);

/*UPPER*/
SELECT UPPER('Kavya');


/*DATE FUNCTIONS*/
/*GET DATE -  returns YY-MM-DD HH:MM:SS*/
SELECT GETDATE() ;

/*DATEADD - ADDS TO THE GIVEN DATE*/ 
SELECT DATEADD (YY, 2, '2010-02-03');

/*DATEDIFF*/
SELECT datediff ( YYYY, convert (date, '2006-05-06'), convert ( date, '2009-01-01'));
SELECT datediff ( MONTH, convert (datetime, '2006-05-06'), convert ( datetime, '2009-01-01'));
SELECT datediff ( DAY, convert (datetime, '2006-05-06'), convert ( datetime, '2009-01-01'));


/*DATEPART - RETRIVES YEAR,MONTH,DAY*/
SELECT DATEPART (YY, '2008-01-01');
SELECT DATEPART (MM, '2008-01-01');
SELECT DATEPART (DD, '2008-01-21');

/*GIVES THE DATE OF MONTH*/
SELECT DAY('2023-12-21');

/*DATENAME - GIVES THE DAY NAME*/
SELECT DATENAME(WEEKDAY, '2023-12-21');

/*GIVES THE DAY NAME IN SHORT- THU */
SELECT FORMAT(CAST('2023-12-21' AS DATE), 'ddd');


/*MATHMATICAL FUNCTIONS*/
/*ABS- GIVES ABSOLUTE VALUE*/
SELECT ABS(-56.787878);

/*CEILING - GIVES THE NEXT VALUE*/
SELECT CEILING(13.16);

/*GIVES THE PREVIOUS VALUE*/
SELECT FLOOR(13.86);

SELECT ROUND(23.566667,1); /*23.600000*/

/*GIVES EXPONENTIAL VALUE*/
SELECT EXP(2);

/*SIN,COS,TAN,COT - RETURNS ANGLE IN RADIANS*/
SELECT SIN(90);

/*LOGARITHMIC VALUES*/
SELECT LOG(2);

SELECT * FROM PRODUCTS;



/*RANK FUNCTIONS*/
/*ROW_NUMBER()- GIVES A CONSECUTIVE NUMBER OF RANKS FOR DUPLICATES TOO*/
SELECT SI,SNAME,PRICE,ROW_NUMBER() OVER(ORDER BY PRICE DESC) AS RANK FROM PRODUCTS;

INSERT INTO PRODUCTS VALUES(109,'LAPTOP',70000,59);

/*RANK() - DUPLICATES HAVE SAME RANKS AND JUMPS ONE RANK FOR THE NEXT ONE*/
SELECT SI,SNAME,PRICE,RANK() OVER (ORDER BY PRICE DESC) AS RANK FROM PRODUCTS;

/*DENSE_RANK() - DUPLICATES HAVE SAME RANKS AND DONT JUMP*/
SELECT SI,SNAME,PRICE,DENSE_RANK() OVER (ORDER BY PRICE DESC) AS RANK FROM PRODUCTS;

INSERT INTO PRODUCTS VALUES(109,'LAPTOP',80000,59);
INSERT INTO PRODUCTS VALUES(109,'LAPTOP',90000,59);
INSERT INTO PRODUCTS VALUES(109,'LAPTOP',100000,59);
INSERT INTO PRODUCTS VALUES(109,'LAPTOP',50000,59);
INSERT INTO PRODUCTS VALUES(109,'LAPTOP',80000,59);

/*NTILE() - GROUPS THE RANK BASED ON ARGUMENTS GIVEN */
SELECT SI,SNAME,PRICE,NTILE(10) OVER (ORDER BY PRICE DESC) AS RANK FROM PRODUCTS WHERE PRICE>=40000;


/*SYSTEM FUNCTIONS*/
/*HOST_ID*/
SELECT HOST_ID() AS HOST_NO;

/*HOST_NAME() - PROVIDES DESKTOP_NAME*/
SELECT HOST_NAME() AS HOST_NAM;

/*SUSER_ID*/
SELECT SUSER_ID('KAVYA_GUNDALA') AS SUSER_IDN;

/*USER_ID*/
SELECT USER_ID('KAVYA_GUNDALA') AS USER_IDN;

/*DB_NAME - GIVES DATABASE NAME*/
SELECT db_name ();

/*AGGREGATE FUNCTIONS*/
/*AVG*/
SELECT 'AVERAGE' = AVG(PRICE) FROM PRODUCTS;

/*COUNT*/
SELECT 'UNIQUE_COUNT' = COUNT(DISTINCT PRICE) FROM PRODUCTS;

/*MIN*/
SELECT 'MINIMUM_PRICE' = MIN(PRICE) FROM PRODUCTS;

/*MAX*/
SELECT 'MAXIMUM_PRICE' = MAX(PRICE) FROM PRODUCTS;

/*SUM*/
SELECT 'SUM_PRICE' = SUM(PRICE) FROM PRODUCTS;