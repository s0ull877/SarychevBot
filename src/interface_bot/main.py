from aiogram import Bot, Dispatcher

from settings import get_settings
from .handlers import register_handlers
from infrastructure.fatsecretClient import client


settings = get_settings()

bot = Bot(token=settings.bot_token)
dp = Dispatcher()

async def start_polling():

    register_handlers(dp)

    await dp.start_polling(bot)