/*TCL COMMANDS*/

CREATE TABLE EMPLOYEES1 (
   ID INT NOT NULL,
   NAME VARCHAR (20) NOT NULL,
   AGE INT NOT NULL,
   ADDRESS CHAR (25),
   SALARY DECIMAL (18, 2),
   PRIMARY KEY (ID)
);

INSERT INTO EMPLOYEES1 VALUES 
(1, 'Ramesh', 32, 'Ahmedabad', 20000.00),
(2, 'Khilan', 25, 'Delhi', 15000.00),
(3, 'Kaushik', 23, 'Kota', 20000.00),
(4, 'Chaitali', 25, 'Mumbai',5000.00),
(5, 'Hardik', 27, 'Bhopal', 85000.00),
(6, 'Komal', 22, 'Hyderabad', 45000.00),
(7, 'Muffy', 24, 'Indore', 10000.00);
/*COMMIT*/
BEGIN TRANSACTION;
DELETE FROM EMPLOYEES1 WHERE AGE=22;
COMMIT;
SELECT * FROM EMPLOYEES1;
/*ROLLBACK*/
BEGIN TRANSACTION;
DELETE FROM EMPLOYEES1 WHERE ADDRESS='INDORE';
ROLLBACK;
SELECT * FROM EMPLOYEES1;
UPDATE EMPLOYEES1 SET ADDRESS='BHOPAL' WHERE AGE=27;
/*SAVEPOINT*/
BEGIN TRANSACTION
SAVE TRANSACTION S1
DELETE FROM EMPLOYEES1 WHERE ADDRESS='BHOPAL';

ROLLBACK TRANSACTION S1;
