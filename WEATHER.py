from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
import requests
from config import TOKEN, WEATHER_API_KEY
import logging

logging.basicConfig(level=logging.INFO)

# Создание объекта бота
bot = Bot(token=TOKEN)

# Создание диспетчера
dp = Dispatcher()


def get_weather(city: str) -> str:
    url = f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&lang=ru'
    response = requests.get(url)
    logging.info(f'Response from weather API: {response.status_code}, {response.text}')
    if response.status_code == 200:
        data = response.json()
        weather_desc = data['current']['condition']['text']
        temp = data['current']['temp_c']
        return f'Сейчас в городе {city} {weather_desc}, температура {temp}°C.'
    else:
        return 'Не удалось получить данные о погоде. Проверьте название города.'

@dp.message(Command('start'))
async def send_welcome(message: Message):
    await message.answer('Привет! Я погодный бот. Используйте /weather <город>, чтобы узнать погоду.')

@dp.message(Command('help'))
async def send_help(message: Message):
    await message.answer('Введите /weather <город>, чтобы получить информацию о погоде в указанном городе.')

@dp.message(Command('weather'))
async def send_weather(message: Message):
    try:
        city = message.text.split(' ', 1)[1]
        weather_info = get_weather(city)
        await message.answer(weather_info)
    except IndexError:
        await message.answer('Пожалуйста, введите название города после команды /weather.')

async def main():
    # Регистрация хэндлеров
    dp.message.register(send_welcome, Command('start'))
    dp.message.register(send_help, Command('help'))
    dp.message.register(send_weather, Command('weather'))

    # Запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())