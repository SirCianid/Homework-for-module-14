import sqlite3

# Подключаемся к базе данных
connect = sqlite3.connect("not_telegram.db")
cursor = connect.cursor()

# Создаем таблицу Users, если она еще не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User {i}", f"example{i}@gmail.com", 10 * i, 1000))

cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")

cursor.execute("DELETE FROM Users WHERE id IN (SELECT id FROM Users WHERE (ROWID - 1) % 3 = 0)")

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")

results = cursor.fetchall()

for result in results:
    print(f"Имя: {result[0]} | Почта: {result[1]} | Возраст: {result[2]} | Баланс: {result[3]}")

connect.commit()
connect.close()
