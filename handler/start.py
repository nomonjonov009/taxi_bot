from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import texts, buttons


   
   
@dp.message_handler(commands=['start'], state="*")
async def start_handler(message: Message, state: FSMContext):
    await message.answer(texts.START, reply_markup=buttons.START)
    await state.finish()