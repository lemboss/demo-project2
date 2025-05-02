from aiogram import F
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format, ScrollingText
from aiogram_dialog.widgets.kbd import Button, NumberedPager, Select
from .states import ShowReportSG
from .getters import (get_simple_report, get_supplier_report, get_wo_supplier_report, get_wait, getter_wait_download, 
                        selection_getter, get_weeks)
from ..lexicon import LEXICON_WAIT_REPORT_TEXT
from ..handlers import switch_inctruction, switch_calculation_formula
from .on_click import to_menu, to_deep_report, to_simple_report, to_missed_suplier_report, to_update_data_menu, to_get_reports_menu
from aiogram_dialog.widgets.media import DynamicMedia
from .handlers import handle_calendar_click, report_handler
from .custom import CustomCalendar
from datetime import datetime, date
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Select
from config.config import settings
from .logic import report_logic
from service.dates import set_custom_date

show_report_dialog = Dialog(
    Window(
        Format("Данные доступны до {max_selectable_date}"),
        Format("Отчетный период: {start_date} - {end_date}"),
        DynamicMedia("image"),
        CustomCalendar(
            id="select_custom_dates_to_report",
            on_click=handle_calendar_click
        ),
        Select(
            Format("Получить отчет {item[0]}{item1}"[:15]),
            id='select_custom_dates',
            item_id_getter=lambda x: x[0],
            items='custom_interval',
            on_click=report_handler,
            when='can_get_report'
        ),
        Button(
            Const("Назад"),
            id="back_menu",
            on_click=to_get_reports_menu
        ),
        getter=selection_getter,
        state=ShowReportSG.select_dates,
    ),
    Window(
        Const("<b>Сумма продаж</b> - продажи селлера, до вычета расходов ВБ, согласно ежедневным/еженедельным отчетам за выбранный период времени. <i>Именно её налоговая считает доходом.</i>", when="show_instruction"),
        Const("<b>Итого к оплате</b> - средства, выплаченные площадкой селлеру (с учетом процента ВБ, логистики, штрафов, займа).", when="show_instruction"),
        Const("<b>Общая сумма закупки</b> - сумма ДС из общей суммы к перечислению, которую селлер потратил на закупку реализованного товара.", when="show_instruction"),
        Const("<b>Налог</b> - сумма ДС, которую необходимо отложить на уплату налогов.", when="show_instruction"),
        Const("<b>Важно</b>❗️Учитывается налог на УСН 7% (6% на доход  +1% на доход свыше 300 тыс руб/мес).", when="show_instruction"),
        Const('<b>Важно</b>❗️Частая ошибка селлеров❗️ Налог накладывается не на поступившую сумму на расчетный счет, а на сумму  в графе  "Продажа" финансовых отчетов в личном кабинета селлера.', when="show_instruction"),
        Const("<b>Грязная прибыль</b> - прибыль селлера, без учета постоянных и переменных расходов.", when="show_instruction"),
        Const("<b>Чистая прибыль</b> - прибыль селлера, с учётом абсолютно всего.", when="show_instruction"),
        Const("<b>Рентабельность</b> - показатель эффективности вложенных средств.", when="show_instruction"),
        
        Const('<b>Налог</b> (УСН6%+1%)', when="show_calculation_formula"),
        Const('= (сумма продаж)*0,07\n', when="show_calculation_formula"),
        Const("<b>Грязная прибыль</b>", when="show_calculation_formula"),
        Const("= (итого к оплате) - (общая сумма закупки)\n", when="show_calculation_formula"),
        Const("<b>Чистая прибыль</b>", when="show_calculation_formula"),
        Const("= (итого к оплате) - (общая сумма закупки) - (налог) - (постоянные расходы) - (переменные расходы)\n", when="show_calculation_formula"),
        Const("<b>Рентабельность</b>", when="show_calculation_formula"),
        Const("= ((чистая прибыль) / (общая сумма закупки))*100%", when="show_calculation_formula"),
        DynamicMedia("image"),
        Button(
            Const("Посмотреть примечания"),
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
            Const("Показать формулы расчетов"),
            id="show_calculation_formula",
            on_click=switch_calculation_formula,
            when=~F["show_calculation_formula"]
        ),
        Button(
            Const("Скрыть формулы расчетов"),
            id="hide_calculation_formula",
            on_click=switch_calculation_formula,
            when=F["show_calculation_formula"]
        ),
        Button(
            Const("Расширенный отчет"),
            id="deep_report",
            on_click=to_deep_report
        ),
        Button(
            Const("Вернуться в главное меню"),
            id="to_menu",
            on_click=to_update_data_menu
        ),
        state=ShowReportSG.standart,
        getter=get_simple_report
    ),
    Window(
        DynamicMedia("image"),
        Format("Итого: {sum_sales}"),
        ScrollingText(
            text=Format("{supplier_text}"),
            id="report_scroll",
            page_size=1000,
        ),
        Format("Артикулов без поставщиков: {count_missed_suppliers}", when="count_missed_suppliers"),
        NumberedPager(
            scroll="report_scroll",
            when="show_scroll"
        ),
        Button(
            Const("Стандартный отчет"),
            id="to_simple",
            on_click=to_simple_report
        ),
        Button(
            Const("Артикулы без поставщиков"),
            id="to_missed_supplier",
            on_click=to_missed_suplier_report,
            when="article_missed_suppliers"
        ),
        state=ShowReportSG.deep,
        getter=get_supplier_report
    ),
    Window(
        DynamicMedia("image"),
        Button(
            Const("Стандартный отчет"),
            id="to_simple",
            on_click=to_simple_report
        ),
        Button(
            Const("Расширенный отчет"),
            id="to_deep",
            on_click=to_deep_report,
            when="article_missed_suppliers"
        ),
        state=ShowReportSG.missed_supplier,
        getter=get_wo_supplier_report
    ),
    Window(
        DynamicMedia("image"),
        Const("Получение данных из Wildberries..."),
        state=ShowReportSG.download,
        getter=getter_wait_download
    )
)