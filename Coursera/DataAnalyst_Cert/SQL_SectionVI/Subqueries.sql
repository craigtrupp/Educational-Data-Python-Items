-- Common Subquery Syntax

-- SELECT column_name [, column_name ]
-- FROM table1 [, table2 ]
-- WHERE column_name OPERATOR
--    (SELECT column_name [, column_name ]
--    FROM table1 [, table2 ]
--    WHERE condition);


-- Exercises


-- Execute a failing query (i.e. one which gives an error) to retrieve all employees records whose salary is lower than the average salary.
SELECT EMP_ID, F_NAME, L_NAME
FROM EMPLOYEES 
WHERE SALARY < AVG(SALARY);
-- Invalid use of an aggregate function or OLAP function Result 


-- Execute a working query using a sub-select to retrieve all employees records whose salary is lower than the average salary.
SELECT EMP_ID, F_NAME, L_NAME, SALARY, (SELECT ROUND(AVG(SALARY)) AS AvgSalary FROM EMPLOYEES )
FROM EMPLOYEES 
WHERE SALARY < (SELECT AVG(SALARY) FROM employees);

-- Sample Result
-- EMP_ID , F_NAME, L_NAME, SALARY, AvgSalary
-- E1003 | Steve | Wells | 50000.00 | 72000.00



-- Execute a Column Expression that retrieves all employees records with EMP_ID, SALARY and maximum salary as MAX_SALARY in every row.
SELECT EMP_ID, SALARY, (SELECT MAX(SALARY) FROM EMPLOYEES) AS MaxSalary
FROM EMPLOYEES;

-- Sample Result
-- EMP_ID, SALARY, MaxSalary
-- E1001 | 100000.00 | 100000.00 
-- E1004 | 60000.00 | 100000.00



-- Execute a Table Expression for the EMPLOYEES table that excludes columns with sensitive employee data (i.e. does not include columns: SSN, B_DATE, SEX, ADDRESS, SALARY).
SELECT *
FROM (SELECT EMP_ID, F_NAME, L_NAME, JOB_ID, MANAGER_ID, DEP_ID FROM EMPLOYEES) AS EMP4ALL;