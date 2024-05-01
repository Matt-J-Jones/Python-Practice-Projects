-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS pokemon;
DROP SEQUENCE IF EXISTS pokemon_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS pokemon_id_seq;
CREATE TABLE pokemon (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    height VARCHAR(255),
    weight VARCHAR(255),
    type VARCHAR(255),
    pic VARCHAR(255)
);