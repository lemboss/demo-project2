from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.kbd import Button, Url
from .states import MainMenuSG
from .getters import get_data
from .on_click import to_get_reports_menu, to_update_data_menu, to_payments_menu, to_preview_video

menu_dialog = Dialog(
    Window(
        Const("ВАЖНО❗️Селлер, для бесперебойной работы CRM, не забудь своевременно обновлять закупочный файл с новыми товарами.", when=""),
        Const("При возникновении сложностей кликните «Обратиться в чат поддержки»."),
        DynamicMedia("image"),
        Button(
            Const("Видео-обзор возможностей"),
            id="to_preview_video",
            on_click=to_preview_video,
        ),
        Button(
            Const("Обновить данные"),
            id="to_update_data_menu",
            on_click=to_update_data_menu,
        ),
        Button(
            Const("Получить отчеты"),
            id="to_get_reports_menu",
            on_click=to_get_reports_menu,
        ),
        Button(
            Const("Управление подпиской"),
            id="to_payments_menu",
            on_click=to_payments_menu,
        ),
        state=MainMenuSG.menu,
        getter=get_data
    ),
)