import logging
from datetime import datetime
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import ShowMode
from .states import SetExpencesSG
from ..update_data.states import UpdateDataSG
from service.user_data import UserData
from ..handlers import to_menu
from tgbot.logic import Scenario
from ..show_report.logic import show_report_logic
from ..handlers import to_state

async def to_set_stable(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await to_state(callback.message, dialog_manager, SetExpencesSG.set_stable)
  
async def to_set_variable(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await to_state(callback.message, dialog_manager, SetExpencesSG.set_variable)
        
async def to_update_data(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await to_state(callback.message, dialog_manager, UpdateDataSG.menu)    
    
async def to_update_expences_menu(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await to_state(callback.message, dialog_manager, SetExpencesSG.menu)    
    
async def to_standart_report(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await show_report_logic.to_standart_report(dialog_manager, True)