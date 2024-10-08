from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_key = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💬Консультация"), KeyboardButton(text="🔍Подбор решения")],
        [KeyboardButton(text="📝Оставить заявку")],
        [KeyboardButton(text="💰Стоимость услуг"), KeyboardButton(text="О разработчике 👨‍💻")]
    ], resize_keyboard=True
)

consultation_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📋 Возможности Telegram-ботов"), KeyboardButton(text="🎯 Что подойдёт именно вам")],
    [KeyboardButton(text="🔙 В главное меню")]
], resize_keyboard=True)

