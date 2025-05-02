from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format, ScrollingText
from aiogram_dialog.widgets.kbd import Button, NumberedPager, Select
from .states import ShowCapitalizatonSG
from .getters import getter_remains_report, getter_wait_download
from .on_click import to_get_reports_menu, to_main_menu
from aiogram_dialog.widgets.media import DynamicMedia

show_capitalization_dialog = Dialog(
    Window(
        DynamicMedia("image"),
        Button(
            Const("Вернуться в главное меню"),
            id="to_menu",
            on_click=to_main_menu
        ),
        state=ShowCapitalizatonSG.report,
        getter=getter_remains_report
    ),
    Window(
        DynamicMedia("image"),
        Const("Получение данных из Wildberries..."),
        state=ShowCapitalizatonSG.download,
        getter=getter_wait_download
    )
)