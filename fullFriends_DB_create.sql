CREATE DATABASE IF NOT EXISTS fullFriends;

USE fullFriends;

CREATE TABLE users(
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(55) NOT NULL,
    last_name VARCHAR(55) NOT NULL,
    created_at DATETIME,
    last_update DATETIME
);

INSERT INTO users(first_name, last_name, created_at) VALUES
	('Austin', 'Danger', NOW()),
    ('Danger', 'Powers', NOW());