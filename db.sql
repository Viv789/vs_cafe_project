CREATE DATABASE  people;

USE people;

CREATE TABLE people (
    person_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) ,
    age INT,
    PRIMARY KEY(person_id)
);

ALTER TABLE people
ADD email VARCHAR(255);

INSERT INTO people (first_name, last_name,age)
VALUES ('Lyra', 'Jones', 20);

INSERT INTO people (first_name, last_name, email)
VALUES ('Lyra', 'Jones', 'lyra@gmail.com');

INSERT INTO people (first_name, last_name, age, email)
VALUES ('Geoff', 'Dyer', 56, 'GDyer@gmail.com');

UPDATE people SET age = 23 Where first_name = 'Lyra'

ALTER TABLE people
DROP first_name NOT NULL;

DELETE FROM people Where last_name = 'Jones'

SELECT * FROM people WHERE age >= 18;

INSERT INTO people (first_name, last_name, age, email)
VALUES ('Henry', 'Miller', 45, 'HM@gmail.com');

INSERT INTO people (first_name, age, email)
VALUES ('Annie', 30, 'AWallace@gmail.com');

SELECT * FROM people WHERE age >= 18 AND age >=50;

INSERT INTO people (first_name, last_name,age)
VALUES ('Lyra', 'Jones', 23);

SELECT * FROM people WHERE age = 23 ORDER BY person_id;

CREATE TABLE person (
    id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY(id)
);

CREATE TABLE 