from aiogram.fsm.state import State, StatesGroup

class ShowCapitalizatonSG(StatesGroup):
    report = State()
    download = State()