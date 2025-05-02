import logging
from datetime import datetime
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import ShowMode
from service.user_data import UserData
from ..set_marketfile.handlers import to_upload_file
from ..menu.states import MainMenuSG
from ..show_report.states import ShowReportSG
from ..set_token.states import SetTokenSG
from ..set_marketfile.states import SetMarketfileSG
from ..show_capitalization.states import ShowCapitalizatonSG
from ..show_capitalization.logic import report_logic
from ..handlers import to_state
from tgbot.logic import Scenario

logger = logging.getLogger(__name__)

async def to_main_menu(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await to_state(callback.message, dialog_manager, MainMenuSG.menu)
    
async def to_select_dates(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await to_state(callback.message, dialog_manager, ShowReportSG.select_dates)

async def to_set_token(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await to_state(callback.message, dialog_manager, SetTokenSG.set_token)
    
async def to_set_marketfile(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    sd = dialog_manager.start_data
    state = SetMarketfileSG.file
    await Scenario.fix_moving(callback.message.chat.id, state)
    example_file = await UserData.get_example_file()
    await to_upload_file(callback.message, dialog_manager, state, example_file, filename="Шаблон таблицы.xlsx")
    sd["show_instruction"] = False
    
async def to_show_capitalization(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await report_logic(callback.message, dialog_manager)
