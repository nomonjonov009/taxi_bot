
from aiogram.types import Message
from aiogram.dispatcher import FSMContext



from loader import dp,bot
from utils.env import ADMIN_ID
from utils import texts, buttons
from utils.state import driver
from asyncio import create_task




@dp.message_handler(content_types=('contact'), state=driver.phone)
async def passenger_handler_task(message: Message, state: FSMContext):

    phone = message.contact.phone_number

    await state.update_data({
        'phone':phone
    })

    data = await state.get_data()
    name = data.get('name')

    
    
    await bot.send_message(
        chat_id=ADMIN_ID,
        text=texts.send_driver( 
            phone = phone,
            name = name,
        )
    )
    
    await message.answer('Tabriklayman sizning arizangiz ADMINGA yuborildi👍🏻🤝🏻')
    
    await state.finish()


@dp.message_handler(content_types=('contact', 'text'), state=driver.phone)
async def passenger_handler(message: Message, state: FSMContext):
    if message.text in [buttons.BASE_BACK]:
         await message.answer(texts.LOCATION, reply_markup=buttons.LOCATION)
         await driver.name.set()
    else:
        await create_task(passenger_handler_task(message, state))
