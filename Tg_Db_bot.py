import asyncio
import json
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
import sqlite3
import os

# Инициализация бота и диспетчера с использованием MemoryStorage
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Путь к базе данных
DB_PATH = 'school_data.db'
JSON_PATH = 'students_data.json'

# Функция для создания таблицы, если она не существует
def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Класс состояний
class Form(StatesGroup):
    name = State()
    age = State()
    grade = State()

# Функция для записи данных в базу данных
def insert_student(name, age, grade):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    conn.close()
    export_to_json()  # Экспорт данных в JSON после вставки

# Функция для экспорта данных в JSON
def export_to_json():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name, age, grade FROM students")
    rows = cursor.fetchall()
    conn.close()

    # Преобразование данных в список словарей
    students = [{'name': row[0], 'age': row[1], 'grade': row[2]} for row in rows]

    # Сохранение данных в JSON файл
    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

# Обработчик команды /start
@dp.message(CommandStart())
async def send_welcome(message: Message, state: FSMContext):
    await message.answer("Привет! Введите ваше имя:")
    await state.set_state(Form.name)

# Обработчик для получения имени
@dp.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите ваш возраст:")
    await state.set_state(Form.age)

# Обработчик для получения возраста
@dp.message(Form.age)
async def process_age(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=int(message.text))
        await message.answer("Введите ваш класс:")
        await state.set_state(Form.grade)
    else:
        await message.answer("Пожалуйста, введите корректный возраст.")

# Обработчик для получения класса
@dp.message(Form.grade)
async def process_grade(message: Message, state: FSMContext):
    await state.update_data(grade=message.text)
    data = await state.get_data()
    insert_student(data['name'], data['age'], data['grade'])
    await message.answer("Ваши данные сохранены!")

# Главная функция для запуска бота
async def main():
    create_table()  # Создание таблицы, если она не существует
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())