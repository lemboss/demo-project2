from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.input import ManagedTextInput
from service.user_data import UserData
from .states import SetTokenSG
from external.wildberries.wb_detalization import WBDetalization
from external.wildberries.wb_capitalization import WBCapitalization
from ..handlers import start
from tgbot.logic import Scenario

async def setting_token(
        message: Message, 
        widget: ManagedTextInput, 
        dialog_manager: DialogManager, 
        token: str) -> None:
    sd = dialog_manager.start_data
    ...
    await dialog_manager.start(state=state, data=sd, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)