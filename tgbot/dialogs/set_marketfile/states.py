from aiogram.fsm.state import State, StatesGroup

class SetMarketfileSG(StatesGroup):
    file = State()
    overflow_file = State()
    incorrect_file_extencion = State()
    incorrect_file_rows = State()
    missed_articles = State()
    success = State()