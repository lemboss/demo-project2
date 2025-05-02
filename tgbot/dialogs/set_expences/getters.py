from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment
from aiogram.enums.content_type import ContentType
from ...media.path import path
from service.user_data import UserData
    
async def getter_stable_expence(dialog_manager: DialogManager, **kwargs):
    sd = dialog_manager.start_data
    image = MediaAttachment(
        path=path.image.stable_expences,
        type=ContentType.PHOTO
    )
    return {
        'incorrect': sd["incorrect"],
        "stable_expence": await UserData.get_stable_expence(sd["chat_id"]),
        "image": image 
    }
    
async def getter_variable_expence(dialog_manager: DialogManager, **_):
    sd = dialog_manager.start_data
    image = MediaAttachment(
        path=path.image.variable_expences,
        type=ContentType.PHOTO
    )
    
    return {
        'incorrect': sd["incorrect"],
        "variable_expence": await UserData.get_variable_expence(sd["chat_id"]),
        "image": image
    }
    
async def getter_pre_report_expence(dialog_manager: DialogManager, **_):
    sd = dialog_manager.start_data
    image = MediaAttachment(
        path=path.image.temp_pre_report_expence.format_map({"chat_id": sd["chat_id"], "timestamp": sd["ts"]}),
        type=ContentType.PHOTO
    )
    return {
        'incorrect': sd["incorrect"],
        "image": image
    }
    
async def getter_expences_menu(dialog_manager: DialogManager, **_):
    sd = dialog_manager.start_data
    image = MediaAttachment(
        path=path.image.expences_menu,
        type=ContentType.PHOTO
    )
    return {
        'image': image,
        "show_instruction": sd["show_instruction"]
    }