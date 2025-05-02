
from tgbot.logic import Scenario
from aiogram_dialog import DialogManager, ShowMode, StartMode
from aiogram.types import Message, BufferedInputFile
from service.user_data import UserData
from service.image_handler import text_putter
from tgbot.media.path import path
from datetime import datetime
from io import BytesIO
from ..set_expences.states import SetExpencesSG
from service.value_formatter import beautify_number

async def create_pre_report_pic(dialog_manager: DialogManager, clean_input: bool = False):
    if clean_input: await Scenario.clean_messages(dialog_manager)
    sd = dialog_manager.start_data
    week = await Scenario.get_choosen_week(dialog_manager)
    value = await UserData.get_variable_expence(sd["chat_id"])
    value = beautify_number(value, "руб.")
    pic = text_putter.handle_pre_report_expence(week, value)
    ...
    await Scenario.remove_content(filename)