import logging
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button
from ..menu.states import MainMenuSG
from ..set_token.states import SetTokenSG
from ..set_marketfile.states import SetMarketfileSG
from ..set_expences.states import SetExpencesSG
from tgbot.logic import Scenario
from ..set_marketfile.handlers import to_upload_file
from service.user_data import UserData
from ..handlers import to_state

logger = logging.getLogger(__name__)

async def to_main_menu(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await to_state(callback.message, dialog_manager, MainMenuSG.menu)

async def to_insctruction(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await to_state(callback.message, dialog_manager, SetTokenSG.step1)
    
async def to_set_token(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await to_state(callback.message, dialog_manager, SetTokenSG.set_token)
    
async def to_set_marketfile(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    sd = dialog_manager.start_data
    state = SetMarketfileSG.file
    await Scenario.fix_moving(callback.message.chat.id, state)
    example_file = await UserData.get_example_file()
    await to_upload_file(callback.message, dialog_manager, state, example_file, filename="Шаблон таблицы.xlsx")
    sd["show_instruction"] = False
    
async def to_set_expences(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await to_state(callback.message, dialog_manager, SetExpencesSG.menu)
    

