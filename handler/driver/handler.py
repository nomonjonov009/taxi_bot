from aiogram.types import Message
from aiogram.dispatcher import FSMContext



from loader import dp
from utils import texts, buttons
from utils.state import driver

@dp.message_handler(lambda message: message.text.startswith(buttons.DRIVER), state="*")
async def check_handler(message: Message, state: FSMContext):
    
    await message.answer(texts.driver_handler, reply_markup=buttons.BACK_handler)
    await driver.name.set()
    
    