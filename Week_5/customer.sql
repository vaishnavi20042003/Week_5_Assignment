CREATE DATABASE Information;
USE Information;

CREATE TABLE People (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    CONSTRAINT chk_gender CHECK (gender IN ('Male', 'Female', 'Other'))
);

INSERT INTO People (name, age, gender) VALUES
('Vaishnavi', 20, 'Female'),
('Ishika', 21, 'Female'),
('Ronak', 20, 'Male'),
('Nandini', 20, 'Female'),
('Akshara', 18, 'Female'),
('Anurag', 19, 'Male'),
('Krishna', 24, 'Male'),
('Sejal', 17, 'Female'),
('Monika', 19, 'Female'),
('Ashish', 17, 'Male'),
('Priyanshi', 20, 'Female'),
('Anjali', 16, 'Female');
SELECT * FROM People;