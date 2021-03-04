CREATE DATABASE IF NOT EXISTS microservice;
USE microservice;
CREATE TABLE IF NOT EXISTS data (
    rowID int primary key auto_increment,
    avgWordsPerPost varchar(20),
    postWithMostWords varchar(255),
    authorWithMostDeletedPosts varchar(255)
    );
INSERT INTO data VALUES (rowID, "", "", "");