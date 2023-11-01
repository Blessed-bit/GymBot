import aiogram
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import token


token = token
bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())
storage = MemoryStorage()


if __name__ == "__main__":
    from bd import *
    from handlers.handlers import *
    executor.start_polling(dp, on_startup=start_db, on_shutdown=stop_dp, skip_updates=True)