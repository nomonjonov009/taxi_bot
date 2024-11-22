from aiogram.types import Message
from aiogram.dispatcher import FSMContext


from loader import dp, bot
from utils import buttons,texts
from utils.state import Passenger

GROUP_ID = -1002382699220

@dp.message_handler(lambda message: message.text.startswith(buttons.CHECK), state=Passenger.check)
async def check_handler(message: Message, state: FSMContext):
    
    data = await state.get_data()
    
    if message.text == [buttons.CHECK]:
        print('-----')

    count = data.get('count')
    location = data.get('location')
    phone = data.get('phone')
    username = message.from_user.username
    
    
    await bot.send_message(
        chat_id=GROUP_ID,
        text=texts.send_gruop( 
            count = count,
            phone = phone,
            location = location,
            username = username
        )
    )
    
    await message.answer('Tabriklayman sizning arizangiz ADMINGA yuborildi👍🏻🤝🏻')