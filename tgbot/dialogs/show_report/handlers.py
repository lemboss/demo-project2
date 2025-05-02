from datetime import datetime, date
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Select
from config.config import settings
from .logic import report_logic
from service.dates import set_custom_date

async def report_handler(callback: CallbackQuery, widget: Select, dialog_manager: DialogManager, id: str):
    sd = dialog_manager.start_data
    sd["choosen_week_id"] = id
    await report_logic(callback.message, dialog_manager)

async def handle_calendar_click(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, selected_date: date):
    sd = dialog_manager.start_data
    selected = dialog_manager.dialog_data.setdefault("selected_dates", [])
    serial_date = selected_date.isoformat()
    if serial_date in selected:
        selected.remove(serial_date)
    elif len(selected) >= 2:
        selected.pop(0)
        selected.append(serial_date)
    else:
        selected.append(serial_date)
    selected.sort()
    if len(selected) == 2:
        set_custom_date(sd["date"], selected[0], selected[1])
        
    