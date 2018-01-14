-- Initial setup of a database

CREATE TABLE users (
	user_name TEXT,
	time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	id SERIAL 
);

CREATE INDEX ON users ((lower(user_name)));