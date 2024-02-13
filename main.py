import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from config import *

bot = Bot(token=Token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "<b>Assalomu alaykum!</b>😆", parse_mode="HTML")
    print(message.from_user.full_name, message.from_user.id, message.from_user.username)


@dp.message(F.text == "Question")
async def question(message: types.Message):
    await message.answer_poll(
        question="Assalomu alaykum!",
        options=['11', '22', '33'],
        type="quiz",
        correct_option_id=0,
        explanation='Togrisi: 11',
        open_period=10,
        close_date=10,
        is_anonymous=False
    )


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
