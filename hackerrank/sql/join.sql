# Given the CITY and COUNTRY tables, query the sum
# of the populations of all cities where the CONTINENT is 'Asia'.
#
# Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

SELECT
    SUM(CITY.POPULATION)
FROM
    COUNTRY
    JOIN CITY ON COUNTRY.CODE = CITY.COUNTRYCODE
WHERE
    COUNTRY.CONTINENT = 'Asia'
    
    
# Given the CITY and COUNTRY tables, query the names of all 
# cities where the CONTINENT is 'Africa'.
#
# Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

SELECT
    CITY.NAME
FROM CITY
    JOIN COUNTRY ON COUNTRY.CODE = CITY.COUNTRYCODE
WHERE
    COUNTRY.CONTINENT = 'Africa'
    
    
# Given the CITY and COUNTRY tables, query the names of all the continents
# (COUNTRY.Continent) and their respective average city populations
# (CITY.Population) rounded down to the nearest integer.
#
# Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

SELECT
    COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION))
FROM
    COUNTRY
    JOIN CITY ON COUNTRY.CODE = CITY.COUNTRYCODE
GROUP BY
    COUNTRY.CONTINENT
    
    
# You are given two tables: Students and Grades. Students contains
# three columns ID, Name and Marks. Grades contains the following data:
# Grade, Min_Mark, Max_Mark.
#
# Ketty gives Eve a task to generate a report containing three columns: 
# Name, Grade and Mark. Ketty doesn't want the NAMES of those students who 
# received a grade lower than 8. The report must be in descending 
$ order by grade -- i.e. higher grades are entered first. If there is more than
# one student with the same grade (8-10) assigned to them, order those 
# particular students by their name alphabetically. Finally, if the grade 
# is lower than 8, use "NULL" as their name and list them by their grades
# in descending order. If there is more than one student with the same grade 
# (1-7) assigned to them, order those particular students by their marks in ascending order.

SELECT
    IF (g.Grade <= 7, NULL, s.`Name`),
    g.Grade,
    s.Marks
FROM
    Students as s
    INNER JOIN Grades as g ON s.Marks >= g.Min_Mark 
    AND s.Marks <= g.Max_Mark
ORDER BY g.Grade desc, s.Name, s.Marks


# Julia just finished conducting a coding contest, and she needs your help
# assembling the leaderboard! Write a query to print the respective hacker_id
# and name of hackers who achieved full scores for more than one challenge. 
# Order your output in descending order by the total number of challenges in 
# which the hacker earned a full score. If more than one hacker received full 
# scores in same number of challenges, then sort them by ascending hacker_id.
#
# The following tables contain contest data:
# - Hackers: The hacker_id is the id of the hacker, and name is the name of the hacker.
# - Difficulty: The difficult_level is the level of difficulty of the challenge, 
# and score is the score of the challenge for the difficulty level.
# - Challenges: The challenge_id is the id of the challenge, the hacker_id is the 
# id of the hacker who created the challenge, and difficulty_level is the level 
# of difficulty of the challenge.
# - Submissions: The submission_id is the id of the submission, hacker_id is 
# the id of the hacker who made the submission, challenge_id is the id of the challenge
# that the submission belongs to, and score is the score of the submission.

SELECT
    CONCAT(wide_info.hacker_id, ' ', wide_info.hacker_name)
FROM (
    SELECT
        submissions.hacker_id as hacker_id, ANY_VALUE(hackers.name) as hacker_name, COUNT(*) as counter
    FROM 
        Submissions as submissions
        INNER JOIN Challenges as challenges ON challenges.challenge_id = submissions.challenge_id
        INNER JOIN Difficulty as difficulty ON difficulty.difficulty_level = challenges.difficulty_level
        INNER JOIN Hackers as hackers ON hackers.hacker_id = submissions.hacker_id
    WHERE 
        submissions.score = difficulty.score
    GROUP BY 
        submissions.hacker_id
    HAVING 
        counter > 1
    ORDER BY
        counter desc, submissions.hacker_id
) as wide_info


# Harry Potter and his friends are at Ollivander's with Ron, finally 
# replacing Charlie's old broken wand.
#
# Hermione decides the best way to choose is by determining the minimum 
# number of gold galleons needed to buy each non-evil wand of high power and age.
# Write a query to print the id, age, coins_needed, and power of the wands 
# that Ron's interested in, sorted in order of descending power. 
# If more than one wand has same power, sort the result in order of descending age.
#
# Input Format
# 
# - Wands: The id is the id of the wand, code is the code of the wand, 
# coins_needed is the total number of gold galleons needed to buy the wand,
# and power denotes the quality of the wand (the higher the power, 
# the better the wand is). 
# - Wands_Property: The code is the code of the wand, age is the age of the wand,
# and is_evil denotes whether the wand is good for the dark arts. If the value
# of is_evil is 0, it means that the wand is not evil. The mapping between code
# and age is one-one, meaning that if there are two pairs, (code1, age1) and (code2, age2),
# then code1 <> code2 and age1 <> age2.

SELECT
    w.id, w_p.age, w.coins_needed, w.power 
FROM
    Wands AS w
    INNER JOIN ( 
        SELECT 
            ANY_VALUE ( code ) AS code, MIN( coins_needed ) AS coins_needed 
        FROM 
            Wands
        GROUP BY 
            code, power 
        ) AS w2 ON w2.CODE = w.CODE AND w2.coins_needed = w.coins_needed
    INNER JOIN Wands_Property as w_p ON w_p.code = w.code AND w_p.is_evil = 0
ORDER BY
    w.power DESC, w_p.age DESC


# Julia asked her students to create some coding challenges. Write a query 
# to print the hacker_id, name, and the total number of challenges created 
# by each student. Sort your results by the total number of challenges in 
# descending order. If more than one student created the same number of 
# challenges, then sort the result by hacker_id. If more than one student
# created the same number of challenges and the count is less than the 
# maximum number of challenges created, then exclude those students from the result.
# 
# - Hackers: The hacker_id is the id of the hacker, and name is the name 
# of the hacker.
# - Challenges: The challenge_id is the id of the challenge, and 
# hacker_id is the id of the student who created the challenge.

SELECT
	ANY_VALUE(h.hacker_id), ANY_VALUE(h.name), COUNT(c.challenge_id) as challenge_count
FROM Hackers as h
	INNER JOIN Challenges as c on c.hacker_id = h.hacker_id
GROUP BY
	h.hacker_id
HAVING 
	challenge_count = (SELECT COUNT(challenge_id) as ch_count FROM Challenges GROUP BY hacker_id ORDER BY ch_count DESC LIMIT 1 )
	OR
	challenge_count IN (
		SELECT 
			ch_total.ch_count 
		FROM 
			( SELECT COUNT( challenge_id ) AS ch_count FROM Challenges GROUP BY hacker_id ) AS ch_total 
		GROUP BY ch_total.ch_count 
		HAVING
			COUNT( ch_total.ch_count ) = 1
		)
ORDER BY
	challenge_count DESC, h.hacker_id


# You did such a great job helping Julia with her last coding contest 
# challenge that she wants you to work on this one, too!
#
# The total score of a hacker is the sum of their maximum scores for all 
# of the challenges. Write a query to print the hacker_id, name, and 
# total score of the hackers ordered by the descending score. If more 
# than one hacker achieved the same total score, then sort the result 
# by ascending hacker_id. Exclude all hackers with a total score of  
# from your result.
#
# - Hackers: The hacker_id is the id of the hacker, and name is the 
# name of the hacker.
# - Submissions: The submission_id is the id of the submission, hacker_id
# is the id of the hacker who made the submission, challenge_id is the id 
# of the challenge for which the submission belongs to, and score is 
# the score of the submission.

SELECT 
    h.hacker_id, h.name, hacker_total_scores.total_score
FROM
    Hackers as h
    INNER JOIN (
        SELECT
            hacker_scores.hacker_id, SUM(hacker_scores.score) as total_score
        FROM (
            SELECT
                hacker_id, MAX(score) as score
            FROM
                Submissions as s
            GROUP BY hacker_id, challenge_id    
        ) as hacker_scores
        GROUP BY
            hacker_scores.hacker_id
    ) as hacker_total_scores ON hacker_total_scores.hacker_id = h.hacker_id
WHERE 
    hacker_total_scores.total_score > 0
ORDER BY
    hacker_total_scores.total_score DESC, h.hacker_id

