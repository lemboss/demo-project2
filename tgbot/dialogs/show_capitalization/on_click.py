import logging
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button
from tgbot.logic import Scenario
from ..handlers import to_state
from ..get_reports.states import GetReportsSG
from ..handlers import start

logger = logging.getLogger(__name__)

async def to_get_reports_menu(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await to_state(callback.message, dialog_manager, GetReportsSG.menu)
    
async def to_main_menu(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await start(callback.message, dialog_manager)