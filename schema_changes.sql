-- PROG8850 Assignment 2 - Question 1: Database Schema Changes

-- creating db named companydb
CREATE DATABASE IF NOT EXISTS companydb;
USE companydb;

-- First, creating table named projects
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE
);

-- Safe check before adding 'budget' column
SET @budget_exists := (
  SELECT COUNT(*) 
  FROM INFORMATION_SCHEMA.COLUMNS 
  WHERE TABLE_SCHEMA = 'companydb' AND TABLE_NAME = 'projects' AND COLUMN_NAME = 'budget'
);
SET @sql := IF(@budget_exists = 0, 'ALTER TABLE projects ADD COLUMN budget DECIMAL(10,2)', 
'SELECT "Column already exists"');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- inserting data in projects table
INSERT INTO projects (project_name, start_date, end_date, budget) VALUES
('Website Redesign', '2025-01-15', '2025-03-15', 15000.00),
('Mobile App Development', '2025-02-01', '2025-06-30', 45000.00),
('Database Migration', '2025-03-01', '2025-04-15', 8500.00);
