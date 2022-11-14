from loader import dp
from aiogram import types
from states.state_btn import Convert
from aiogram.dispatcher import FSMContext
from .transliterate import to_cyrillic, to_latin
from keyboards.default.back import back

@dp.callback_query_handler(text="kiriltolotin", state='*')
async def convertlatin(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Lotinga o'girmoqchi bo'lgan textni kiriting🔽</b>")
    await Convert.tolatin.set()

@dp.message_handler(state=Convert.tolatin)
async def convlotin(message: types.Message, state: FSMContext):
    msg = message.text
    # print(msg)
    convertlotin = to_latin(msg)
    await message.answer(text=convertlotin, reply_markup=back)
    await state.finish()

