from aiogram import F
from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.text import Const, Format, ScrollingText
from aiogram_dialog.widgets.kbd import Button, NumberedPager, Row
from aiogram_dialog.widgets.media import DynamicMedia
from ..handlers import switch_inctruction
from .states import GetReportsSG
from .getters import getter_status_token_file
from .on_click import to_main_menu, to_select_dates, to_set_token, to_set_marketfile, to_show_capitalization

get_reports_dialog = Dialog(
    Window(
        Const("• выбор периода для отчета предоставляет отчет по продажам, налогам, прибыли и рентабельности за выбранное количество дней", when=F["show_buttons"] & F["show_instruction"]),
        Const("• выбор отчета капитализации предоставляет данные об общем количестве денег, вложенных вами в закупку товара, которые уже были отгружены, но еще не выкуплены клиентами", when=F["show_buttons"] & F["show_instruction"]),
        Const("Для получения отчета необходимо установить API токен!", when=~F['token']),
        Const("Для получения отчета необходимо установить закупочный файл!", when=~F['file']),
        DynamicMedia("image"),
        Button(
            Const("Показать примечания"),
            id="show_instruction",
            on_click=switch_inctruction,
            when=~F["show_instruction"] & F["show_buttons"]
        ),
        Button(
            Const("Скрыть примечания"),
            id="hide_instruction",
            on_click=switch_inctruction,
            when=F["show_instruction"] & F["show_buttons"]
        ),
        Button(
            Const("Установить API токен"),
            id="to_set_token",
            on_click=to_set_token,
            when=~F["token"]
        ),
        Button(
            Const("Установить закупочный файл"),
            id="to_set_marketfile",
            on_click=to_set_marketfile,
            when=~F["file"]
        ),
        Button(
            Const("Выберите период для отчета"),
            id="to_calendar",
            on_click=to_select_dates,
            when="show_buttons"
        ),
        Button(
            Const("Капитализация товарных остатков на складах WB"),
            id="to_capitalization_report",
            on_click=to_show_capitalization,
            when="show_buttons"
        ),
        Button(
            Const("Назад"),
            id="to_main_menu",
            on_click=to_main_menu
        ),
        state=GetReportsSG.menu,
        getter=getter_status_token_file
    ),
)