from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    async_sessionmaker,
    AsyncSession,
)

from src.core.config import settings


# Класс помощника для управления соединениями с базой данных и сессиями.
class DatabaseHelper:
    def __init__(
        self,
        url: str,  # URL подключения к базе данных
        echo: bool = False,  # Логгирование SQL-запросов
        echo_pool: bool = False,  # Логгирование операций пула
        pool_size: int = 5,  # Размер пула подключений
        max_overflow: int = 10,  # Максимальное количество дополнительных подключений
    ) -> None:
        """
        Инициализирует экземпляр DatabaseHelper, создавая асинхронный движок базы данных
        и фабрику сессий с настраиваемыми параметрами.
        """
        # Создание асинхронного движка для подключения к базе данных
        self.engine: AsyncEngine = create_async_engine(
            url=url
        )

        # Создание фабрики для сессий базы данных
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False
        )

    async def dispose(self) -> None:
        """
        Закрывает все подключения движка к базе данных, очищая пул.
        """
        await self.engine.dispose()

    @asynccontextmanager
    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Асинхронный контекстный менеджер для получения сессии базы данных.
        Используйте его в middleware и хендлерах для работы с базой данных.
        """
        async with self.session_factory() as session:
            try:
                yield session
            finally:
                await session.close()


# Создание экземпляра DatabaseHelper с настройками из переменных окружения
db_helper = DatabaseHelper(
    url=str(settings.DB_URL)
)
