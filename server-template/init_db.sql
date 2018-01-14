-- Initial setup of a database

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

CREATE TABLE users (
	user_name TEXT NOT NULL,
	age integer NOT NULL,
	time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	id SERIAL 
);

CREATE INDEX ON users ((lower(user_name)));

ALTER TABLE users OWNER TO vagrant;

INSERT INTO users VALUES ('Tom Cat', 33), ('Bead Eat', 44);