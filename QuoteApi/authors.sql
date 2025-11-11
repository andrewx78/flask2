PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
-- CREATE TABLE authors (
-- 	id INTEGER NOT NULL, 
-- 	name VARCHAR(32) NOT NULL, surname VARCHAR(32) DEFAULT 'Ivanov' NOT NULL, 
-- 	PRIMARY KEY (id)
-- );
INSERT INTO authors VALUES(1,'Mark Twen','Ivanov');
INSERT INTO authors VALUES(2,'Lev Tolstoy','Ivanov');
INSERT INTO authors VALUES(3,'Nikolay Nosov','Ivanov');
INSERT INTO authors VALUES(4,'Nikolay Tolstoy','Ivanov');
COMMIT;
PRAGMA foreign_keys=OFF;
       
