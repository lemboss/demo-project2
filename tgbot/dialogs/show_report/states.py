from aiogram.fsm.state import State, StatesGroup

class ShowReportSG(StatesGroup):
    download = State()
    standart = State()
    deep = State()
    missed_supplier = State()
    select_dates = State()