from aiogram.fsm.state import State, StatesGroup

class SetExpencesSG(StatesGroup):
    menu = State()
    set_variable = State()
    set_stable = State()
    pre_report = State()
