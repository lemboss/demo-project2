from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment
from aiogram.enums.content_type import ContentType
from ...media.path import path
from config.config import settings

async def getter_menu(dialog_manager: DialogManager, **kwargs):
    sd = dialog_manager.start_data
    image = MediaAttachment(
        path=path.image.update_data,
        type=ContentType.PHOTO
    )
    return {
        "image": image,
        "show_instruction": sd["show_instruction"]
    }
    
    