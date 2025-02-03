from aiogram import Dispatcher
from . import lead, admin


def register_handlers(dp: Dispatcher):
    dp.include_router(lead.router)
    dp.include_router(admin.router)
