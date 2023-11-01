from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


kb_menu = [
    [
        KeyboardButton(text="Мой профиль"),
        KeyboardButton(text="Моя тренировка"),
        KeyboardButton(text="Мои показатели"),
    ]
]


kb_menu_edit = [
    [
        KeyboardButton(text="Редактировать вес"),
        KeyboardButton(text="Редактировать рост"),
        KeyboardButton(text="Назад")
    ]
]


kb_weight = [
    [
        KeyboardButton(text="Изменить жим"),
        KeyboardButton(text="Изменить присед"),
        KeyboardButton(text="Изменить становую"),
        KeyboardButton(text="Назад")
    ]
]



