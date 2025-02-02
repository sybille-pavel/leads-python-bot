from aiogram import Dispatcher
from . import main


def register_handlers(dp: Dispatcher):
    dp.include_router(main.router)
