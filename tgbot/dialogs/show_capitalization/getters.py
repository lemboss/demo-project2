from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment
from aiogram.enums.content_type import ContentType
from service.value_formatter import beautify_number
from ...media.path import path

async def getter_remains_report(dialog_manager: DialogManager, **_):
    sd = dialog_manager.start_data
    image = MediaAttachment(
        path=path.image.temp_capitaliaztion.format_map({"chat_id": sd["chat_id"], "timestamp": sd["ts"]}),
        type=ContentType.PHOTO
    )
    
    return {'image': image}
    
    
async def getter_wait_download(dialog_manager: DialogManager, **_):
    image = MediaAttachment(
        path=path.image.wait_data_wb,
        type=ContentType.PHOTO
    )
    
    return {
        'image': image,
    }
    