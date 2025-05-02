from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from config.config import settings
from service.user_data import UserData
from service.handling_data import InputDataHandler
from tgbot.logic import Scenario
from ..set_marketfile.states import SetMarketfileSG
from ..show_capitalization.states import ShowCapitalizatonSG
from ..handlers import to_state
from datetime import datetime
from tgbot.media.path import path
from service.image_handler import text_putter
import asyncio
from service.value_formatter import beautify_number

def create_pic(dialog_manager):
    sd = dialog_manager.start_data
    return text_putter.handle_capitalization(
        count_remains=beautify_number(sd["count_remains"], "шт."),
        to_clients=beautify_number(sd["sum_to_client"], "руб."),
        from_clients=beautify_number(sd["sum_from_client"], "руб."),
        in_warehouses=beautify_number(sd["sum_in_warehouse"], "руб."),
        all_remains=beautify_number(sd["sum_remains"], "руб.")
    )

async def to_show_capitalization(dialog_manager, clean_input = False):
    state = ShowCapitalizatonSG.report
    ...
    await Scenario.remove_content(filename)

async def report_logic(message: Message, dialog_manager: DialogManager):
    sd = dialog_manager.start_data
    task = asyncio.create_task(Scenario.to_show_capitalization(sd["chat_id"], dialog_manager))
    await to_state(message, dialog_manager, ShowCapitalizatonSG.download)
    await asyncio.sleep(0)
    await task
    await asyncio.sleep(0)
    if sd["missed_articles"] and any(sd["missed_articles"]):
        ...
        await asyncio.sleep(0)
        await to_upload_file(message, dialog_manager, state, file, filename=filename, clean_input=True)
    else:
        await to_show_capitalization(dialog_manager)
        
