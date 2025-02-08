import asyncio
import requests
import xml.etree.ElementTree as ET
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Функция для получения курсов валют
def get_exchange_rates():
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    tree = ET.ElementTree(ET.fromstring(response.content))
    root = tree.getroot()

    rates = {}
    for currency in root.findall('Valute'):
        char_code = currency.find('CharCode').text
        value = currency.find('Value').text.replace(',', '.')
        nominal = currency.find('Nominal').text
        rates[char_code] = float(value) / float(nominal)

    return rates

# Обработчик команды /start
@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Введите количество рублей для конвертации:")

# Обработчик текста
@dp.message(lambda message: message.text.isdigit())
async def convert_currency(message: Message):
    rub_amount = float(message.text)
    rates = get_exchange_rates()

    currencies = {
        'USD': 'доллары',
        'EUR': 'евро',
        'JPY': 'йены',
        'CNY': 'юани',
        'GBP': 'фунты',
        'SEK': 'шведские кроны',
        'UAH': 'гривны'
    }

    results = []
    for code, name in currencies.items():
        if code in rates:
            converted_amount = rub_amount / rates[code]
            results.append(f"{converted_amount:.2f} {name}")

    await message.answer("\n".join(results))

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())