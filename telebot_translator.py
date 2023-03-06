import logging

from aiogram import Bot, types 
from aiogram.dispatcher import Dispatcher 
from aiogram.utils import executor 

from dictfunc import translator

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',\
                    filename = './log_journal.txt', level = logging.INFO,\
                        datefmt='%Y-%m-%d %H:%M:%S')

TOKEN = 'your_telegram-bot_token'

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def start_command(message : types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f"{user_name=} {user_id=} sent message: {message.text}")
    text = f"Hello, {user_name}! I can translate your name for a flight ticket! Please,\
        enter your name in capslock in cyrillic."
    await message.reply(text)


@dp.message_handler(commands = ['help'])
async def help_command(message : types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f"{user_name=} {user_id=} sent message: {message.text}")
    await message.reply('Hi! I will translate your name for a flight ticket!')


@dp.message_handler()
async def name_translation(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f"{user_name=} {user_id=} sent message: {message.text} bot reply: {translator(message.text)}")
    await bot.send_message(message.from_user.id, translator(message.text))


if __name__ == '__main__':
    executor.start_polling(dp)