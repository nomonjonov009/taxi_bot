from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import buttons, texts
from utils.state import Passenger
from utils.env import GROUP_ID
from ..start import start_handler

@dp.message_handler(lambda message: message.text.startswith(buttons.CANCEL), state='*')
async def check_handler(message: Message, state: FSMContext):
    await message.answer(texts.PHONE, reply_markup=buttons.PHONE)

    await Passenger.phone.set()