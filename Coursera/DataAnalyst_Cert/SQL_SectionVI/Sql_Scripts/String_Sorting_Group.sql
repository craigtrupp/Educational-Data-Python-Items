-- Retrieve all employees whose address is in Elgin,IL.
SELECT EMP_ID, F_NAME, L_NAME, B_DATE
FROM EMPLOYEES
WHERE ADDRESS LIKE '%Elgin,IL%';

-- Retrieve all employees who were born during the 1970's. B_DATE column is a date data type
SELECT EMP_ID, F_NAME, L_NAME, B_DATE
FROM EMPLOYEES
WHERE B_DATE BETWEEN '01-01-1970' AND '12-31-1979';

-- Retrieve all employees in department 5 whose salary is between 60000 and 70000.
SELECT EMP_ID, F_NAME, L_NAME, SALARY
FROM EMPLOYEES
WHERE DEP_ID = 5 AND (SALARY BETWEEN 60000 AND 70000)




-- Retrieve a list of employees ordered by department ID.
SELECT EMP_ID, F_NAME, L_NAME, DEP_ID
FROM EMPLOYEES
ORDER BY DEP_ID;


-- Retrieve a list of employees ordered in descending order by department ID and within each department ordered alphabetically in descending order by last name.
SELECT EMP_ID, F_NAME, L_NAME, DEP_ID
FROM EMPLOYEES
ORDER BY DEP_ID DESC, L_NAME DESC;

-- In SQL problem 2 (Exercise 2 Problem 2), use department name instead of department ID. 
-- Retrieve a list of employees ordered by department name, and within each department ordered alphabetically in descending order by last name.
SELECT emp.F_NAME, emp.L_NAME, dept.DEP_NAME 
FROM EMPLOYEES AS emp 
	INNER JOIN DEPARTMENTS AS dept
	ON emp.DEP_ID = dept.DEPT_ID_DEP
ORDER BY dept.DEP_NAME, emp.L_NAME DESC;




-- Grouping

-- For each department ID retrieve the number of employees in the department.
SELECT DEP_ID, COUNT(*) AS DepartmentCount
FROM EMPLOYEES
GROUP BY DEP_ID;

-- For each department retrieve the number of employees in the department, and the average employee salary in the department..
SELECT DEP_ID, COUNT(*) AS DepartmentCount, ROUND(AVG(SALARY), 2)
FROM EMPLOYEES
GROUP BY DEP_ID;

-- With Aliases
SELECT DEP_ID, COUNT(*) AS "NUM_EMPLOYEES", AVG(SALARY) AS "AVG_SALARY"
FROM EMPLOYEES
GROUP BY DEP_ID;

-- Order Above by Average Salary
SELECT DEP_ID, COUNT(*) AS "NUM_EMPLOYEES", AVG(SALARY) AS "AVG_SALARY"
FROM EMPLOYEES
GROUP BY DEP_ID
ORDER BY AVG_SALARY;

-- In SQL problem 4 (Exercise 3 Problem 4), limit the result to departments with fewer than 4 employees.
SELECT DEP_ID, COUNT(*) AS "NUM_EMPLOYEES", AVG(SALARY) AS "AVG_SALARY"
FROM EMPLOYEES
GROUP BY DEP_ID
HAVING COUNT(*) < 4
ORDER BY AVG_SALARY;