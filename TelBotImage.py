import telebot

# Ваш API токен, который вы получили у BotFather
API_TOKEN = '7190369938:AAHs0ERVZHJiGvgdeUskeFpf0BPOh-7uIEo'

bot = telebot.TeleBot(API_TOKEN)

# Хранилище для сообщений, разделённое по пользователям
user_messages = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я буду запоминать всё, что ты мне напишешь.")

@bot.message_handler(commands=['list'])
def list_messages(message):
    user_id = message.chat.id
    if user_id in user_messages and user_messages[user_id]:
        response = "Вот твои сохранённые сообщения:\n"
        for i, msg in enumerate(user_messages[user_id]):
            response += f"{i + 1}. {msg}\n"
    else:
        response = "У тебя пока нет сохранённых сообщений."
    bot.send_message(user_id, response)

@bot.message_handler(func=lambda message: message.text.startswith('del '))
def delete_message(message):
    user_id = message.chat.id
    try:
        index = int(message.text.split()[1]) - 1
        if user_id in user_messages and 0 <= index < len(user_messages[user_id]):
            deleted_msg = user_messages[user_id].pop(index)
            bot.reply_to(message, f"Сообщение '{deleted_msg}' удалено.")
        else:
            bot.reply_to(message, "Некорректный номер сообщения.")
    except (ValueError, IndexError):
        bot.reply_to(message, "Пожалуйста, укажите корректный номер сообщения после команды 'del'.")

@bot.message_handler(func=lambda message: True)
def save_message(message):
    user_id = message.chat.id
    if user_id not in user_messages:
        user_messages[user_id] = []
    user_messages[user_id].append(message.text)
    bot.reply_to(message, "Сообщение сохранено.")

# Запускаем бота
bot.polling()