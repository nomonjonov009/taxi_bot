from aiogram.types import Message
from aiogram.dispatcher import FSMContext




from loader import dp
from utils import texts, buttons
from utils.state import Passenger



@dp.message_handler(content_types=('text'), state=Passenger.count)
async def passenger_handler(message: Message, state: FSMContext):


    count = message.text
    
    await state.update_data({
        'count': count
    })

    await message.answer(texts.LOCATION, reply_markup=buttons.LOCATION)

    await Passenger.location.set() 

