from aiogram.types import Message
from aiogram.dispatcher import FSMContext



from loader import dp
from utils import texts, buttons
from utils.state import mail

@dp.message_handler(lambda message: message.text.startswith(buttons.MAIL), state="*")
async def check_handler(message: Message, state: FSMContext):
    
    await message.answer(texts.MAIL_HANDELR, reply_markup=buttons.LOCATION)
    await mail.locations.set()
    
    