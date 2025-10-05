CREATE DATABASE voting_db;
USE voting_db;

CREATE TABLE IF NOT EXISTS Admin (
    admin_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Voter (
    voter_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50),
    has_voted BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS Candidate (
    candidate_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    party VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Vote (
    vote_id INT PRIMARY KEY AUTO_INCREMENT,
    voter_id INT,
    candidate_id INT,
    FOREIGN KEY (voter_id) REFERENCES Voter(voter_id),
    FOREIGN KEY (candidate_id) REFERENCES Candidate(candidate_id)
);

INSERT INTO Admin (username, password)
SELECT 'admin', 'admin123'
WHERE NOT EXISTS (SELECT * FROM Admin WHERE username='admin');
