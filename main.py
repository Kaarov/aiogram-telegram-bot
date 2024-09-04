import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher

from aiogram.enums import ParseMode

from config import settings
from routers import router as main_router
from aiogram.client.bot import DefaultBotProperties


async def main():
    dp = Dispatcher()
    dp.include_router(main_router)

    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=settings.bot_token,
        # default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
