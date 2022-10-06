--Find the total number of crimes recorded in the CRIME table
SELECT COUNT(*) FROM CHICAGO_CRIME_DATA;
-- Make sure ID not null
SELECT COUNT(*) FROM CHICAGO_CRIME_DATA WHERE ID IS NOT NULL;

-- List community areas with per capita income less than 11000.
SELECT COMMUNITY_AREA_NAME, PER_CAPITA_INCOME FROM CENSUS_DATA WHERE PER_CAPITA_INCOME  < 11000 ORDER BY PER_CAPITA_INCOME DESC;
-- Just to See What we're working with
SELECT COMMUNITY_AREA_NAME, PER_CAPITA_INCOME FROM CENSUS_DATA WHERE PER_CAPITA_INCOME BETWEEN 8201 AND 20000 ORDER BY PER_CAPITA_INCOME;


-- List all case numbers for crimes involving minors?(children are not considered minors for the purposes of crime analysis) - CRIME HAS COMMUNITY_AREA int VALUE
SELECT * FROM CHICAGO_CRIME_DATA LIMIT 5;
-- Doesn't appear to be a key/join in the census detail that could somehow uniquely attribute a crime to a particular age (checking out the description)
SELECT DISTINCT(DESCRIPTION) FROM CHICAGO_CRIME_DATA; -- ~100 here
SELECT COUNT(DISTINCT(DESCRIPTION)) FROM CHICAGO_CRIME_DATA WHERE LOWER(DESCRIPTION) LIKE '%minor%'; -- Only 2 huzzah

-- Submission
SELECT CASE_NUMBER, DESCRIPTION FROM CHICAGO_CRIME_DATA  WHERE LOWER(DESCRIPTION) LIKE '%minor%';



-- List all kidnapping crimes involving a child?
SELECT DISTINCT(PRIMARY_TYPE) FROM CHICAGO_CRIME_DATA WHERE LOWER(PRIMARY_TYPE) LIKE '%kidnap%';
-- How many crimes within our table are a kidnapping type
SELECT COUNT(*) AS Kidnapping_Crime_Count
FROM CHICAGO_CRIME_DATA
WHERE LOWER(PRIMARY_TYPE) LIKE '%kidnap%';

-- Submission
SELECT PRIMARY_TYPE, DESCRIPTION, CASE_NUMBER, ID FROM CHICAGO_CRIME_DATA WHERE LOWER(PRIMARY_TYPE) LIKE '%kidnap%';



-- What kinds of crimes were recorded at schools? - Crime_Data Has LocationDescription

-- Unique counts of crime type and descriptions (can be different) for kinds of crimes where location description has school in detail
SELECT PRIMARY_TYPE, DESCRIPTION, COUNT(*) AS CrimeTypeCounts 
FROM CHICAGO_CRIME_DATA 
WHERE LOWER(LOCATION_DESCRIPTION) LIKE '%school%'
GROUP BY PRIMARY_TYPE, DESCRIPTION
ORDER BY CrimeTypeCounts DESC;

-- And location Grouping?
SELECT PRIMARY_TYPE, DESCRIPTION, LOCATION_DESCRIPTION, COUNT(*) AS CrimeTypeCounts 
FROM CHICAGO_CRIME_DATA 
WHERE LOWER(LOCATION_DESCRIPTION) LIKE '%school%'
GROUP BY PRIMARY_TYPE, DESCRIPTION, LOCATION_DESCRIPTION
ORDER BY CrimeTypeCounts DESC;



-- List the average safety score for each type of school. (Lots of Columns in School)
SELECT * FROM SYSCAT.COLUMNS WHERE tabname = 'CHICAGO_PUBLIC_SCHOOLS' and LOWER(COLNAME) LIKE '%safety%';

SELECT * FROM CHICAGO_PUBLIC_SCHOOLS LIMIT 1;

-- Distinct Counts for wonky column 
SELECT DISTINCT("Elementary, Middle, or High School") FROM CHICAGO_PUBLIC_SCHOOLS;

-- Not altering table column (previously done in other section exercise) -- not the best column name though!
-- Can get average safety
SELECT "Elementary, Middle, or High School", AVG(SAFETY_SCORE) AS AverageTypeScore
FROM CHICAGO_PUBLIC_SCHOOLS
GROUP BY "Elementary, Middle, or High School"
ORDER BY AverageTypeScore DESC;



-- List 5 community areas with highest % of households below poverty line
SELECT * FROM CENSUS_DATA LIMIT 3;

-- Validate Community Area Number and Name Has Single Counts
SELECT COMMUNITY_AREA_NUMBER, COMMUNITY_AREA_NAME, COUNT(*) As Community_Area_Number_Name
FROM CENSUS_DATA
GROUP BY COMMUNITY_AREA_NUMBER, COMMUNITY_AREA_NAME
ORDER BY Community_Area_Number_Name DESC;

SELECT COMMUNITY_AREA_NUMBER, COMMUNITY_AREA_NAME, PERCENT_HOUSEHOLDS_BELOW_POVERTY 
FROM CENSUS_DATA
ORDER BY PERCENT_HOUSEHOLDS_BELOW_POVERTY DESC 
LIMIT 5;



-- Which community area is most crime prone? (Crime : District, Ward, CommunityArea_Number) - Get Community Name from implicit join and count of grouped by rows form join
SELECT CCD.COMMUNITY_AREA_NUMBER AS Community_Area, CNS.COMMUNITY_AREA_NAME, COUNT(*) AS Total_Crime_Counts
FROM CHICAGO_CRIME_DATA CCD, CENSUS_DATA CNS
WHERE CCD.COMMUNITY_AREA_NUMBER = CNS.COMMUNITY_AREA_NUMBER
GROUP BY CCD.COMMUNITY_AREA_NUMBER, CNS.COMMUNITY_AREA_NAME
ORDER BY Total_Crime_Counts DESC 
LIMIT 1;



-- Use a sub-query to find the name of the community area with highest hardship index
SELECT COMMUNITY_AREA_NAME, HARDSHIP_INDEX
FROM CENSUS_DATA 
WHERE HARDSHIP_INDEX = (SELECT MAX(HARDSHIP_INDEX) FROM CENSUS_DATA);


-- Use a sub-query to determine the Community Area Name with most number of crimes?
-- -- Note here that running a count (agg type function won't work with a subquery column usage so count must occur in order by after groupby statement on single column)
SELECT * FROM CHICAGO_CRIME_DATA LIMIT 1;

SELECT COMMUNITY_AREA_NAME 
FROM CENSUS_DATA
WHERE COMMUNITY_AREA_NUMBER = (SELECT COMMUNITY_AREA_NUMBER 
        FROM CHICAGO_CRIME_DATA 
        GROUP BY COMMUNITY_AREA_NUMBER 
        ORDER BY COUNT(COMMUNITY_AREA_NUMBER) DESC 
        LIMIT 1
			); 




 

