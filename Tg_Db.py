import sqlite3

def create_database():
    # Подключение к базе данных (если файла базы данных не существует, он будет создан)
    conn = sqlite3.connect('school_data.db')
    cursor = conn.cursor()

    # Создание таблицы students
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL
        )
    ''')

    # Закрытие соединения с базой данных
    conn.commit()
    conn.close()

# Вызов функции для создания базы данных и таблицы
if __name__ == '__main__':
    create_database()