from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment
from aiogram.enums.content_type import ContentType
from ...media.path import path
from datetime import datetime
from copy import copy

async def get_wait(dialog_manager: DialogManager, **kwargs):
    sd = dialog_manager.start_data
    image = MediaAttachment(
        path=path.image.wait,
        type=ContentType.ANIMATION
    )
    return {'image': image}


async def get_simple_report(dialog_manager: DialogManager, **kwargs):
    sd = dialog_manager.start_data
    image = MediaAttachment(
        path=path.image.temp_report.format_map({"chat_id": sd["chat_id"], "timestamp": sd["ts"]}),
        type=ContentType.PHOTO
    )
    return {
        'image': image, 
        "variable_expence": sd["simple_report"]["variable_expence"],
        "show_instruction": sd["show_instruction"],
        "show_calculation_formula": sd["show_calculation_formula"]
    }

async def get_supplier_report(dialog_manager: DialogManager, **kwargs):
    sd = dialog_manager.start_data
    data = copy(sd["supllier_report"])
    image = MediaAttachment(
        path=path.image.temp_w_suppliers.format_map({"chat_id": sd["chat_id"], "timestamp": sd["ts"]}),
        type=ContentType.PHOTO
    )
    data["image"] = image

    return data

async def get_wo_supplier_report(dialog_manager: DialogManager, **kwargs):
    sd = dialog_manager.start_data
    data = copy(sd["supllier_report"])
    image = MediaAttachment(
        path=path.image.temp_wo_suppliers.format_map({"chat_id": sd["chat_id"], "timestamp": sd["ts"]}),
        type=ContentType.PHOTO
    )
    data["image"] = image

    return data

async def getter_wait_download(dialog_manager: DialogManager, **_):
    image = MediaAttachment(
        path=path.image.wait_data_wb,
        type=ContentType.PHOTO
    )
    
    return {'image': image}

SELECTED_DAYS_KEY = "selected_dates"

async def get_weeks(dialog_manager: DialogManager, **kwargs):
    sd = dialog_manager.start_data
    weeks = sd["date"]["weeks"]
    last_month = [weeks[-2]]
    weeks = weeks[:4]
    image = MediaAttachment(
        path=path.image.choose_week,
        type=ContentType.PHOTO
    )
    return {'weeks': weeks, 'last_month': last_month, "image": image}
    
    
async def selection_getter(dialog_manager, **_):
    sd = dialog_manager.start_data
    selected = dialog_manager.dialog_data.get(SELECTED_DAYS_KEY, [])
    selected = list(map(lambda d: datetime.strptime(d, "%Y-%m-%d").strftime("%d.%m.%Y"),selected))
    image = MediaAttachment(
        path=path.image.choose_week,
        type=ContentType.PHOTO
    )
    return {
        "image": image,
        "can_get_report": True if len(selected) == 2 else False,
        "start_date": selected[0] if len(selected) >= 1 else "",
        "end_date": selected[1] if len(selected) == 2 else "",
        "custom_interval": [sd["date"]["weeks"][-1]],
        "max_selectable_date": sd["date"]["weeks"][0][-1]
    }