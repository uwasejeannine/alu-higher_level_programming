-- A script that creates a table second_table in the database
-- Add multiples rows.
CREATE TABLE IF NOT EXISTS second_table(
	id INT,
	name VARCHAR(256),
	score INT);
INSERT INTO second_table (id, name, score) VALUES (1, 'Jeannine', 78);
INSERT INTO second_table (id, name, score) VALUES (2, 'Gentille', 67);
INSERT INTO second_table (id, name, score) VALUES (3, 'Germen', 62);
