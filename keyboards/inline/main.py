from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Lotindan-Kirilga🔄", callback_data='lotintocyril')],
        [InlineKeyboardButton(text="Kirildan-Lotinga🔄", callback_data='kiriltolotin')]
    ]
)