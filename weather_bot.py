import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests
import os
from config import TOKEN
from config import WEATHER_API_KEY

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'WEATHER_API_KEY')

async def main():
    await dp.start_polling(bot)

@dp.message_handler(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\\n/start\\n/help")

@dp.message(F.text == "что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')

def get_weather(city: str) -> str:
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        return f'Сейчас в городе {city} {weather_desc}, температура {temp}°C.'
    else:
        return 'Не удалось получить данные о погоде. Проверьте название города.'

@dp.message_handler(CommandStart)
async def send_welcome(message: Message):
    await message.reply('Привет! Я погодный бот. Введите /weather <город>, чтобы узнать погоду.')

@dp.message_handler(Command('weather'))
async def send_weather(message: Message):
    try:
        city = message.text.split(' ', 1)[1]
        weather_info = get_weather(city)
        await message.reply(weather_info)
    except IndexError:
        await message.reply('Пожалуйста, введите название города после команды /weather.')

if __name__ == "__main__":
    asyncio.run(main())