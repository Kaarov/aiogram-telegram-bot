import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command

import config

dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f"Hello, {message.from_user.full_name}")


@dp.message(Command("help"))
async def handle_help(message: types.Message):
    text = "I'm and echo bot. \nSend me a message!"
    await message.answer(text=text)


@dp.message()
async def echo_message(message: types.Message):
    # await bot.send_message(
    #     chat_id=message.chat.id,
    #     text="Start processing...",
    # )
    # await bot.send_message(
    #     chat_id=message.chat.id,
    #     text="Detected message",
    #     reply_to_message_id=message.message_id,
    # )

    await message.answer(text="Wait a second...")

    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Something new 😄")

    # await message.answer(text=message.text)
    # await message.send_copy(chat_id=message.chat.id)
    # if message.text:
    #     await message.reply(text=message.text)
    # elif message.sticker:
    #     await message.bot.send_sticker(
    #         chat_id=message.chat.id,
    #         sticker=message.sticker.file_id,
    #     )
    # await message.reply(text=message.sticker.file_id)
    # elif message.photo:
    #     await message.reply(photo=message.photo)
    # else:
    #     await message.reply(text="Something new)")


async def main():
    bot = Bot(token=config.BOT_TOKEN)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
