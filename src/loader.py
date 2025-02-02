from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from core.bot_settings import bot_settings

bot = Bot(token=bot_settings.bot_token,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML)
          )
