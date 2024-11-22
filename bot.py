from aiogram import executor
from loader import bot, dp

from utils.env import ADMIN_ID

import handler

async def on_startup(dp):
    
    await bot.send_message(ADMIN_ID, 'bot ishga tushdi')
    
    
executor.start_polling(dp, on_startup=on_startup, skip_updates=False)