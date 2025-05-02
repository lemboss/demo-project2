from aiogram.types import Message, Document
from aiogram_dialog import DialogManager, ShowMode, StartMode
from aiogram_dialog.widgets.input import MessageInput, ManagedTextInput
from service.user_data import UserData
from ..handlers import start
from tgbot.logic import Scenario
from io import BytesIO
from aiogram.types import Message
import sys
from config.config import settings
from service.handling_data import InputDataHandler
from .logic import (MarketfileSuccess, MarketfileIncorrectExtencion, MarketfileToShowReport, 
                    MarketfileOverflow, MarketfileIncorrectRows, MarketfileToShowCapitalization)
from io import BytesIO
from .logic import BaseMarketfileHandler

async def handle_marketfile(message, dialog_manager: DialogManager):
    ...

    if res == "no_errors" and sd["comed_from"] == "choose_week":
        await UserData.set_file(message.chat.id, data=file)
        return MarketfileToShowReport(message)
    elif res == "no_errors" and sd["comed_from"] == "show_capitalization":
        await UserData.set_file(message.chat.id, data=file)
        return MarketfileToShowCapitalization(message)
    elif res == "no_errors":
        await UserData.set_file(message.chat.id, data=file)
        return MarketfileSuccess() 
    elif res == "cant_read":
        return MarketfileIncorrectExtencion()
    else:
        f = MarketfileIncorrectRows()
        await f.set_file(res, "Файл с подсвеченными ошибками.xlsx")
        return f

async def get_user_document(message: Document, widget: MessageInput, dialog_manager: DialogManager):
    await Scenario.clean_messages(dialog_manager, message.message_id)
    state = await handle_marketfile(message, dialog_manager)
    await state.set_file()
    await state.clean_old(dialog_manager)
    await state.to_scene(dialog_manager)
    await state.send_file(message, dialog_manager)
    await Scenario.fix_moving(message.chat.id, state.state)

async def to_upload_file(
                        message: Message,
                        dialog_manager: DialogManager,
                        state,
                        file: BytesIO,
                        filename: str,
                        clean_input: bool = False,
                        ):
        h = BaseMarketfileHandler()
        await h.set_state(state)
        if clean_input: await h.clean_old(dialog_manager)
        await h.set_file(file, filename)
        await h.to_scene(dialog_manager)
        await h.send_file(message, dialog_manager)