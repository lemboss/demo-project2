from aiogram.types import Message, Document
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput, ManagedTextInput
from service.user_data import UserData
from ..handlers import start
from tgbot.logic import Scenario
from ..get_reports.states import GetReportsSG
from .states import SetExpencesSG
from aiogram_dialog import DialogManager, StartMode, ShowMode
from .logic import create_pre_report_pic


def is_digit(text: str) -> str:
    if all(ch.isdigit() for ch in text.strip()):
        return text
    raise ValueError

async def correct_stable_expence(
        message: Message, 
        widget: ManagedTextInput, 
        dialog_manager: DialogManager, 
        value: str) -> None:
    sd = dialog_manager.start_data
    sd["incorrect"] = False
    state = GetReportsSG.menu
    await UserData.set_stable_expence(message.chat.id, int(value))
    await Scenario.fix_moving(message.chat.id, state)
    await dialog_manager.start(state, data=sd, mode=StartMode.RESET_STACK, show_mode=ShowMode.EDIT)
    await Scenario.clean_messages(dialog_manager, message.message_id)
    
async def error_stable_expence(
        message: Message, 
        widget: ManagedTextInput, 
        dialog_manager: DialogManager, 
        error: ValueError):
    sd = dialog_manager.start_data
    sd["incorrect"] = True
    state = SetExpencesSG.set_stable
    await Scenario.fix_moving(message.chat.id, state)
    await Scenario.clean_messages(dialog_manager, message.message_id)
    
async def correct_variable_expence(
        message: Message, 
        widget: ManagedTextInput, 
        dialog_manager: DialogManager, 
        value: str) -> None:
    sd = dialog_manager.start_data
    sd["msgs_to_delete"].append(message.message_id)
    sd["incorrect"] = False
    state = GetReportsSG.menu
    await UserData.set_variable_expence(message.chat.id, int(value))
    await Scenario.fix_moving(message.chat.id, state)
    await dialog_manager.start(state, data=sd, mode=StartMode.RESET_STACK, show_mode=ShowMode.EDIT)
    
async def error_variable_expence(
        message: Message, 
        widget: ManagedTextInput, 
        dialog_manager: DialogManager, 
        error: ValueError):
    sd = dialog_manager.start_data
    sd["incorrect"] = True
    sd["msgs_to_delete"].append(message.message_id)
    state = SetExpencesSG.set_variable
    await Scenario.fix_moving(message.chat.id, state)
    
async def correct_pre_report_expence(
        message: Message, 
        widget: ManagedTextInput, 
        dialog_manager: DialogManager, 
        value: str) -> None:
    sd = dialog_manager.start_data
    sd["msgs_to_delete"].append(message.message_id)
    sd["incorrect"] = False
    await UserData.set_variable_expence(message.chat.id, int(value))
    await create_pre_report_pic(dialog_manager, True)
    
async def error_pre_report_expence(
        message: Message, 
        widget: ManagedTextInput, 
        dialog_manager: DialogManager, 
        error: ValueError):
    sd = dialog_manager.start_data
    sd["incorrect"] = True
    sd["msgs_to_delete"].append(message.message_id)
    await create_pre_report_pic(dialog_manager, True)