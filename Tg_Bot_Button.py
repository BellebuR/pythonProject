from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram import F
from config import TOKEN
import asyncio

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Задание 1: Обработчик команды /start
@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
    ], resize_keyboard=True)
    await message.answer("Выберите опцию:", reply_markup=keyboard)

@dp.message(lambda message: message.text in ["Привет", "Пока"])
async def greet_or_farewell(message: types.Message):
    if message.text == "Привет":
        await message.answer(f"Привет, {message.from_user.first_name}!")
    elif message.text == "Пока":
        await message.answer(f"До свидания, {message.from_user.first_name}!")

# Задание 2: Обработчик команды /links
@dp.message(Command('links'))
async def send_links(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Новости", url='https://news.example.com')],
        [InlineKeyboardButton(text="Музыка", url='https://music.example.com')],
        [InlineKeyboardButton(text="Видео", url='https://video.example.com')]
    ])
    await message.answer("Выберите ссылку:", reply_markup=keyboard)

# Задание 3: Обработчик команды /dynamic
@dp.message(Command('dynamic'))
async def send_dynamic(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data='show_more')]
    ])
    await message.answer("Нажмите кнопку:", reply_markup=keyboard)

@dp.callback_query(F.data == 'show_more')
async def show_more_options(callback_query: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Опция 1", callback_data='option_1')],
        [InlineKeyboardButton(text="Опция 2", callback_data='option_2')]
    ])
    await callback_query.message.edit_text("Выберите опцию:", reply_markup=keyboard)

@dp.callback_query(lambda c: c.data in ['option_1', 'option_2'])
async def option_selected(callback_query: types.CallbackQuery):
    if callback_query.data == 'option_1':
        await callback_query.message.answer("Вы выбрали Опция 1")
    elif callback_query.data == 'option_2':
        await callback_query.message.answer("Вы выбрали Опция 2")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())