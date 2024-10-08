import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from src.core.config import settings
from src.handlers.commands import router as router_commands

from src.core.middleware.db_session import DbSessionMiddleware
from src.handlers.handlers_main_menu import router as router_main_menu
from src.handlers.handlers_callback import router as router_callback


async def main():
    load_dotenv()
    bot = Bot(token=settings.TOKEN)
    dp = Dispatcher()
    # Регистрация middleware для работы с сессией
    dp.update.middleware(DbSessionMiddleware())
    dp.include_router(router_commands)
    dp.include_router(router_main_menu)
    dp.include_router(router_callback)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    try:
        print("Bot online")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot offline")
