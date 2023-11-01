from aiogram import types
from bd import *
from workout_calculation import *
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from main import dp, bot, storage
from button.MenuButton import *
from button.inlinebutton import *
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@dp.message_handler(commands=["start"])
async def start(message: types.message):
    if await check_user_in_db(message.chat.id):
        await create_profile(message.chat.id)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb_menu)
    await bot.send_message(text="Здарова заебал",
                           chat_id=message.chat.id,
                           reply_markup=keyboard
                           )
    await message.delete()


@dp.message_handler(Text(equals="Назад"))
async def start(message: types.message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb_menu)
    await bot.send_message(text="Возвращаю вас в меню",
                           chat_id=message.chat.id,
                           reply_markup=keyboard)


@dp.message_handler(Text(equals="Мой профиль"))
async def start(message: types.message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb_menu_edit)
    height = show_height(message.chat.id)
    weight = show_weight(message.chat.id)
    await bot.send_message(text=f"Ваше имя: {message.from_user.first_name}\nВаш рост: {height}см\nВаш Вес: {weight}кг",
                           chat_id=message.chat.id,
                           reply_markup=keyboard)
    await message.delete()


@dp.message_handler(Text(equals="Мои показатели"))
async def start(message: types.message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb_weight)
    bench_press = show_bench_press(message.chat.id)
    deadlift = show_deadlift(message.chat.id)
    squat = show_squat(message.chat.id)
    await bot.send_message(text=f"Твои показатели:\nЖим лежа: {bench_press}кг\nПрисед со штангой: {squat}кг\nСтановая тяга: {deadlift}кг\n",
                           chat_id=message.chat.id,
                           reply_markup=keyboard)
    await message.delete()


@dp.message_handler(Text(equals="Моя тренировка"))
async def start(message: types.message):
    dead = calculation_dead(userid=message.chat.id)
    squat = calculation_squat(userid=message.chat.id)
    bench_press = calculation_bench_press(userid=message.chat.id)
    await bot.send_message(text=f"Вот примерные веса для хорошей тренировки:\nЖим лежа: {int(bench_press)}кг, 3 подхода\nПрисед со штангой: {int(squat)}кг, 3 подхода\nСтановая тяга: {int(dead)}кг 3 подхода",
                           chat_id=message.chat.id,
                           parse_mode="Markdown")
    await message.delete()


@dp.message_handler(Text(equals="Изменить жим"))
async def start(message: types.message, state: FSMContext):
    await bot.send_message(text="Введите вес снаряда:",
                           chat_id=message.chat.id)
    await state.set_state("bench_press")
    await message.delete()


@dp.message_handler(Text(equals="Изменить присед"))
async def start(message: types.message, state: FSMContext):
    await bot.send_message(text="Введите вес снаряда:",
                           chat_id=message.chat.id)
    await state.set_state("squat")
    await message.delete()


@dp.message_handler(Text(equals="Изменить становую"))
async def start(message: types.message, state: FSMContext):
    await bot.send_message(text="Введите вес снаряда:",
                           chat_id=message.chat.id)
    await state.set_state("deadlift")
    await message.delete()


@dp.message_handler(Text(equals="Редактировать рост"))
async def start(message: types.message, state: FSMContext):
    await bot.send_message(text="Введите ваш рост:",
                           chat_id=message.chat.id)
    await state.set_state("Height")
    await message.delete()


@dp.message_handler(Text(equals="Редактировать вес"))
async def start(message: types.message, state: FSMContext):
    await bot.send_message(text="Введите ваш вес:",
                           chat_id=message.chat.id)
    await state.set_state("Weight")
    await message.delete()


@dp.message_handler(state="bench_press")
async def start(message: types.message, state: FSMContext):
    bench_press1 = message.text
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb_weight)
    await bench_press(bench=bench_press1, userid=message.chat.id)
    await bot.send_message(text="Ваши данные сохранены",
                           chat_id=message.chat.id,
                           reply_markup=keyboard)
    await state.finish()



@dp.message_handler(state="squat")
async def start(message: types.message, state: FSMContext):
    squat1 = message.text
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb_weight)
    await squat(squat=squat1, userid=message.chat.id)
    await bot.send_message(text="Ваши данные сохранены",
                           chat_id=message.chat.id,
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(state="deadlift")
async def start(message: types.message, state: FSMContext):
    deadlift1 = message.text
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb_weight)
    await deadlift(deadlift=deadlift1, userid=message.chat.id)
    await bot.send_message(text="Ваши данные сохранены",
                           chat_id=message.chat.id,
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(state="Height")
async def start(message: types.message, state: FSMContext):
    Height1 = message.text
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb_menu)
    await add_height(height=Height1, userid=message.chat.id)
    await bot.send_message(text="Ваши данные сохранены",
                           chat_id=message.chat.id,
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(state="Weight")
async def start(message: types.message, state: FSMContext):
    Weight = message.text
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb_menu)
    await add_weight(weight=Weight, userid=message.chat.id)
    await bot.send_message(text="Ваши данные сохранены",
                           chat_id=message.chat.id,
                           reply_markup=keyboard)
    await state.finish()