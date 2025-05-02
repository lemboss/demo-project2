import logging
from datetime import datetime
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import ShowMode
from ..get_reports.states import GetReportsSG
from ..set_expences.states import SetExpencesSG
from ..update_data.states import UpdateDataSG
from ..show_report.states import ShowReportSG
from tgbot.logic import Scenario

# logger = logging.getLogger(__name__)
    
async def to_update_data(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    state = UpdateDataSG.menu
    await Scenario.fix_moving(callback.message.chat.id, state)
    await Scenario.clean_messages(dialog_manager)
    await dialog_manager.start(state, data=dialog_manager.start_data, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)
    
async def to_set_expences(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    state = SetExpencesSG.menu
    await Scenario.fix_moving(callback.message.chat.id, state)
    await dialog_manager.start(state, data=dialog_manager.start_data, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)
    
async def to_get_reports(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    state = GetReportsSG.menu
    await Scenario.fix_moving(callback.message.chat.id, state)
    await dialog_manager.start(state, data=dialog_manager.start_data, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)
    
async def to_choose_weeks(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    state = ShowReportSG.select_dates
    await Scenario.fix_moving(callback.message.chat.id, state)
    await Scenario.clean_messages(dialog_manager)
    await dialog_manager.start(state, data=dialog_manager.start_data, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)
    
