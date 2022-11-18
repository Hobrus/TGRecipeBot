# 5691120266:AAGRU5wI5WImRXmmbJ3u58-a81FUGzscmgs
# КЛЮЧ ВАШ УНИКАЛЬНЫЙ

import aiogram

API_TOKEN = "5691120266:AAGRU5wI5WImRXmmbJ3u58-a81FUGzscmgs"

bot = aiogram.Bot(token=API_TOKEN)
dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_message(message: aiogram.types.Message):
    await message.reply("Hello")
