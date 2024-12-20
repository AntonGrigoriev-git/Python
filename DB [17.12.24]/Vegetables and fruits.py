import sqlite3

conn = sqlite3.connect('produce.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS vegetables_and_fruits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    color TEXT NOT NULL,
    calorie INTEGER NOT NULL,
    description TEXT
)
''')

cursor.execute('''
INSERT INTO vegetables_and_fruits (name, type, color, calorie, description) VALUES (?, ?, ?, ?, ?)
''', ('Tomato', 'Vegetable', 'Red', 18, 'A red vegetable often used in salads.'))

cursor.execute('''
INSERT INTO vegetables_and_fruits (name, type, color, calorie, description) VALUES (?, ?, ?, ?, ?)
''', ('Apple', 'Fruit', 'Green', 52, 'A green fruit that is sweet and crunchy.'))

cursor.execute('''
INSERT INTO vegetables_and_fruits (name, type, color, calorie) VALUES (?, ?, ?, ?)
''', ('Cucumber', 'Vegetable', 'Green', 16))

cursor.execute('''
INSERT INTO vegetables_and_fruits (name, type, color, calorie) VALUES (?, ?, ?, ?)
''', ('Carrot', 'Vegetable', 'Orange', 41))

cursor.execute('''
INSERT INTO vegetables_and_fruits (name, type, color, calorie, description) VALUES (?, ?, ?, ?, ?)
''', ('Orange', 'Fruit', 'Orange', 47, 'A sweet and juicy citrus fruit.'))

conn.commit()

cursor.execute('SELECT * FROM vegetables_and_fruits')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()