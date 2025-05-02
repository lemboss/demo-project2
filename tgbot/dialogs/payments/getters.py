from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment
from aiogram.enums.content_type import ContentType
from ...media.path import path
from service.user_data import UserData
from config.config import settings

async def getter_payment_menu(dialog_manager: DialogManager, **kwargs):
    url = settings.domain
    image = MediaAttachment(
        path=path.image.payment_manage,
        type=ContentType.PHOTO
    )
    return {
        'image': image,
        "url": url,
        "chat_id": dialog_manager.start_data["chat_id"]
    }
    
async def getter_payment_success(dialog_manager: DialogManager, **kwargs):
    image = MediaAttachment(
        path=path.image.payment_success,
        type=ContentType.PHOTO
    )
    return {
        'image': image,
    }

async def getter_payment_fail(dialog_manager: DialogManager, **kwargs):
    image = MediaAttachment(
        path=path.image.payment_fail,
        type=ContentType.PHOTO
    )
    return {
        'image': image,
    }