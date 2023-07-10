from aiogram.fsm.state import StatesGroup, State


class Registration(StatesGroup):
    ask_city = State()
    complete = State()


class Tracker(StatesGroup):
    action = State()
    category = State()
    subcategory = State()
    income_source = State()
    amount = State()
