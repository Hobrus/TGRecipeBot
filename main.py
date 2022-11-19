# 5691120266:AAGRU5wI5WImRXmmbJ3u58-a81FUGzscmgs
# КЛЮЧ ВАШ УНИКАЛЬНЫЙ

import aiogram
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from recipe_getter import get_urls_from_ingridients

API_TOKEN = "5691120266:AAGRU5wI5WImRXmmbJ3u58-a81FUGzscmgs"

bot = aiogram.Bot(token=API_TOKEN)
dp = aiogram.Dispatcher(bot)

button_hi = KeyboardButton('Ввод продуктов')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

current_products = []

button1 = KeyboardButton('Яйца')
button2 = KeyboardButton('Сахар')
button3 = KeyboardButton('Молоко')
button4 = KeyboardButton('Очистить')
button5 = KeyboardButton('Поиск')

ingridients_kb = ReplyKeyboardMarkup().add(
    button1).add(button2).add(button3).add(button4).add(button5)


@dp.message_handler(commands=['start'])
async def send_message(message: aiogram.types.Message):
    await message.reply('''Привет! Я бот с рецептами, когда ты присылаешь мне ингедиенты, я высылаю тебе рецепты.
Присылать ингридиенты надо в формате, на английском языке:

xxxx, xxxx, xxxx

Например:

eggs, sugar''', reply_markup=greet_kb)


@dp.message_handler()
async def echo(message: aiogram.types.Message):
    if message.text == 'Ввод продуктов':
        await message.reply('''Выберите продукты которые у вас есть и я найду вам рецепт.
        Для того, что бы начать заново нажмите очистить. Когда будете готовы нажмите поиск.''',
                            reply_markup=ingridients_kb)
    if message.text == 'Яйца':
        current_products.append('egg')
    if message.text == 'Молоко':
        current_products.append('milk')
    if message.text == 'Сахар':
        current_products.append('sugar')
    if message.text == 'Очистить':
        current_products.clear()
    if message.text == 'Поиск':
        ingridients = current_products
        urls = get_urls_from_ingridients(*ingridients)
        answer = ''
        for url in urls:
            answer += url + '\n'
        await message.answer(answer)


aiogram.executor.start_polling(dp, skip_updates=True)
