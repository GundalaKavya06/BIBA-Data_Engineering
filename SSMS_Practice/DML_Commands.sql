CREATE DATABASE PET_ADOPTION;
USE PET_ADOPTION;


CREATE TABLE animals (id INT NOT NULL, name CHAR(20), breed CHAR(20), color CHAR(20), gender CHAR(6), status INTEGER);

SELECT * FROM ANIMALS; 

/*INSERT STATEMENTS*/
INSERT INTO ANIMALS(id,name,breed,color,gender,status) VALUES ('1','Bellyflop', 'Beagle', 'Brown', 'Male', 0);
INSERT INTO ANIMALS(id,name,breed,color,gender,status) VALUES ('2','Snowy', 'Husky', 'White', 'Female', 0);
INSERT INTO ANIMALS(id,name,breed,color,gender,status) VALUES ('3','Princess', 'Pomeranian', 'Black', 'Female', 0);
INSERT INTO ANIMALS(id,name,breed,color,gender,status) VALUES ('4','Cricket', 'Chihuahua', 'Brown', 'Male', 0);
INSERT INTO ANIMALS(id,name,breed,color,gender,status) VALUES ('5','Princess', 'Poodle', 'Purple', 'Female', 0);
INSERT INTO ANIMALS(id,name,breed,color,gender,status) VALUES ('6','Spot', 'Dalmation', 'Black and White', 'Male', 0);

/*SELECT STATEMENTS*/
SELECT * FROM ANIMALS;
SELECT BREED FROM ANIMALS;
SELECT NAME FROM ANIMALS WHERE GENDER='FEMALE';

/*UPDATE STATEMENTS*/
UPDATE ANIMALS SET COLOR='BROWN' WHERE ID='1';
UPDATE ANIMALS SET NAME='PRINCE' WHERE COLOR='PURPLE';

/*DELETE STATEMENTS*/
DELETE FROM ANIMALS WHERE NAME='PRINCE'; 

SELECT * FROM ANIMALS;

ALTER TABLE animals ADD species CHAR(10);

UPDATE animals SET species = 'Dog';

SELECT * FROM ANIMALS;

INSERT INTO animals (id, name, species, breed, color, gender, status) VALUES ('7', 'Meowmix', 'Cat', 'Munchkin', 'Yellow', 'Female', 0);
INSERT INTO animals (id, name, species, breed, color, gender, status) VALUES ('8', 'Ash', 'Cat', 'Persian', 'Gray', 'Female', 0);
INSERT INTO animals (id, name, species, breed, color, gender, status) VALUES ('9', 'Tiger', 'Cat', 'Bengal', 'Brown', 'Male', 0);

SELECT * FROM ANIMALS;

CREATE TABLE shelters (id INTEGER, name CHAR(20), location char(30));

INSERT INTO shelters (id, name, location) VALUES (1, 'Animals 4 Homes', 'Red City');

ALTER TABLE animals ADD shelter INTEGER;

UPDATE animals SET shelter = 1;

INSERT INTO shelters (id, name, location) VALUES (2, 'Adopt A Buddy', 'Green Town');
INSERT INTO shelters (id, name, location) VALUES (3, 'Fluffy Animals', 'Blue Hills');


SELECT * FROM SHELTERS;

INSERT INTO animals (id, name, shelter, species, breed, color, gender, status) VALUES ('10', 'Snoops', 2, 'Dog', 'Beagle', 'Brown', 'Male', 0);
INSERT INTO animals (id, name, shelter, species, breed, color, gender, status) VALUES ('11', 'Salt', 2, 'Cat', 'Turkish Angora', 'White', 'Female', 0);
INSERT INTO animals (id, name, shelter, species, breed, color, gender, status) VALUES ('12', 'Fuzz', 3, 'Dog', 'Papillon', 'Gray', 'Male', 0);


CREATE INDEX animal_shelter ON animals (shelter);
SELECT * FROM animals JOIN shelters ON animals.shelter = shelters.id;

SELECT * FROM adoptions JOIN animals ON adoptions.animal_id = animals.id WHERE animals.shelter = 1;