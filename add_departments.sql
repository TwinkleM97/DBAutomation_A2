
-- PROG8850 Assignment 2 - Q2: Departments Table Creation
-- This script creates the departments table as specified in Q2

-- Q2: Creating departments table
USE companydb;

CREATE TABLE IF NOT EXISTS departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    UNIQUE KEY uniq_department (department_name, location) 
);

-- Inserting data for testing (avoiding duplicates on re-runs)
INSERT IGNORE INTO departments (department_name, location) VALUES
('Consulting', 'Toronto, ON'),
('Human Resources', 'Kitchener, ON'),
('Finance', 'Waterloo, ON'),
('Marketing', 'Guelph, ON'),
('Operations', 'Cambridge, ON');

