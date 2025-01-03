CREATE TABLE IF NOT EXISTS Departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Financing INTEGER NOT NULL CHECK (Financing > 0),
    Name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Faculties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Dean TEXT NOT NULL,
    Name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL UNIQUE,
    Rating INTEGER NOT NULL CHECK (Rating BETWEEN 0 AND 5),
    Year INTEGER NOT NULL CHECK (Rating BETWEEN 1 AND 5)
);

CREATE TABLE IF NOT EXISTS Teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    EmploymentDate TEXT NOT NULL CHECK (EmploymentDate > '1990-01-01'),
    IsAssistant TEXT NOT NULL,
    IsProfessor TEXT NOT NULL,
    Name TEXT NOT NULL,
    Position TEXT NOT NULL,
    Premium REAL NOT NULL CHECK (Salary > 0),
    Salary REAL NOT NULL CHECK (Salary >= 0),
    Surname TEXT NOT NULL,
    UNIQUE(Name, Surname)
);