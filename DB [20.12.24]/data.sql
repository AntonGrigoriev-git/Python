INSERT OR IGNORE INTO Departments (Financing, Name) VALUES (15000, 'Department of Management');
INSERT OR IGNORE INTO Departments (Financing, Name) VALUES (26000, 'Department of Computer Programming');
INSERT OR IGNORE INTO Departments (Financing, Name) VALUES (10000, 'Department of Economic Theory');
INSERT OR IGNORE INTO Departments (Financing, Name) VALUES (18000, 'Department of Foreign Languages');

INSERT OR IGNORE INTO Faculties (Dean, Name) VALUES ('Smith', 'Management');
INSERT OR IGNORE INTO Faculties (Dean, Name) VALUES ('Taylor', 'Computer Science');
INSERT OR IGNORE INTO Faculties (Dean, Name) VALUES ('Davis', 'Economics');
INSERT OR IGNORE INTO Faculties (Dean, Name) VALUES ('Wilson', 'Foreign Languages');

INSERT OR IGNORE INTO Groups (Name, Rating, Year) VALUES ('Group 301', 4, 3);
INSERT OR IGNORE INTO Groups (Name, Rating, Year) VALUES ('Group 201', 5, 2);
INSERT OR IGNORE INTO Groups (Name, Rating, Year) VALUES ('Group 302', 3, 3);
INSERT OR IGNORE INTO Groups (Name, Rating, Year) VALUES ('Group 401', 4, 4);

INSERT OR IGNORE INTO Teachers (EmploymentDate, IsAssistant, IsProfessor, Name, Position, Premium, Salary, Surname)
VALUES ('2015-09-01', 'No', 'Yes', 'John', 'Professor', 600, 1000, 'Smith');
INSERT OR IGNORE INTO Teachers (EmploymentDate, IsAssistant, IsProfessor, Name, Position, Premium, Salary, Surname)
VALUES ('2018-01-15', 'Yes', 'No', 'Emily', 'Assistant', 200, 900, 'Johnson');
INSERT OR IGNORE INTO Teachers (EmploymentDate, IsAssistant, IsProfessor, Name, Position, Premium, Salary, Surname)
VALUES ('2020-03-10', 'No', 'Yes', 'Michael', 'Associate Professor', 300, 1100, 'Williams');
INSERT OR IGNORE INTO Teachers (EmploymentDate, IsAssistant, IsProfessor, Name, Position, Premium, Salary, Surname)
VALUES ('2012-07-20', 'Yes', 'No', 'Sarah', 'Lecturer', 150, 1200, 'Brown');