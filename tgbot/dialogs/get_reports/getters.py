from service.user_data import UserData
from aiogram_dialog.api.entities import MediaAttachment
from aiogram.enums.content_type import ContentType
from ...media.path import path

async def getter_status_token_file(dialog_manager, **_):
    sd = dialog_manager.start_data
    chat_id = dialog_manager.start_data["chat_id"]
    token = await UserData.get_key(chat_id)
    file = await UserData.get_file(chat_id)
    
    image = MediaAttachment(
        path=path.image.get_reports_menu,
        type=ContentType.PHOTO
    )
    
    return {
        "image": image,
        "token": True if token is not None else False,
        "file": True if file is not None else False,
        "show_buttons": token and file,
        "show_instruction": sd["show_instruction"]
    }