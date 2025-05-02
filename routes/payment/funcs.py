from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.api.protocols import BgManagerFactory
from aiogram.fsm.state import State
from aiogram import Bot
from tgbot.logic import Scenario
from datetime import datetime

async def switch_dialog(bot: Bot, state: State, bg_factory: BgManagerFactory, chat_id: int):
    bg_manager: DialogManager = bg_factory.bg(
        user_id=chat_id,
        chat_id=chat_id,
        bot=bot
    )
    data = await Scenario.get_fields(chat_id)
    await bg_manager.start(state, data=data, mode=StartMode.RESET_STACK, show_mode=ShowMode.EDIT)
    
def stack_time(subs):
    d = max(subs, key=lambda r: r.expiration_at)
    days = (d.expiration_at - datetime.now()).days
    if days >= 0: return days
    else: return 0
    