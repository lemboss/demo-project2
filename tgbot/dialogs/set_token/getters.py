from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment
from aiogram.enums.content_type import ContentType
from ...media.path import path

async def getter_set_token(dialog_manager: DialogManager, **_):
    image = MediaAttachment(
        path=path.image.set_token,
        type=ContentType.PHOTO
    )
    return {'image': image, 'incorrect': dialog_manager.start_data["incorrect"]}
    
async def getter_step1(dialog_manager: DialogManager, **_):
    image = MediaAttachment(
        path=path.image.instruction_step1,
        type=ContentType.PHOTO
    )
    return {'image': image}

async def getter_success_token(dialog_manager: DialogManager, **_):
    image = MediaAttachment(
        path=path.image.success_token,
        type=ContentType.PHOTO
    )
    return {'image': image}

async def getter_step2(dialog_manager: DialogManager, **_):
    image = MediaAttachment(
        path=path.image.instruction_step2,
        type=ContentType.PHOTO
    )
    return {'image': image}

async def getter_step3(dialog_manager: DialogManager, **_):
    image = MediaAttachment(
        path=path.image.instruction_step3,
        type=ContentType.PHOTO
    )
    return {'image': image}

async def getter_step4(dialog_manager: DialogManager, **_):
    image = MediaAttachment(
        path=path.image.instruction_step4,
        type=ContentType.PHOTO
    )
    return {'image': image}