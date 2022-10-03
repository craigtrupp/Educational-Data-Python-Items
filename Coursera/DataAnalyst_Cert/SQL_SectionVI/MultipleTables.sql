-- How does an Implicit version of CROSS JOIN (also known as Cartesian Join) statement syntax look?
SELECT column_name(s)
FROM table1, table2;

-- How does an Implicit version of INNER JOIN statement syntax look?
SELECT column_name(s)
FROM table1, table2
WHERE table1.column_name = table2.column_name;


SELECT * FROM JOBS LIMIT 5;
SELECT * FROM EMPLOYEES LIMIT 5;

----  Accessing Multiple Tables with Sub-Queries

-- Retrieve only the EMPLOYEES records that correspond to jobs in the JOBS table. (One Join the Rest Sub-Queries)
SELECT E.EMP_ID, E.F_NAME, E.L_NAME, E.JOB_ID AS EmpJbIDVal, J.JOB_TITLE, J.JOB_IDENT AS JobJbIDVal
FROM EMPLOYEES E, JOBS J 
WHERE E.JOB_ID = J.JOB_IDENT;

SELECT * 
FROM EMPLOYEES 
WHERE JOB_ID IN (SELECT JOB_IDENT FROM JOBS);

-- Retrieve only the list of employees whose JOB_TITLE is Jr. Designer.
SELECT *
FROM EMPLOYEES
WHERE JOB_ID IN (SELECT JOB_IDENT FROM JOBS WHERE JOB_TITLE LIKE '%Jr. Designer%'); 

-- Retrieve JOB information and who earn more than $70,000.
SELECT *
FROM JOBS
WHERE JOB_IDENT IN (SELECT JOB_ID FROM EMPLOYEES WHERE SALARY > 70000); 

-- Retrieve JOB information and whose birth year is after 1976.
SELECT *
FROM JOBS
WHERE JOB_IDENT IN (SELECT JOB_ID FROM EMPLOYEES WHERE YEAR(B_DATE) > 1976);

-- Retrieve JOB information for female employees whose birth year is after 1976.
SELECT *
FROM JOBS
WHERE JOB_IDENT IN (SELECT JOB_ID FROM EMPLOYEES WHERE YEAR(B_DATE) > 1976 AND SEX = 'F');



----  Accessing Multiple Tables with Implicit Joins

-- Perform an implicit cartesian/cross join between EMPLOYEES and JOBS tables.
select * from employees, jobs;

-- Result Set is simply all data from each (not a lot value in a cartesian and confusing return)


-- Retrieve only the EMPLOYEES records that correspond to jobs in the JOBS table.
SELECT E.F_NAME, E.L_NAME, E.EMP_ID, E.JOB_ID AS EmployeeJobId, J.JOB_IDENT AS JobsJobId, J.JOB_TITLE 
FROM EMPLOYEES E, JOBS J
WHERE E.JOB_ID = J.JOB_IDENT;

-- Redo the previous query, but retrieve only the Employee ID, Employee Name and Job Title. (No Job_Title column in Employees so doesn't require alias)
SELECT EMP_ID,F_NAME,L_NAME, JOB_TITLE 
	FROM employees E, jobs J 
	WHERE E.JOB_ID = J.JOB_IDENT;
	
-- Redo the previous query, but specify the fully qualified column names with aliases in the SELECT clause
SELECT EMP_ID,F_NAME,L_NAME, J.JOB_TITLE 
	FROM employees E, jobs J 
	WHERE E.JOB_ID = J.JOB_IDENT;