import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_polling
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привіт! Це твій бот для розвитку! 🚀")

if __name__ == "__main__":
    start_polling(dp)
