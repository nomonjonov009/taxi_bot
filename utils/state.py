from aiogram.dispatcher.filters.state import State, StatesGroup


class Passenger(StatesGroup):
    count = State()
    location = State()
    phone = State()
    check = State()
    
class mail(StatesGroup):
    locations = State()
    phone = State()
    
class driver(StatesGroup):
    name = State()
    phone = State()
    
    