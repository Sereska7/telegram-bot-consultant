from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.schemas.client import CreateClient
from src.crud.client import get_client, app_client
from src.keyboards.main_keyboards import main_key

router = Router()


@router.message(CommandStart())
async def start_message(message: Message, db_session: AsyncSession):
    client = await get_client(message.from_user.id, db_session)
    if not client:
        data = {
            "tg_id": message.from_user.id,
            "user_name": message.from_user.username,
            "name": message.from_user.first_name,
            "number": None
        }
        data_client = CreateClient(**data)
        await app_client(data_client, db_session)
    await message.answer(

        f'👋 Добро пожаловать, {message.from_user.first_name}! \n'
            f'Я — ваш персональный менеджер по разработке Telegram-ботов.\n'
'''
💼 <b>Что я могу предложить</b>:

🔹 <b><u>Консультация</u></b> — обсуждение возможностей и функционала для вашего проекта.

🔹 <b><u>Подбор решения</u></b> — создадим уникальный бот, который максимально соответствует вашим потребностям.

🔹<b><u>Стоимость услуг</u></b> — детальная смета и план работ.

🔹 <b><u>Оставить заявку</u></b> — оформите заявку, и мы свяжемся с вами для старта сотрудничества.

💡 Выберите действие из меню или задайте вопрос — и я помогу вам сделать первый шаг!
''', reply_markup=main_key, parse_mode="HTML")

