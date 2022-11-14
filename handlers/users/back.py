from loader import dp
from aiogram import types
from states.state_btn import Convert
from keyboards.inline.main import main_button
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="◀️Orqaga", state='*')
async def kril_menu(message: types.Message, state: FSMContext):
    await message.delete()
    await message.answer("<b>Men sizga <i>Lotin</i> yozilgan textni <i>Kirilga</i> va <i>Kirilda</i> yozilgan textni <i>Lotinga</i> o'girib beraman🫡</b>", reply_markup=main_button)
    await state.finish()