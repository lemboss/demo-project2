from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.text import Const, Format, ScrollingText
from aiogram_dialog.widgets.kbd import Button, NumberedPager, Row
from .states import SetMarketfileSG
from aiogram_dialog.widgets.media import DynamicMedia
from .getters import (getter_image_upload_file, get_incorrect_rows, 
                      getter_success_marketfile)
from .handlers import get_user_document
from ..lexicon import LEXICON_SEND_USER_DATA_TEXT, LEXICON_START_TEXT
from ..lexicon import lexicon
from ..handlers import to_menu, get_back
from .on_click import to_update_data, to_get_reports, to_set_expences, to_choose_weeks

from aiogram_dialog.widgets.input import MessageInput

set_marketfile_dialog = Dialog(
    Window(
        DynamicMedia("image"),
        MessageInput(
            func=get_user_document,
            content_types=ContentType.ANY,
        ),
        Button(
            Const("Назад"),
            id="to_update_data",
            on_click=to_update_data
        ),
        getter=getter_image_upload_file,
        state=SetMarketfileSG.file,
    ),
    Window(
        Const("Для этого периода в файле с закупками не хватает артикулов. Заполните файл и отправьте его"),
        DynamicMedia("image"),
        MessageInput(
            func=get_user_document,
            content_types=ContentType.ANY,
        ),
        Button(
            Const("Назад"),
            id="to_choose_weeks",
            on_click=to_choose_weeks
        ),
        getter=getter_image_upload_file,
        state=SetMarketfileSG.missed_articles,
    ),
    Window(
        Const("Файл слишком большой. Удалите из него лишнюю информацию!"),
        DynamicMedia("image"),
        MessageInput(
            func=get_user_document,
            content_types=ContentType.ANY,
        ),
        Button(
            Const("Назад"),
            id="to_update_data",
            on_click=to_update_data
        ),
        getter=getter_image_upload_file,
        state=SetMarketfileSG.overflow_file,
    ),
    Window(
        Const(text="Некорректный файл! Загрузите файл формата .xls или .xlsx"),
        DynamicMedia("image"),
        MessageInput(
            func=get_user_document,
            content_types=ContentType.ANY,
        ),
        Button(
            Const("Назад"),
            id="to_update_data",
            on_click=to_update_data
        ),
        getter=getter_image_upload_file,
        state=SetMarketfileSG.incorrect_file_extencion,
    ),
    Window(
        Const("Исправьте файл и загрузите его заново"),
        DynamicMedia("image"),
        Button(
            Const("Назад"),
            id="to_update_data",
            on_click=to_update_data
        ),
        MessageInput(
            func=get_user_document,
            content_types=ContentType.ANY,
        ),
        getter=get_incorrect_rows,
        state=SetMarketfileSG.incorrect_file_rows,
    ),
    Window(
        DynamicMedia("image"),
        Button(
            Const("Обновить расходы"),
            id="to_set_expences",
            on_click=to_set_expences
        ),
        Button(
            Const("Получить отчет"),
            id="to_get_reports",
            on_click=to_get_reports
        ),
        Button(
            Const("Назад"),
            id="to_update_data",
            on_click=to_update_data
        ),
        getter=getter_success_marketfile,
        state=SetMarketfileSG.success,
    ),
)
