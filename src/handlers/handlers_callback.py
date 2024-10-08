from aiogram import Router, F
from aiogram.types import CallbackQuery

from src.keyboards.inline_keyboards import keyboard_type_bot

router = Router()


@router.callback_query(F.data.startswith('search_solution'))
async def search_solution(callback: CallbackQuery):
    await callback.answer(text="Собираем подборку")
    await callback.message.answer(text='''🎯 Вот подборка частых решений для определённых ботов:

Выберите один из вариантов ниже, чтобы узнать подробнее или предложите свой!''', reply_markup=await keyboard_type_bot())


