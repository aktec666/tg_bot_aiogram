import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6905579810:AAHrJJqhIawfpVccf6zV9nrFWQgW4wkW2XY")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("kodland"))
async def cmd_kodland(message: types.Message):
    await message.answer("programm")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())