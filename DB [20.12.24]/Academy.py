import sqlite3

def execute_sql_file(cursor, filename):
    with open(filename, 'r', encoding='utf-8') as file:
        sql_script = file.read()
        cursor.executescript(sql_script)

# Блок для создания таблиц и вставки данных
with sqlite3.connect('Academy.db') as conn:
    cursor = conn.cursor()

    execute_sql_file(cursor, 'tables.sql')
    execute_sql_file(cursor, 'data.sql')

# Блок для проверки данных
with sqlite3.connect('Academy.db') as conn:
    cursor = conn.cursor()

    # 1.
    print('\n1. Таблица кафедр (поля расположены в обратном порядке)')
    cursor.execute('''
        SELECT * FROM Departments
        ORDER BY id DESC;
    ''')

    departments = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    print(f'{column_names[0]:<20} {column_names[1]:<20} {column_names[2]:<20}')

    for row in departments:
        print(f'{row[0]:<20} {row[1]:<20} {row[2]:<20}')

    # 2.
    print('\n2. Названия групп и их рейтинги с уточнением имен полей именем таблицы')
    cursor.execute('''
        SELECT Name AS 'GroupsName', Rating AS 'GroupsRating'
        FROM Groups
    ''')

    groups = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    print(f'{column_names[0]:<20} {column_names[1]:<20}')

    for row in groups:
        print(f'{row[0]:<20} {row[1]:<20}')

    # 3.
    print(
        '\n3. Фамилии преподователей, процент ставки по отношению к надбавке '
        'и процент ставки по отношению к зарплате'
    )
    cursor.execute('''
        SELECT Surname,
        (Premium / Salary) * 100 AS PremiumPercentage, 
        (Salary / (Salary + Premium)) * 100 AS SalaryPercentage
        FROM Teachers
    ''')

    teachers = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    print(f'{column_names[0]:<20} {column_names[1]:<20} {column_names[2]:<20}')

    for row in teachers:
        print(f'{row[0]:<20} {row[1]:<20.2f} {row[2]:<20.2f}')

    # 4.
    print('\n4. Фамилии преподователей, которые являются профессорами и ставка которых превышвет 1050')
    cursor.execute('''
        SELECT Surname, IsProfessor, Salary
        FROM Teachers
        WHERE IsProfessor = 'Yes' AND Salary > 1050
    ''')

    teachers = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    print(f'{column_names[0]:<20} {column_names[1]:<20} {column_names[2]:<20}')

    for row in teachers:
        print(f'{row[0]:<20} {row[1]:<20} {row[2]:<20}')

    # 5.
    print('\n5. Названия кафедр, фонд финансирования которых меньше 11000 или больше 25000')
    cursor.execute('''
        SELECT Name, Financing
        FROM Departments
        WHERE Financing < 11000 OR Financing > 25000
    ''')

    departments = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    print(f'{column_names[0]:<40} {column_names[1]:<20}')

    for row in departments:
        print(f'{row[0]:<40} {row[1]:<20}')

    # 6.
    print('\n6. Названия факультетов кроме "Computer Science"')
    cursor.execute('''
        SELECT Name
        FROM Faculties
        WHERE Name != "Computer Science"
    ''')

    faculties = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    print(f'{column_names[0]:<20}')

    for row in faculties:
        print(f'{row[0]:<20}')

    # 7.
    print('\n7. Фамилии и должности преподавателей, которые не являются профессорами')
    cursor.execute('''
        SELECT Surname, Position
        FROM Teachers
        WHERE IsProfessor = 'No'
    ''')

    teachers = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    print(f'{column_names[0]:<20} {column_names[1]:<20}')

    for row in teachers:
        print(f'{row[0]:<20} {row[1]:<20}')

    # 8.
    print('\n8. Фамилии, должности, ставки и набдавки ассистентов, у которых надбавка в диапазоне от 160 до 550')
    cursor.execute('''
        SELECT Surname, Position, Salary, Premium
        FROM Teachers
        WHERE IsAssistant = 'Yes' AND Premium BETWEEN 160 AND 550
    ''')

    teachers = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    print(f'{column_names[0]:<20} {column_names[1]:<20} {column_names[2]:<20} {column_names[3]:<20}')

    for row in teachers:
        print(f'{row[0]:<20} {row[1]:<20} {row[2]:<20} {row[3]:<20}')

    # 9.
    print('\n9. Фамилии и ставки ассистентов')
    cursor.execute('''
        SELECT Surname, Salary
        FROM Teachers
        WHERE IsAssistant = 'Yes'
    ''')

    teachers = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    print(f'{column_names[0]:<20} {column_names[1]:<20}')

    for row in teachers:
        print(f'{row[0]:<20} {row[1]:<20}')

    # 10.
    print('\n10. Фамилии и должности преподавателей, которые были приняты на работу до 01.01.2020')
    cursor.execute('''
        SELECT Surname, Position
        FROM Teachers
        WHERE EmploymentDate < '2020-01-01'
    ''')

    teachers = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    print(f'{column_names[0]:<20} {column_names[1]:<20}')

    for row in teachers:
        print(f'{row[0]:<20} {row[1]:<20}')

    # 11.
    print('\n11. Фамилии ассистентов, имеющие зарплату (сумма ставки и надбавки) не более 1200')
    cursor.execute('''
        SELECT Surname, (Salary + Premium) AS TotalSalary
        FROM Teachers
        WHERE IsAssistant = 'Yes' AND (Salary + Premium) <= 1200
    ''')

    teachers = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    print(f'{column_names[0]:<20} {column_names[1]:<20}')

    for row in teachers:
        print(f'{row[0]:<20} {row[1]:<20}')