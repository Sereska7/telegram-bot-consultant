from contextlib import asynccontextmanager

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Callable, Awaitable, Dict, Any

from src.core.models.db_helper import db_helper


class DbSessionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        # Используем session_getter для создания сессии
        async with db_helper.session_getter() as session:
            data["db_session"] = session  # Передаем сессию в хендлер
            return await handler(event, data)
