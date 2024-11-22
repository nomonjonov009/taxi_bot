
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp,bot
from utils.env import GROUP_ID
from utils import texts, buttons
from utils.state import mail
from asyncio import create_task




async def passenger_handler_task(message: Message, state: FSMContext):

    phone = message.contact.phone_number
    print(phone)

    await state.update_data({
        'phone':phone
    })

    data = await state.get_data()
    location = data.get('location')

    
    await bot.send_message(
        chat_id=GROUP_ID,
        text=texts.send_mail( 
            phone=phone,
            location=location,
        )
    )
    
    await message.answer('Tabriklayman sizning arizangiz ADMINGA yuborildi👍🏻🤝🏻')
    
    await state.finish()


@dp.message_handler(content_types=('contact', 'text'), state=mail.phone)
async def passenger_handler(message: Message, state: FSMContext):
    if message.text in [buttons.BASE_BACK]:
         await message.answer(texts.LOCATION, reply_markup=buttons.LOCATION)
         await mail.location.set()
    else:
        await create_task(passenger_handler_task(message, state))
