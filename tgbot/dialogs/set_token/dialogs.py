from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.text import Const, Format, ScrollingText
from aiogram_dialog.widgets.kbd import Button, NumberedPager, Row
from .states import SetTokenSG
from aiogram_dialog.widgets.media import DynamicMedia
from .getters import getter_step1, getter_step2, getter_step3, getter_step4, getter_set_token, getter_success_token
from .on_click import to_step1, to_step2, to_step3, to_step4, to_update_data_menu, to_set_token, to_set_marketfile
from .handlers import setting_token

set_api_token_dialog = Dialog(
    Window(
        Const("Токен некорректен, повторите ввод!", when="incorrect"),
        DynamicMedia("image"),
        Const(""),
        Button(
            Const("Назад"),
            id="to_update_data_menu",
            on_click=to_update_data_menu
        ),
        TextInput(
            id='get_api_token',
            on_success=setting_token
        ),
        state=SetTokenSG.set_token,
        getter=getter_set_token
    ),
    Window(
        Const("<i>*закупочная цена –  это цена товара, по которой селлер приобретает его у поставщика (себестоимость товара для селлера)</i>"),
        DynamicMedia("image"),
        Button(
            Const("Установить файл с закупками"),
            id="to_set_marketfile",
            on_click=to_set_marketfile
        ),
        Button(
            Const("Назад"),
            id="to_update_data_menu",
            on_click=to_update_data_menu
        ),
        state=SetTokenSG.success,
        getter=getter_success_token
    ),
    Window(
        Const("Зайдите <b>в настройки</b> личного кабинета селлера"),
        DynamicMedia("image"),
        Button(
            Const("Далее ->"),
            id="to_step2",
            on_click=to_step2
        ),
        Button(
            Const("<- Назад"),
            id="to_update_data_menu",
            on_click=to_update_data_menu
        ),
        state=SetTokenSG.step1,
        getter=getter_step1
    ),
    Window(
        Const("Выберите вкладку «<b>Доступ к API</b>»"),
        Const("Кликните «<b>Создать новый токен</b>»"),
        DynamicMedia("image"),
        Button(
            Const("Далее ->"),
            id="to_step3",
            on_click=to_step3
        ),
        Button(
            Const("<- Назад"),
            id="to_step1",
            on_click=to_step1
        ),
        state=SetTokenSG.step2,
        getter=getter_step2
    ),
    Window(
        Const("Введите название для токета"),
        Const("Поставьте галочку «Только на чтение» "),
        Const("Укажите методы API «Маркетплейс», «Статистика», «Аналитика»"),
        Const("Кликните «Создать токен»"),
        DynamicMedia("image"),
        Button(
            Const("Далее ->"),
            id="to_step4",
            on_click=to_step4
        ),
        Button(
            Const("<- Назад"),
            id="to_step2",
            on_click=to_step2
        ),
        state=SetTokenSG.step3,
        getter=getter_step3
    ),
    Window(
        Const("Токен создан. Кликните «Скопировать» и переходите к установке токена"),
        Const("<i>Внимание! Скопировать токен можно лишь раз, далее он будет недоступен. Токен действует 180 дней, далее требуется пересоздать.</i>"),
        DynamicMedia("image"),
        Button(
            Const("Перейти к установке токена"),
            id="to_set_token",
            on_click=to_set_token
        ), 
        Button(
            Const("Назад"),
            id="to_step3",
            on_click=to_step3
        ),   
        state=SetTokenSG.step4,
        getter=getter_step4
    ),
)