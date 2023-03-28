-- A script that creates a table second_table in the database
-- Add multiples rows.
CREATE TABLE IF NOT EXISTS second_table(
	id INT,
	name VARCHAR(256),
	score INT);
INSERT INTO second_table(id,name,score)VALUES(1,"Jeannine", 99);
INSERT INTO second_table(id,name,score)VALUES(2,"Challes", 90);
INSERT INTO second_table(id,name,score)VALUES(3,"Fille", 79);
INSERT INTO second_table(id,name,score)VALUES(4,"Uwase", 77);
INSERT INTO second_table(id,name,score)VALUES(5,"Gentille", 75);
INSERT INTO second_table(id,name,score)VALUES(6,"Uwimbazi", 69);
