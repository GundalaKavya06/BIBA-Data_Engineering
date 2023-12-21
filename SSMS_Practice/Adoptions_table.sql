CREATE TABLE ADOPTIONS(ANIMAL_ID INT NOT NULL, NAME VARCHAR(20),CONTACT VARCHAR(20),DATES DATETIME);

INSERT INTO adoptions (animal_id, name, contact, DATES) VALUES ('4', 'Pinocchio', 'realboy', CURRENT_TIMESTAMP);
INSERT INTO adoptions (animal_id, name, contact, DATES) VALUES ('5', 'Patalie', 'poodlequeen', CURRENT_TIMESTAMP);
INSERT INTO adoptions (animal_id, name, contact, DATES) VALUES ('6',  'Ella', 'ellacrew',CURRENT_TIMESTAMP);

SELECT * FROM ADOPTIONS;

SELECT * FROM adoptions ORDER BY DATES DESC;

