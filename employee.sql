DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone_number TEXT,
    gender TEXT,
    position TEXT,
);

INSERT INTO employees (
    first_name,
    last_name,
    email,
    phone_number,
    gender,
    position,
    department,
    salary
) VALUES 
('Alice', 'Mwangi', 'alice.mwangi@company.com', '+254712345678', 'Female', 'Software Engineer', 'IT', 120000.00),
('David', 'Kamau', 'david.kamau@company.com', '+254798112233', 'Male', 'Product Manager', 'Product', 150000.00),
('Sarah', 'Mutheu', 'sarah.mutheu@company.com', '+254701234567', 'Female', 'Data Analyst', 'Analytics', 110000.00),
('John', 'Otieno', 'john.otieno@company.com', '+254729876543', 'Male', 'System Administrator', 'IT', 100000.00);
