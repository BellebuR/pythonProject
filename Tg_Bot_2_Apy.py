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

# Функция для получения информации о стране
def get_country_info(code):
    url = "https://countries.trevorblades.com"
    json = {'query': f'''
    {{
      country(code: "{code.upper()}") {{
        name
        native
        emoji
        currency
        languages {{
          code
          name
        }}
      }}
    }}
    '''}

    response = requests.post(url, json=json)
    data = response.json()

    if 'errors' in data:
        return "Информация о стране не найдена. Проверьте код страны."

    country = data['data']['country']
    languages = ", ".join(lang['name'] for lang in country['languages'])
    info = (f"Название: {country['name']}\n"
            f"Национальное название: {country['native']}\n"
            f"Флаг: {country['emoji']}\n"
            f"Валюта: {country['currency']}\n"
            f"Языки: {languages}")

    return info

# Обработчик команды /start
@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Введите количество рублей для конвертации или код страны для информации:")

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

# Обработчик для получения информации о стране
@dp.message(lambda message: len(message.text) == 2)  # Предполагаем, что код страны состоит из 2 символов
async def country_info(message: Message):
    country_code = message.text.strip()
    info = get_country_info(country_code)
    await message.answer(info)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())