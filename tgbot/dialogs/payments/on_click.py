import logging
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button
from ..payments.states import PaymentsSG
from ..menu.states import MainMenuSG
from ..handlers import to_state
from tgbot.logic import Scenario

logger = logging.getLogger(__name__)

async def to_main_menu(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await to_state(callback.message, dialog_manager, MainMenuSG.menu)
    
async def to_payments_menu(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await to_state(callback.message, dialog_manager, PaymentsSG.menu)