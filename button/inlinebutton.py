from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import KeyboardButton


inline_btn_1 = InlineKeyboardButton('Изменить вес', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('Изменить рост', callback_data='button2')

inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2)