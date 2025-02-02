from aiogram.fsm.state import State, StatesGroup


class Lead(StatesGroup):
    name = State()
    contact = State()
    product = State()
    time = State()