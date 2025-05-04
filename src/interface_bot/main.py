from aiogram import Bot, Dispatcher

from settings import get_settings

settings = get_settings()

async def start_polling():

    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()

    await dp.start_polling(bot)