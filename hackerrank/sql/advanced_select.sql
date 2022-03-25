# Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. 
# Output one of the following statements for each record in the table:
#
# Equilateral: It's a triangle with  sides of equal length.
# Isosceles: It's a triangle with  sides of equal length.
# Scalene: It's a triangle with  sides of differing lengths.
# Not A Triangle: The given values of A, B, and C don't form a triangle.

SELECT
    CASE
        WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
        WHEN A = B AND B = C THEN 'Equilateral'
        WHEN A = B OR A = C OR B = C THEN 'Isosceles'
        ELSE 'Scalene'
    END
FROM TRIANGLES;


# Generate the following two result sets:
#
# 1. Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first 
# letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: 
# AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
#
# 2. Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending
# order, and output them in the following format: "There are a total of [occupation_count] [occupation]s.",
# where [occupation_count] is the number of occurrences of an occupation in OCCUPATIONS 
# and [occupation] is the lowercase occupation name. If more than one Occupation has the same [occupation_count], 
# they should be ordered alphabetically.

SELECT 
    CONCAT(Name, '(', LEFT(Occupation, 1), ')')
FROM OCCUPATIONS
ORDER BY Name;

SELECT
    CONCAT('There are a total of ', COUNT(*), ' ', LOWER(Occupation), 's.')
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(*), Occupation;


# Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed
# underneath its corresponding Occupation. The output column headers should be 
# Doctor, Professor, Singer, and Actor, respectively.
#
#Note: Print NULL when there are no more names corresponding to an occupation.
#
# Occupation will only contain one of the following values: 
# Doctor, Professor, Singer or Actor.

SET @r1 = 0, @r2 = 0, @r3 = 0, @r4 = 0;

SELECT
    MIN( ranked_occupation.Doctor ),
    MIN( ranked_occupation.Professor ),
    MIN( ranked_occupation.Singer ),
    MIN( ranked_occupation.Actor ) 
FROM
    (
    SELECT
        CASE Occupation WHEN 'Doctor' THEN NAME END AS Doctor,
        CASE Occupation WHEN 'Professor' THEN NAME END AS Professor,
        CASE Occupation WHEN 'Singer' THEN NAME END AS Singer,
        CASE Occupation WHEN 'Actor' THEN NAME END AS Actor,
        CASE Occupation 
            WHEN 'Doctor' THEN        @r1 := @r1 + 1 
            WHEN 'Professor' THEN @r2 := @r2 + 1 
            WHEN 'Singer' THEN        @r3 := @r3 + 1 
            WHEN 'Actor' THEN            @r4 := @r4 + 1 
        END AS ranker
    FROM
        OCCUPATIONS 
    ORDER BY Name 
    ) AS ranked_occupation
GROUP BY
    ranked_occupation.ranker;
    

# You are given a table, BST, containing two columns: N and P, where N represents
# the value of a node in Binary Tree, and P is the parent of N.
#
# Write a query to find the node type of Binary Tree ordered by the value of the node.
#
# Output one of the following for each node:
# - Root: If node is root node.
# - Leaf: If node is leaf node.
# - Inner: If node is neither root nor leaf node.

SELECT
	BST.N,
	ANY_VALUE ( 
		CASE 
			WHEN BST.P IS NULL THEN 'Root' 
			WHEN COUNT( BST_CHILDS.N ) = 0 THEN 'Leaf' 
			ELSE 'Inner' 
		END 
	) as Type 
FROM
	BST
	LEFT JOIN BST AS BST_CHILDS ON BST.N = BST_CHILDS.P 
GROUP BY
	BST.N 
ORDER BY
	N;
    

# Amber's conglomerate corporation just acquired some new companies. 
# Each of the companies follows this hierarchy:
# Founder -> Lead manager -> Senior manager -> Manager -> Employee
#
# Given the table schemas below, write a query to print the company_code, 
# founder name, total number of lead managers, total number of senior managers, 
# total number of managers, and total number of employees. 
# Order your output by ascending company_code.
#
# Note:
# 1. The tables may contain duplicate records.
# 2. The company_code is string, so the sorting should not be numeric. 
# For example, if the company_codes are C_1, C_2, and C_10, 
# then the ascending company_codes will be C_1, C_10, and C_2.

SELECT
    c.company_code, 
    ANY_VALUE(c.founder),
    COUNT(DISTINCT l_m.lead_manager_code),
    COUNT(DISTINCT s_m.senior_manager_code),
    COUNT(DISTINCT m.manager_code),
    COUNT(DISTINCT e.employee_code)
FROM 
    Company as c
    LEFT JOIN Lead_Manager as l_m ON l_m.company_code = c.company_code
    LEFT JOIN Senior_Manager as s_m ON s_m.lead_manager_code = l_m.lead_manager_code
    LEFT JOIN Manager as m ON m.senior_manager_code = s_m.senior_manager_code
    LEFT JOIN Employee as e ON e.manager_code = m.manager_code
GROUP BY c.company_code
ORDER BY c.company_code;

