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
