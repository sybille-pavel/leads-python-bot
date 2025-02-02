from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from static import callback_data, buttons

# Кнопки выбора
product_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=buttons.product_1, callback_data=callback_data.product_1)],
        [InlineKeyboardButton(text=buttons.product_2, callback_data=callback_data.product_2)]
    ]
)

time_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=buttons.time_morning, callback_data=callback_data.time_morning)],
        [InlineKeyboardButton(text=buttons.time_afternoon, callback_data=callback_data.time_afternoon)],
        [InlineKeyboardButton(text=buttons.time_evening, callback_data=callback_data.time_evening)]
    ]
)