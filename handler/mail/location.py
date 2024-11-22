from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from asyncio import create_task



from loader import dp
from utils import texts, buttons
from utils.state import mail



@dp.message_handler(content_types=('text'), state=mail.locations)
async def passenger_handler_task(message: Message, state: FSMContext):


    location = message.text
    
    await state.update_data({
        'location': location
    })
    
    await message.answer(texts.PHONE, reply_markup=buttons.PHONE)
    await mail.phone.set()

 

    