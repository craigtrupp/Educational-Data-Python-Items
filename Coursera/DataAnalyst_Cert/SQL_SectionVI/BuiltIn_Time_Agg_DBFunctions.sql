-- Query A1: Enter a function that calculates the total cost of all animal rescues in the PETRESCUE table.
SELECT SUM(COST) AS Total_Sum
FROM PETRESCUE;

-- Query A2: Enter a function that displays the total cost of all animal rescues in the PETRESCUE table in a column called SUM_OF_COST.
SELECT SUM(COST) AS SUM_OF_COST
FROM PETRESCUE;

-- Query A3: Enter a function that displays the maximum quantity of animals rescued.
SELECT MAX(QUANTITY) AS Max_Quantity
FROM PETRESCUE;

-- Query A4: Enter a function that displays the average cost of animals rescued.
SELECT ROUND(AVG(COST), 2) AS Avg_Rescue_Cost
FROM PETRESCUE;

-- Query A5: Enter a function that displays the average cost of rescuing a dog.
-- Bear in mind the cost of rescuing one dog on a day can be different from another day. So you will have to use and average of averages.
SELECT ROUND(AVG(COST/QUANTITY),2) AS Avg_Rescue_Cost_Dogs
FROM PETRESCUE 
WHERE LCASE(ANIMAL) = 'dog';

-- Avg_Rescue_Cost_Dogs -- Value Gained by performing the Average over the rows results below
-- 127.27

-- Dig a little deeper (Each row has a quantity for total)
SELECT (COST/QUANTITY) AS c_divided_q , RESCUEDATE, COST, QUANTITY
FROM PETRESCUE 
WHERE LCASE(ANIMAL) = 'dog';

-- c_divided_q , RESCUEDATE, COST, QUANTITY
-- 222.220 | 2018-06-01 | 666.66 | 3
-- 100.000 | 2018-06-04 | 100 | 1
-- 75.75 | 2018-06-10 | 75.75 | 1
-- 111.11 | 2018-06-15 | 222.22 | 2

-- c_divided_q value for each row is gathered to see how an Avg is gathered. For each row(s) fitting the condition take the value of the cost/quantity and get the avg for all of these values for found rows (4)
-- 222.22 + 100 + 75.75 + 111.11 = (509.08 / 4) = 127.27




--Query B1: Enter a function that displays the rounded cost of each rescue.
SELECT ROUND(COST) AS Rounded_Cost
FROM PETRESCUE;

--Query B2: Enter a function that displays the length of each animal name.
SELECT LENGTH(ANIMAL), ANIMAL
FROM PETRESCUE;

--Query B3: Enter a function that displays the animal name in each rescue in uppercase.
SELECT UCASE(ANIMAL), ANIMAL
FROM PETRESCUE;

--Query B4: Enter a function that displays the animal name in each rescue in uppercase without duplications.
SELECT DISTINCT(UCASE(ANIMAL)), ANIMAL
FROM PETRESCUE;

--Query B5: Enter a query that displays all the columns from the PETRESCUE table, where the animal(s) rescued are cats. Use cat in lower case in the query.
SELECT *
FROM PETRESCUE 
WHERE LCASE(ANIMAL) = 'cat';




--Query C1: Enter a function that displays the day of the month when cats have been rescued.
SELECT ID, ANIMAL, RESCUEDATE, DAY(RESCUEDATE) AS RescueDay
FROM PETRESCUE 
WHERE LCASE(ANIMAL) = 'cat';

--Query C2: Enter a function that displays the number of rescues on the 5th month.
SELECT SUM(QUANTITY) AS TotalRescues
FROM PETRESCUE
WHERE MONTH(RESCUEDATE) = '05';

--Query C3: Enter a function that displays the number of rescues on the 14th day of the month.
SELECT SUM(QUANTITY) AS TotalRescues_14
FROM PETRESCUE 
WHERE DAY(RESCUEDATE) = '14';

--Query C4: Animals rescued should see the vet within three days of arrivals. Enter a function that displays the third day from each rescue.
SELECT RESCUEDATE, (RESCUEDATE + 3 DAYS) AS CheckUpDate
FROM PETRESCUE;

--Query C5: Enter a function that displays the length of time the animals have been rescued; the difference between today’s date and the rescue date.
SELECT RESCUEDATE, (CURRENT_DATE - RESCUEDATE) AS Duration
FROM PETRESCUE;

-- RESCUEDATE, Duration
-- 2018-05-29 | 40405 
-- 2018-06-01  | 40402

-- Return for Duration column is y/mm/dd (years/months/day) = 4 years, 4 months, 5 days from today's date (10/3/2022)


