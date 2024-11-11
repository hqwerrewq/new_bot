import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from client import client
from src.keyboards.command import setup_bot_command
from src.settings.config import config
from routers import get_apps_router


async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(get_apps_router())
    bot = Bot(token=config.BOT_TOKEN)
    await client.start()
    await setup_bot_command(bot=bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
