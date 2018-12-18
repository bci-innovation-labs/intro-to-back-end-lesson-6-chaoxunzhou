1. Database is seems like a library of data. It saves many data and people have access to read,copy and edit it.
2. it's include:
Hierarchical databases.Looks like a tree structure, and easy to see the realtion of each data.
Network databases.  It more connections can be made between different types of data,looks more like a cobweb or interconnected network of records.
Relational databases.Relational databases work on each table has a key field that uniquely indicates each row, and that these key fields can be used to connect one table of data to another.
Object-oriented databasesThe object-oriented database derivation is the integrity of object-oriented programming language systems and consistent systems.




CREATE TABLE vegetables (id INTEGER, name VARCHAR(20), description VARCHAR(255), created_at DATE);
INSERT INTO vegetables(id, name, description, created_at)
VALUES 
(1,'Apple','The round fruit of a tree of the rose family, which typically has thin red or green skin and crisp flesh. Many varieties have been developed as dessert or cooking fruit or for making cider.','2018-12-01 19:39:53.442867'),
(2,'Banana','A banana is an edible fruit – botanically a berry – produced by several kinds of large herbaceous flowering plants in the genus Musa.','2018-12-5 19:39:53.442867'),
(3,'Cucumber','Cucumber is a widely cultivated plant in the gourd family, Cucurbitaceae. It is a creeping vine that bears cucumiform fruits that are used as vegetables', '2018-12-10 19:39:53.442867');

a) id 2  name Banana
b) id 1  name Apple
