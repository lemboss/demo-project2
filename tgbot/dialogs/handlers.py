from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, ChatMemberUpdated, CallbackQuery
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, MEMBER, KICKED
from .menu.states import MainMenuSG
from tgbot.logic import Scenario
from service.user_data import UserData
from ..logic import Scenario

start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager):
    data = await Scenario.get_fields(message.chat.id)
    state = MainMenuSG.menu
    await Scenario.fix_moving(message.chat.id, state)
    await dialog_manager.start(state=state, 
                               mode=StartMode.RESET_STACK, 
                               show_mode=ShowMode.DELETE_AND_SEND,
                               data=data)
    
@start_router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blocking_bot(event: ChatMemberUpdated, dialog_manager: DialogManager):
    await UserData.update_user(chat_id=event.from_user.id, is_user=False)

@start_router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER))
async def process_user_unblocking_bot(event: ChatMemberUpdated, dialog_manager: DialogManager):
    await UserData.update_user(chat_id=event.from_user.id, is_user=True)

async def switch_inctruction(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    sd = dialog_manager.start_data
    sd["show_instruction"] = not sd["show_instruction"]   
    if sd["show_calculation_formula"]:
       sd["show_calculation_formula"] = False 
    
async def switch_calculation_formula(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    sd = dialog_manager.start_data
    sd["show_calculation_formula"] = not sd["show_calculation_formula"]    
    if sd["show_instruction"]:
        sd["show_instruction"] = False
    
async def to_state(message: Message, dialog_manager: DialogManager, state, show_instruction = False):
    sd = dialog_manager.start_data
    await Scenario.fix_moving(message.chat.id, state)
    await dialog_manager.start(state, data=dialog_manager.start_data, mode=StartMode.RESET_STACK, show_mode=ShowMode.EDIT)
    sd["show_instruction"] = show_instruction

async def delete_input_message(bot, chat_id, message_id):
    await bot.delete_message(chat_id=chat_id, message_id=message_id)    

async def clean_messages(dialog_manager: DialogManager):
    sd = dialog_manager.start_data
    msgs_id = sd["msgs_to_delete"]
    for msg_id in msgs_id:
        await delete_input_message(dialog_manager.middleware_data["bot"], sd["chat_id"], msg_id)
    sd["msgs_to_delete"].clear()
    
async def to_menu(message, widget: Button, dialog_manager: DialogManager):
    await clean_messages(dialog_manager)
    message = message if isinstance(message, Message) else message.message
    await start(message, dialog_manager)
    await Scenario.fix_moving(message.chat.id, MainMenuSG.menu)
    
async def get_back(message, widget, dialog_manager: DialogManager):
    await dialog_manager.done(show_mode=ShowMode.EDIT)
    