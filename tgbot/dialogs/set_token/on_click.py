import logging
from datetime import datetime
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import ShowMode
from .states import SetTokenSG
from ..set_marketfile.states import SetMarketfileSG
from ..update_data.states import UpdateDataSG
from service.user_data import UserData
from ..handlers import to_menu
from tgbot.logic import Scenario
from ..set_marketfile.handlers import to_upload_file

async def to_update_data_menu(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    state = UpdateDataSG.menu
    await Scenario.fix_moving(callback.message.chat.id, state)
    await dialog_manager.start(state, data=dialog_manager.start_data, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)

async def to_step1(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    state = SetTokenSG.step1
    await Scenario.fix_moving(callback.message.chat.id, state)
    await dialog_manager.start(state, data=dialog_manager.start_data, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)
    
async def to_step2(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    state = SetTokenSG.step2
    await Scenario.fix_moving(callback.message.chat.id, state)
    await dialog_manager.start(state, data=dialog_manager.start_data, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)
    
async def to_step3(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    state = SetTokenSG.step3
    await Scenario.fix_moving(callback.message.chat.id, state)
    await dialog_manager.start(state, data=dialog_manager.start_data, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)
    
async def to_step4(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    state = SetTokenSG.step4
    await Scenario.fix_moving(callback.message.chat.id, state)
    await dialog_manager.start(state, data=dialog_manager.start_data, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)
    
async def to_set_token(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    state = SetTokenSG.set_token
    await Scenario.fix_moving(callback.message.chat.id, state)
    dialog_manager.start_data['incorrect'] = False
    await dialog_manager.start(state, data=dialog_manager.start_data, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)
    
async def to_set_marketfile(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    state = SetMarketfileSG.file
    await Scenario.fix_moving(callback.message.chat.id, state)
    example_file = await UserData.get_example_file()
    await to_upload_file(callback.message, dialog_manager, state, example_file, filename="Шаблон таблицы.xlsx")