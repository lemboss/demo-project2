from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment
from aiogram.enums.content_type import ContentType
from ...media.path import path
from service.user_data import UserData
from config.config import settings

async def get_data(dialog_manager: DialogManager, **kwargs):
    chat_id = dialog_manager.start_data["chat_id"]
    token = await UserData.get_key(chat_id)
    file = await UserData.get_file(chat_id)
    
    if token and file:
        img_path = path.image.main_after
    else:
        img_path = path.image.main
    
    image = MediaAttachment(
        path=img_path,
        type=ContentType.PHOTO
    )
    
    return {
        "image": image
    }
    
    