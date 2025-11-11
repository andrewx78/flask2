PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE quotes (
	id INTEGER NOT NULL, 
	author_id INTEGER NOT NULL, 
	text VARCHAR(255) NOT NULL, rating INTEGER DEFAULT '1' NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(author_id) REFERENCES authors (id)
);
INSERT INTO quotes VALUES(1,1,'Mark''s quote',1);
INSERT INTO quotes VALUES(2,1,'srveretbgrt',2);
INSERT INTO quotes VALUES(3,2,'quote3',3);
INSERT INTO quotes VALUES(4,3,'Nikolay''s 1-st quote',1);
COMMIT;
