import asyncio
import logging
import sys

from aiogram import Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from core.logger import logger
from core.redis_settings import redis_settings
from handlers import register_handlers
from loader import bot
from database.database import init_db

dp = Dispatcher(
    storage=RedisStorage(
        redis=Redis(host=redis_settings.host, port=redis_settings.port),
    ),
)


async def start():
    await init_db()

    register_handlers(dp=dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(start())
    except (KeyboardInterrupt, SystemExit):
        logging.info('Bot stopped!')

