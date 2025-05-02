from aiogram import F
from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.text import Const, Format, ScrollingText
from aiogram_dialog.widgets.kbd import Button, NumberedPager, Row
from ..handlers import switch_inctruction
from .states import UpdateDataSG
from .getters import getter_menu
from aiogram_dialog.widgets.media import DynamicMedia
from .on_click import to_main_menu, to_insctruction, to_set_token, to_set_marketfile, to_set_expences

update_data_menu_dialog = Dialog(
    Window(
        DynamicMedia("image"),
        Const("<b>API токен</b> (Через него бот сможет получать данные об отчетах и обрабатывать их для Вас)", when="show_instruction"),
        Const("<b>Закупочный файл</b> (Шаблон внутри. По нему бот определит где прибыль, а где потраченные средства на закуп реализованных товаров)\n", when="show_instruction"),
        Const("При необходимости воспользуйтесь инструкцией по созданию API токена", when="show_instruction"),    
        Button(
            Const("Показать примечания"),
            id="show_instruction",
            on_click=switch_inctruction,
            when=~F["show_instruction"]
        ),
        Button(
            Const("Скрыть примечания"),
            id="hide_instruction",
            on_click=switch_inctruction,
            when=F["show_instruction"]
        ),
        Button(
            Const("Установить API ключ"),
            id="to_set_api_token",
            on_click=to_set_token
        ),
        Button(
            Const("Инструкция для установки API ключа"),
            id="to_instruction_for_setting_token",
            on_click=to_insctruction
        ),
        Button(
            Const("Установить файл с закупками"),
            id="to_set_marketfile",
            on_click=to_set_marketfile,
        ),
        Button(
            Const("Обновить расходы"),
            id="to_set_expences",
            on_click=to_set_expences
        ),
        Button(
            Const("Назад"),
            id="to_main_menu",
            on_click=to_main_menu
        ),
        state=UpdateDataSG.menu,
        getter=getter_menu
    )
)