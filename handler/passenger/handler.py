from aiogram.types import Message
from aiogram.dispatcher import FSMContext



from loader import dp
from utils import texts, buttons
from utils.state import Passenger



@dp.message_handler(lambda message: message.text.startswith(buttons.PASSENGER), state='*')
async def passenger_handler(message: Message, state: FSMContext):



    await message.answer(texts.PASSENGER_HANDLER, reply_markup=buttons.COUNT)

    await Passenger.count.set()