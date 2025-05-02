from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment
from aiogram.enums.content_type import ContentType
from ...media.path import path
from service.user_data import UserData

async def get_image_select_next(dialog_manager: DialogManager, **kwargs):
    image = MediaAttachment(
        path=path.image.select_next,
        type=ContentType.PHOTO
    )
    return {"image": image}

async def getter_image_upload_file(dialog_manager: DialogManager, **kwargs):
    image = MediaAttachment(
        path=path.image.example_file,
        type=ContentType.PHOTO
    )
    data = {"image": image}
    return data

async def getter_success_marketfile(dialog_manager: DialogManager, **kwargs):
    image = MediaAttachment(
        path=path.image.success_marketfile,
        type=ContentType.PHOTO
    )
    data = {"image": image}
    return data


async def get_incorrect_rows(dialog_manager: DialogManager, **kwargs):
    image = MediaAttachment(
        path=path.image.example_file,
        type=ContentType.PHOTO
    )
    return {"image": image}
    
async def get_stable_expence(dialog_manager: DialogManager, **kwargs):
    sd = dialog_manager.start_data
    # image = MediaAttachment(
    #     path=path.image.temp_stable_expence.format_map({"chat_id": sd["chat_id"], "timestamp": sd["ts"]}),
    #     type=ContentType.PHOTO
    # )
    
    return {
        'incorrect': sd["incorrect"],
        "stable_expence_setted": sd["stable_expence_setted"], 
        "input_stable_expence": await UserData.get_stable_expence(sd["chat_id"])
    }

async def get_correctable_user_data(dialog_manager: DialogManager, **_):
    sd = dialog_manager.start_data
    image = MediaAttachment(
        path=path.image.set_token,
        type=ContentType.PHOTO
    )
    return {'incorrect': sd["incorrect"], "image": image}

async def get_variable_expence(dialog_manager: DialogManager, **_):
    sd = dialog_manager.start_data
    # image = MediaAttachment(
    #     path=path.image.set_token,
    #     type=ContentType.PHOTO
    # )
    return {'variable_expence': sd["variable_expence"]}