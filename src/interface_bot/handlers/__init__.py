from aiogram import Bot

from settings import get_settings

settings = get_settings()
bot = Bot(settings.bot_token)