import logging
from datetime import datetime
from aiogram.types import CallbackQuery, Message
from aiogram.types.input_file import FSInputFile
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import ShowMode
from tgbot.dialogs.get_reports.states import GetReportsSG
from ..menu.states import MainMenuSG
from .states import ShowReportSG
from service.user_data import UserData
from ..handlers import start
from service.handling_data import InputDataHandler
from aiogram.types import BufferedInputFile
from tgbot.logic import Scenario
from .logic import show_report_logic
from utils.memory_analys import hp

logger = logging.getLogger(__name__)

async def to_menu(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await Scenario.clean_messages(dialog_manager)
    await start(callback.message, dialog_manager)
    
async def to_update_data_menu(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    state = MainMenuSG.menu
    await Scenario.fix_moving(callback.message.chat.id, state)
    data = await Scenario.get_fields(callback.message.chat.id)
    dialog_manager.start_data.clear()
    await dialog_manager.start(state, data=data, mode=StartMode.RESET_STACK)
    
async def to_deep_report(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await show_report_logic.to_suppliers_report(callback.message, dialog_manager, clean_input=True)
    
async def to_simple_report(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await show_report_logic.to_standart_report(dialog_manager, clean_input=True)

async def to_missed_suplier_report(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await show_report_logic.to_wo_suppliers_report(callback.message, dialog_manager, clean_input=True)
    
async def to_get_reports_menu(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    state = GetReportsSG.menu
    await Scenario.fix_moving(callback.message.chat.id, state)
    await dialog_manager.start(state, data=dialog_manager.start_data, mode=StartMode.RESET_STACK, show_mode=ShowMode.EDIT) 