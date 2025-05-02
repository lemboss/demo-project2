import logging
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button
from ..update_data.states import UpdateDataSG
from ..get_reports.states import GetReportsSG
from ..payments.states import PaymentsSG
from ..preview.states import PreviewSG
from tgbot.logic import Scenario
from ..handlers import to_state

logger = logging.getLogger(__name__)

async def to_update_data_menu(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    sd = dialog_manager.start_data
    state = UpdateDataSG.menu
    await Scenario.fix_moving(callback.message.chat.id, state)
    await dialog_manager.start(state, data=sd, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)
    
async def to_get_reports_menu(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    sd = dialog_manager.start_data
    state = GetReportsSG.menu
    await Scenario.fix_moving(callback.message.chat.id, state)
    await dialog_manager.start(state, data=sd, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)
    
async def to_payments_menu(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await to_state(callback.message, dialog_manager, state=PaymentsSG.menu)
    
async def to_preview_video(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await to_state(callback.message, dialog_manager, state=PreviewSG.menu)