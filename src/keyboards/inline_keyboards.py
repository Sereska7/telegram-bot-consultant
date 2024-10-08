from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


async def button_search():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="🛠 Посмотреть готовые решения для ботов",
                                      callback_data="search_solution"))
    return keyboard.as_markup()


async def keyboard_type_bot():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="🛍 Бот-магазин", callback_data="bot_shop"))
    keyboard.add(InlineKeyboardButton(text="📊 Аналитический бот", callback_data="bot_analytics"))
    keyboard.add(InlineKeyboardButton(text="📝 Бот-консультант", callback_data="bot_consultant"))
    keyboard.add(InlineKeyboardButton(text="⚙️ Техническая поддержка", callback_data="bot_support"))
    keyboard.add(InlineKeyboardButton(text="📅 Бот для бронирования", callback_data="bot_booking"))
    keyboard.add(InlineKeyboardButton(text="🎓 Обучающий бот", callback_data="bot_education"))
    keyboard.adjust(2)
    keyboard.add(InlineKeyboardButton(text="🤖 Написать свой вариант", callback_data="custom_bot"))
    keyboard.adjust(1)

    return keyboard.as_markup()
