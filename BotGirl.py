import telebot
import requests

# Вставьте сюда ваш токен Telegram API
TELEGRAM_API_TOKEN = '7190369938:AAHs0ERVZHJiGvgdeUskeFpf0BPOh-7uIEo'

# Вставьте сюда ваш API ключ OpenWeatherMap
WEATHER_API_KEY = 'df0b136ec46d4a5236b1b6ebf06df445'

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

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

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я погодный бот. Введите /weather <город>, чтобы узнать погоду.')

@bot.message_handler(commands=['weather'])
def send_weather(message):
    try:
        city = message.text.split(' ', 1)[1]
        weather_info = get_weather(city)
        bot.reply_to(message, weather_info)
    except IndexError:
        bot.reply_to(message, 'Пожалуйста, введите название города после команды /weather.')

def main():
    bot.polling()

if __name__ == '__main__':
    main()