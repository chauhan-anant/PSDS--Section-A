-- Create database
CREATE DATABASE IF NOT EXISTS college_db;
USE college_db;
CREATE TABLE Department (
    dept_id     INT          PRIMARY KEY,
    dept_name   VARCHAR(100) NOT NULL,
    hod         VARCHAR(100)
);

CREATE TABLE Student (
    student_id  INT          PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(100) UNIQUE,
    dept_id     INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

CREATE TABLE Course (
    course_id   INT          PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits     INT          CHECK (credits > 0),
    dept_id     INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

CREATE TABLE Enrollment (
    enroll_id   INT PRIMARY KEY,
    student_id  INT NOT NULL,
    course_id   INT NOT NULL,
    grade       CHAR(2),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id)  REFERENCES Course(course_id)
);
-- Insert into Department
INSERT INTO Department VALUES (1, 'Data Structure', 'Dr. Smith');
INSERT INTO Department VALUES (2, 'Mathematics', 'Dr. Verma');

-- Insert into Student
INSERT INTO Student VALUES (1, 'Anant Chauhan', 'CU25250060@gmail.com', 1);
INSERT INTO Student VALUES (2, 'Rahul Sharma', 'rahul@gmail.com', 2);

-- Insert into Course
INSERT INTO Course VALUES (101, 'Data Structures', 3, 1);
INSERT INTO Course VALUES (102, 'Calculus', 4, 2);

-- Insert into Enrollment
INSERT INTO Enrollment VALUES (1001, 1, 101, 'A');
INSERT INTO Enrollment VALUES (1002, 2, 102, 'B');

-- Display all tables
SELECT * FROM Department;
SELECT * FROM Student;
SELECT * FROM Course;
SELECT * FROM Enrollment;


