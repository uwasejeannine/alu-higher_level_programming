-- A script that lists all records with a score >= 10 in the table second_table
-- The database name will be passed as an argument of the mysql command
SELECT score, name FROM second_table
ORDER BY score DESC;
