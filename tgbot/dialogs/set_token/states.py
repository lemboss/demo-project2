from aiogram.fsm.state import State, StatesGroup

class SetTokenSG(StatesGroup):
    set_token = State()
    step1 = State()
    step2 = State()
    step3 = State()
    step4 = State()
    success = State()