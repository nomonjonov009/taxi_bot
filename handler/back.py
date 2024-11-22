from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import buttons, texts
from . start import start_handler


from aiogram.types import message
from aiogram.dispatcher import FSMContext


from loader import dp, Bot
from utils import buttons,texts
from utils.env import GROUP_ID
from .start import start_handler




dp.message_handler(lambda message: message.text.startwith(buttons.BASE_BACK), state='*')
async def passenger_handler(message: Message, state: FSMContext):
    
    await start_handler(message, state)

