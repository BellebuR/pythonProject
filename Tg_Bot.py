import os
import logging
from aiogram import Bot, Dispatcher, Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from gtts import gTTS
from googletrans import Translator
from aiogram.types import FSInputFile
import asyncio

from config import TOKEN  # Убедитесь, что ваш API токен определен в config.py

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

# Создаем объект переводчика
translator = Translator()

# Директория для сохранения изображений
IMG_DIR = 'img'
os.makedirs(IMG_DIR, exist_ok=True)

@router.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer(
        'Привет! Отправьте фото, и я сохраню его. Напишите текст, и я переведу его на английский. Отправлю голосовое сообщение в ответ.')

@dp.message(lambda message: message.photo)
async def handle_photos(message: types.Message):
    photo = message.photo[-1]  # Получаем фото наилучшего качества
    file_info = await bot.get_file(photo.file_id)
    filename = os.path.join(IMG_DIR, f"{photo.file_id}.jpg")
    await bot.download_file(file_info.file_path, filename)
    await message.answer('Фото сохранено!')

@router.message(F.text)
async def handle_text(message: Message):
    # Перевод текста на английский
    translated = translator.translate(message.text, dest='en')
    await message.answer(f'Перевод: {translated.text}')

    # Создание голосового сообщения
    tts = gTTS(text=translated.text, lang='en')
    voice_filename = f"{message.message_id}.mp3"
    tts.save(voice_filename)

    # Отправка голосового сообщения
    voice_file = FSInputFile(voice_filename)
    await bot.send_voice(chat_id=message.chat.id, voice=voice_file)

    # Удаление временного файла
    os.remove(voice_filename)

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())