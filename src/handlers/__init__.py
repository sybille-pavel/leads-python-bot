from aiogram import Dispatcher
from . import lead


def register_handlers(dp: Dispatcher):
    dp.include_router(lead.router)
