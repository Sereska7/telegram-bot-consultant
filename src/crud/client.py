from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.models import Client
from src.core.schemas.client import CreateClient


async def app_client(data_client: CreateClient, session: AsyncSession):
    user = Client(**data_client.model_dump())
    session.add(user)
    await session.commit()
    return user


async def get_client(tg_id: int, session: AsyncSession):
    request = select(Client).where(Client.tg_id == tg_id)
    user = await session.execute(request)
    return user.scalar_one_or_none()
