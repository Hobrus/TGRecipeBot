# 5691120266:AAGRU5wI5WImRXmmbJ3u58-a81FUGzscmgs
# КЛЮЧ ВАШ УНИКАЛЬНЫЙ

import aiogram

API_TOKEN = "5691120266:AAGRU5wI5WImRXmmbJ3u58-a81FUGzscmgs"

bot = aiogram.Bot(token=API_TOKEN)
dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_message(message: aiogram.types.Message):
    await message.reply("Привет! Я бот с рецептами, когда ты присылаешь мне ингедиенты, я высылаю тебе рецепты")


@dp.message_handler()
async def echo(message: aiogram.types.Message):
    await message.answer(message.text)

aiogram.executor.start_polling(dp, skip_updates=True)
