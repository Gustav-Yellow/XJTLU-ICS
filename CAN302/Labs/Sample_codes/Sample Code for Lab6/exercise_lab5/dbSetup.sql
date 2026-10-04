-- Create the database
CREATE DATABASE library;

-- Use the database
USE library;

-- Create the books table
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL
);