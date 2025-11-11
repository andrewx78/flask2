PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
INSERT INTO alembic_version VALUES('0ddc960cfaf1');
CREATE TABLE authors (
	id INTEGER NOT NULL, 
	name VARCHAR(32) NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO authors VALUES(1,'Mark Twen');
INSERT INTO authors VALUES(2,'Lev Tolstoy');
INSERT INTO authors VALUES(3,'Nikolay Nosov');
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
CREATE UNIQUE INDEX ix_authors_name ON authors (name);
COMMIT;
