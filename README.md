# Intro To Back End - Lesson 6

## Please submit answers in your own words

1. What is a database? (2-3 sentances)

2. Name three types of databases and give one sentance explaining each kind

3. Given the following database table, write the result that the following SQL would return (Example http://sqlfiddle.com/#!17/f95cb/4/0)

table: `vegetables`

|id|name|description|created_at|
|---|---|---|---|
|1|Apple|the round fruit of a tree of the rose family, which typically has thin red or green skin and crisp flesh. Many varieties have been developed as dessert or cooking fruit or for making cider.|2018-12-01 19:39:53.442867|
|2|Banana|A banana is an edible fruit – botanically a berry – produced by several kinds of large herbaceous flowering plants in the genus Musa.|2018-12-5 19:39:53.442867|
|3|Cucumber|Cucumber is a widely cultivated plant in the gourd family, Cucurbitaceae. It is a creeping vine that bears cucumiform fruits that are used as vegetables|2018-12-10 19:39:53.442867|

a) 
```
SELECT id, name FROM vegetables where id = 2
```
b) 
```
SELECT id, name FROM vegetables where created_at < '2018-12-5 19:39:53.442867'
```
