from aiogram.types import Message
from aiogram.dispatcher import FSMContext



from loader import dp
from utils import texts, buttons
from utils.state import Passenger
from asyncio import create_task




@dp.message_handler(content_types=('contact'), state=Passenger.phone)
async def passenger_handler_task(message: Message, state: FSMContext):

    phone = message.contact.phone_number

    await state.update_data({
        'phone':phone
    })

    data = await state.get_data()
    count = data.get('count')
    location = data.get('location')

    await message.answer(
        texts.check(
            count=count,
            location=location,
            phone=phone
        ), reply_markup=buttons.SEND_GROUP)
    
    await Passenger.check.set()


@dp.message_handler(content_types=('contact', 'text'), state=Passenger.phone)
async def passenger_handler(message: Message, state: FSMContext):
    if message.text in [buttons.BASE_BACK]:
         await message.answer(texts.LOCATION, reply_markup=buttons.LOCATION)
         await Passenger.location.set()
    else:
        await create_task(passenger_handler_task(message, state))