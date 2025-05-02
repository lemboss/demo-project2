from aiogram.fsm.state import State, StatesGroup

class PaymentsSG(StatesGroup):
    menu = State()
    expirated = State()
    create = State()
    success = State()
    fail = State()