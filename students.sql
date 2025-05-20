CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT,
    age INTEGER,
    phone_number TEXT,
    admission_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    gender TEXT
);
