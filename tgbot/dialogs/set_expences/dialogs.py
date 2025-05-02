from aiogram import F
from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.text import Const, Format, ScrollingText
from aiogram_dialog.widgets.kbd import Button, NumberedPager, Row
from .states import SetExpencesSG
from aiogram_dialog.widgets.media import DynamicMedia
from .handlers import (correct_stable_expence, error_stable_expence, correct_variable_expence, 
                       error_variable_expence, is_digit, error_pre_report_expence, correct_pre_report_expence)
from .on_click import to_set_stable, to_set_variable, to_update_data, to_update_expences_menu, to_standart_report
from .getters import getter_stable_expence, getter_expences_menu, getter_variable_expence, getter_pre_report_expence
from ..handlers import switch_inctruction
from aiogram_dialog.widgets.input import MessageInput

set_expences_dialog = Dialog(
    Window(
        Const("<b>Постоянные расходы</b> – это расходы селлера, не связанные с объёмом продаж. От месяца к месяцу они будут оставаться неизменными. К ним относятся: зарплата сотрудников, аренда помещения, подписки MPstats/маяк и прочее.", when="show_instruction"),
        Const("<b>Переменные расходы</b> – это расходы селлера, которые зависят от объёма продаж. Чем больше заказов, тем выше эти расходы. К ним относятся: покупка курьер-пакетов, коробок, логисты и прочее.\n", when="show_instruction"),
        Const("<i>ВАЖНО! После введения данных селлером, бот автоматически распределяет все расходы равномерно «по всему календарному месяцу».</i>\n", when="show_instruction"),
        Const("<i>Введенные данные можно корректировать и дополнять в реальном времени.</i>\n", when="show_instruction"),
        Const("<i>Пример: Ваши ежемесячные расходы в месяц составляют 30 000 руб. При выборе отчетного периода в 30 дней - бот вычтет эти 30 000 руб. При выборе отчетного периода в 2 дня - бот вычтет 2 000 из оборотных средств этого периода.</i>", when="show_instruction"),
        DynamicMedia("image"),
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
            Const("Обновить постоянные расходы"),
            id="to_set_stable_expence",
            on_click=to_set_stable
        ),
        Button(
            Const("Обновить переменные расходы"),
            id="to_set_variable_expence",
            on_click=to_set_variable
        ),
        Button(
            Const("Назад"),
            id="to_update_data",
            on_click=to_update_data,
        ),
        state=SetExpencesSG.menu,
        getter=getter_expences_menu
    ),
    Window(
        Const("Некорректное число.", when="incorrect"),
        Format("Постоянные расходы: {stable_expence} р. Если хотите обновить, то отправьте новое значение."),
        DynamicMedia("image"),
        Button(
            Const("Назад"),
            id="to_update_expences_menu",
            on_click=to_update_expences_menu
        ),
        TextInput(
            id='get_stable_expence',
            type_factory=is_digit,
            on_success=correct_stable_expence,
            on_error=error_stable_expence,
        ),
        state=SetExpencesSG.set_stable,
        getter=getter_stable_expence
    ),
    Window(
        Const("Некорректное число.", when="incorrect"),
        Format("Переменные расходы: {variable_expence} р. Если хотите обновить, то отправьте новое значение."),
        DynamicMedia("image"),
        Button(
            Const("Назад"),
            id="to_update_expences_menu",
            on_click=to_update_expences_menu
        ),
        TextInput(
            id='get_variable_expence',
            type_factory=is_digit,
            on_success=correct_variable_expence,
            on_error=error_variable_expence,
        ),
        state=SetExpencesSG.set_variable,
        getter=getter_variable_expence
    ),
    Window(
        Const("Некорректное число.", when="incorrect"),
        DynamicMedia("image"),
        Button(
            Const("Посмотреть отчет"),
            id="to_standart_report",
            on_click=to_standart_report
        ),
        TextInput(
            id='get_pre_report_expence',
            type_factory=is_digit,
            on_success=correct_pre_report_expence,
            on_error=error_pre_report_expence,
        ),
        state=SetExpencesSG.pre_report,
        getter=getter_pre_report_expence
    ),
)
