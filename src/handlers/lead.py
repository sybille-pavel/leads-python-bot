from aiogram import F, Router  # noqa: WPS347
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.state import Lead
from keyboards import keyboards
from static import messages

router = Router()


# Обработчик команды /start
@router.message(CommandStart())
async def command_start_menu(message: Message, state: FSMContext):
    await message.answer(messages.GET_NAME)
    await state.set_state(Lead.name)


# Получаем имя
@router.message(Lead.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(messages.GET_CONTACT_OR_USERNAME)
    await state.set_state(Lead.contact)


# Получаем контакт
@router.message(Lead.contact, F.text)
async def process_contact(message: Message, state: FSMContext):
    await state.update_data(contact=message.text)
    await message.answer(messages.GET_PRODUCT, reply_markup=keyboards.product_buttons)
    await state.set_state(Lead.product)


# Получаем продукт
@router.callback_query(F.data.startswith("product_"))
async def process_product(callback_query, state: FSMContext):
    await state.update_data(product=callback_query.data.replace("product_", ""))
    await callback_query.message.answer(messages.GET_TIME, reply_markup=keyboards.time_buttons)
    await state.set_state(Lead.time)

    await callback_query.answer()


# Получаем время и записываем в БД
@router.callback_query(F.data.startswith("time_"))
async def process_time(callback_query, state: FSMContext):
    user_data = await state.get_data()
    user_data["time"] = callback_query.data.replace("time_", "")


    await callback_query.message.answer(messages.FINAL)
    await state.clear()
    await callback_query.answer()
