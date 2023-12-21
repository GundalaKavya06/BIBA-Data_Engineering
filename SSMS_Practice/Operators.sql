USE xstream_db;

CREATE TABLE employees (emp_id INT, emp_name VARCHAR(255), 
                                  emp_city VARCHAR(255),
                                  emp_country VARCHAR(255),
                                  PRIMARY KEY (emp_id));

INSERT INTO employees VALUES (101, 'Utkarsh Tripathi', 'Varanasi', 'India'),
                            (102, 'Abhinav Singh', 'Varanasi', 'India'), 
                            (103, 'Utkarsh Raghuvanshi', 'Varanasi', 'India'),
                            (104, 'Utkarsh Singh', 'Allahabad', 'India'),
                            (105, 'Sudhanshu Yadav', 'Allahabad', 'India'),
                            (106, 'Ashutosh Kumar', 'Patna', 'India');
/*AND OPERATOR*/
SELECT * FROM employees WHERE emp_city = 'Allahabad' AND emp_country = 'India';
/*IN OPERATOR*/
SELECT * FROM employees WHERE emp_city IN ('Allahabad', 'Patna');
/*NOT OPERATOR*/
SELECT * FROM employees WHERE emp_city NOT LIKE 'A%';
/*OR OPERATOR*/
SELECT * FROM employees WHERE emp_city = 'Varanasi' OR emp_country = 'India';
/*LIKE OPERATOR*/
SELECT * FROM employees WHERE emp_city LIKE 'P%'; 
/*BETWEEN OPERATOR*/
SELECT * FROM employees WHERE emp_id BETWEEN 101 AND 104;
/*ALL OPERATOR*/
SELECT * FROM employees WHERE emp_id = ALL 
                (SELECT emp_id FROM employees WHERE emp_city = 'Varanasi');
/*ANY OPERATOR*/
SELECT * FROM employees WHERE emp_id = ANY
                (SELECT emp_id FROM employees WHERE emp_city = 'Varanasi');
/*EXISTS OPERATOR*/
SELECT emp_name FROM employees WHERE EXISTS
                (SELECT emp_id FROM employees WHERE emp_city = 'Patna');

/*SOME OPERATOR*/
SELECT * FROM employees WHERE emp_id < SOME 
                (SELECT emp_id FROM employees WHERE emp_city = 'Patna');


/*DISTINCT OPERATIONS*/
CREATE TABLE students (
  ROLL_NO INT,
  NAME VARCHAR(50),
  ADDRESS VARCHAR(100),
  PHONE VARCHAR(20),
  AGE INT
);

INSERT INTO students (ROLL_NO, NAME, ADDRESS, PHONE, AGE)
VALUES 
  (1, 'Shubham Kumar', '123 Main Street, Bangalore', '9876543210', 23),
  (2, 'Shreya Gupta', '456 Park Road, Mumbai', '9876543211', 23),
  (3, 'Naveen Singh', '789 Market Lane, Delhi', '9876543212', 26),
  (4, 'Aman Chopra', '246 Forest Avenue, Kolkata', '9876543213', 22),
  (5, 'Aditya Patel', '7898 Ocean Drive, Chennai', '9876543214', 27),
  (6, 'Avdeep Desai', '34 River View, Hyderabad', '9876543215', 24);
 Select * from students;

 SELECT DISTINCT NAME FROM students;





