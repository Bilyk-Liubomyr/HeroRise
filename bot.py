import asyncio
import nest_asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
import os
import logging
import multiprocessing

nest_asyncio.apply()  # Allow nested event loops

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.reply("Привіт! Це твій бот для розвитку! 🚀")

def run_bot():
    asyncio.run(dp.start_polling(bot))

if __name__ == "__main__":
    # Запускаємо бота в окремому процесі
    bot_process = multiprocessing.Process(target=run_bot)
    bot_process.start()
    bot_process.join()  # Дозволяє виконати інші задачі в Jupyter
