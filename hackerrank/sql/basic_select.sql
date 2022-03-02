# Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.

SELECT 
  * 
FROM CITY 
WHERE 
  CountryCode = 'USA' 
  AND POPULATION > 100000;


# Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.

SELECT 
    NAME 
FROM CITY 
WHERE 
  CountryCode = 'USA' 
  AND POPULATION > 120000;


# Query all columns (attributes) for every row in the CITY table.

SELECT 
    * 
FROM CITY 
