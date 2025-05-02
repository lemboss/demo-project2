from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button
from ..handlers import switch_inctruction
from .states import PreviewSG
from aiogram_dialog.widgets.media import StaticMedia
from ...media.path import path
from .on_click import to_main_menu

preview_dialog = Dialog(
    Window(
        StaticMedia(
            path=path.video.preview,
            type=ContentType.VIDEO,
            media_params={"width": 1920, "height": 1148, "has_spoiler": True}
        ),
        Button(
            Const("Назад"),
            id="to_main_menu",
            on_click=to_main_menu
        ),
        state=PreviewSG.menu,
    )
)