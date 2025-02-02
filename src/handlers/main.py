from aiogram import F, Router  # noqa: WPS347
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(CommandStart())
async def command_start_menu(message: Message, state: FSMContext):
    await message.answer("hello")