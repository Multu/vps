# Query a count of the number of cities in CITY having
# a Population larger than 100000.

SELECT 
    COUNT(*)
FROM
    CITY
WHERE POPULATION > 100000;


# Query the total population of all cities in CITY
# where District is California.

SELECT 
    SUM(POPULATION)
FROM
    CITY
WHERE DISTRICT = 'California';


# Query the average population of all cities in CITY
# where District is California.

SELECT 
    AVG(POPULATION)
FROM
    CITY
WHERE DISTRICT = 'California';


# Query the average population for all cities in CITY,
# rounded down to the nearest integer.

SELECT 
    FLOOR(AVG(POPULATION))
FROM
    CITY
    

# Query the sum of the populations for all Japanese 
# cities in CITY. The COUNTRYCODE for Japan is JPN.

SELECT 
    SUM(POPULATION)
FROM
    CITY
WHERE COUNTRYCODE = 'JPN';


# Query the difference between the maximum and minimum
# populations in CITY.

SELECT 
    MAX(POPULATION) - MIN(POPULATION)
FROM
    CITY
    
    
# Samantha was tasked with calculating the average monthly salaries
# for all employees in the EMPLOYEES table, but did not realize 
# her keyboard's 0 key was broken until after completing the calculation. 
# She wants your help finding the difference between her miscalculation
# (using salaries with any zeros removed), and the actual average salary.
#
# Write a query calculating the amount of error (i.e.: actual - miscalculated
# average monthly salaries), and round it up to the next integer.

SELECT
   CEIL(AVG(Salary) - AVG(REPLACE(Salary, '0', '')))
FROM 
    EMPLOYEES
    
    
# We define an employee's total earnings to be their monthly 
# salary * months worked, and the maximum total earnings to be 
# the maximum total earnings for any employee in the Employee table. 
# Write a query to find the maximum total earnings for all employees
# as well as the total number of employees who have maximum total earnings. 
# Then print these values as 2 space-separated integers.

SELECT
    (months * salary) as total_earn, COUNT(*)
FROM
    Employee
GROUP BY total_earn
ORDER BY total_earn DESC
LIMIT 1


# Query the following two values from the STATION table:
# 1. The sum of all values in LAT_N rounded to a scale of 2 decimal places.
# 2. The sum of all values in LONG_W rounded to a scale of 2 decimal places.

SELECT 
    ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2)
FROM 
    STATION
    
    
# Query the sum of Northern Latitudes (LAT_N) from STATION having
# values greater than 38.7880 and less than 137.2345. Truncate 
# your answer to 4 decimal places.

SELECT 
    ROUND(SUM(LAT_N), 4)
FROM
    STATION
WHERE
    LAT_N > 38.7880 AND LAT_N < 137.2345    
    
    
# Query the greatest value of the Northern Latitudes (LAT_N) from STATION
# that is less than 137.2345. Truncate your answer to  decimal places.

SELECT
    ROUND(MAX(LAT_N), 4)
FROM 
    STATION
WHERE
    LAT_N < 137.2345
    
    
# Query the Western Longitude (LONG_W) for the largest Northern 
# Latitude (LAT_N) in STATION that is less than 137.2345. 
# Round your answer to  decimal places.

SELECT
    ROUND(LONG_W, 4)
FROM 
    STATION
WHERE
    LAT_N < 137.2345
ORDER BY
    LAT_N DESC
LIMIT 1


# Query the smallest Northern Latitude (LAT_N) from STATION that
# is greater than 38.7780. Round your answer to 4 decimal places.

SELECT
    ROUND(MIN(LAT_N), 4)
FROM 
    STATION
WHERE
    LAT_N > 38.7780
    
    
# Query the Western Longitude (LONG_W) where the smallest Northern Latitude
# (LAT_N) in STATION is greater than 38.7780. Round your answer 
# to 4 decimal places.

SELECT
    ROUND(LONG_W, 4)
FROM 
    STATION
WHERE
    LAT_N > 38.7780
ORDER BY
    LAT_N
LIMIT 1


# Consider P1(a,b) and P2(c,d) to be two points on a 2D plane.
# - a happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
# - b happens to equal the minimum value in Western Longitude (LONG_W in STATION).
# - c happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
# - d happens to equal the maximum value in Western Longitude (LONG_W in STATION).
#
# Query the Manhattan Distance between points P1 and P2 and 
# round it to a scale of 4 decimal places.

SELECT
    ROUND(ABS(MIN(LAT_N) - MAX(LAT_N)) + ABS(MIN(LONG_W) - MAX(LONG_W)), 4)
FROM
    STATION
    
    
# Consider P1(a,c) and P2(b,d) to be two points on a 2D plane where
# (a,b) are the respective minimum and maximum values of Northern Latitude 
# (LAT_N) and (c,d) are the respective minimum and maximum values 
# of Western Longitude (LONG_W) in STATION.
#
# Query the Euclidean Distance between points P1 and P2 and
@ format your answer to display 4 decimal digits.

SELECT
    ROUND(SQRT(POW(MIN(LAT_N) - MAX(LAT_N), 2) + POW(MIN(LONG_W) - MAX(LONG_W), 2)), 4)
FROM
    STATION
    

# A median is defined as a number separating the higher half of a data set
# from the lower half. Query the median of the Northern Latitudes (LAT_N)
# from STATION and round your answer to 4 decimal places.

SELECT
    ROUND(SUM(LAT_N) / COUNT(*), 4)
FROM
    ( SELECT 
            *, 
            ROW_NUMBER() OVER ( ORDER BY LAT_N ) AS ranker,
            COUNT(*) OVER() as counter
        FROM 
            STATION
    ) AS inner_table
WHERE
    CASE MOD(counter, 2)
        WHEN 0 THEN
            ranker IN (counter/2,counter/2 + 1)
        ELSE
            ranker IN ((counter + 1)/2)
    END;


