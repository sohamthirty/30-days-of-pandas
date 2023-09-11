# Write your MySQL query statement below
SELECT a.candidate_id
FROM Candidates a
JOIN Rounds b
ON a.interview_id=b.interview_id
WHERE a.years_of_exp>=2
GROUP BY candidate_id 
HAVING SUM(b.score)>15;