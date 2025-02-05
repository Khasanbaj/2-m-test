import sqlite3
from datetime import datetime, timedelta

connect = sqlite3.connect("library.db")
cursor = connect.cursor()

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER,
        available BOOLEAN DEFAULT 1
    ) 
""")

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS readers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        book_id INTEGER,
        due_date DATE, 
        FOREIGN KEY (book_id) REFERENCES books(id)
    )    
""")

books = [
    ('Спрут', 'Фрэнк Норрис', 1901),
    ('Послы', 'Генри Джеймс', 1903),
    ('Короли и капуста', 'О. Генри', 1904),
    ('Мартин Иден', 'Джек Лондон', 1909),
    ('В ногу!', 'Шервуд Андерсон', 1917),
    ('Моя Антония', 'Уилла Кэсер', 1918)
]

for book in books:
    cursor.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', book)

readers = [
    ('Jordan', 42),
    ('Khabib', 37),
    ('Ronaldo', 40)
]
for reader in readers:
    cursor.execute('INSERT INTO readers (name, age) VALUES (?, ?)', reader)

cursor.execute('UPDATE readers SET book_id = 1 WHERE id = 1')
cursor.execute('UPDATE books SET available = 0 WHERE id = 1')

cursor.execute('SELECT * FROM books WHERE available = 1')
available_books = cursor.fetchall()

print("Доступные книги:")
for book in available_books:
    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")

cursor.execute('DELETE FROM books WHERE id = 2')

cursor.execute('SELECT * FROM readers WHERE book_id IS NOT NULL')
readers_with_books = cursor.fetchall()

print("Читатели с книгами:")
for reader in readers_with_books:
    print(f"ID: {reader[0]}, Name: {reader[1]}, Age: {reader[2]}, Book ID: {reader[3]}")

cursor.execute('UPDATE readers SET due_date = ? WHERE id = 1', ((datetime.now() - timedelta(days=1)).date(),))

cursor.execute('SELECT * FROM readers WHERE due_date < ?', (datetime.now().date(),))
overdue_readers = cursor.fetchall()

print("Читатели с просроченными книгами:")
for reader in overdue_readers:
    print(f"ID: {reader[0]}, Name: {reader[1]}, Age: {reader[2]}, Book ID: {reader[3]}, Due Date: {reader[4]}")

connect.commit()
connect.close()