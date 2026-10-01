# Write your MySQL query statement below
SELECT R.contest_id, ROUND(COUNT(DISTINCT U.user_id)*100/(SELECT COUNT(*) FROM users),2)
AS percentage
FROM Users U RIGHT JOIN Register R
ON U.user_id = R.user_id
GROUP BY R.contest_id
ORDER BY percentage DESC, R.contest_id 