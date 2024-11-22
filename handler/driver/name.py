from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from asyncio import create_task



from loader import dp
from utils import texts, buttons
from utils.state import driver



@dp.message_handler(content_types=('text'), state=driver.name)
async def passenger_handler_task(message: Message, state: FSMContext):

    name = message.text
    
    await state.update_data({
        'name': name
    })
    
    await message.answer(texts.PHONE, reply_markup=buttons.PHONE)
    await driver.phone.set()

 

    