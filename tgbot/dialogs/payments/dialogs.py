from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.kbd import Button, Url
from aiogram_dialog.widgets.input import TextInput

from .states import PaymentsSG
from .getters import getter_payment_menu, getter_payment_fail, getter_payment_success
from .on_click import to_main_menu, to_payments_menu

payments_dialog = Dialog(
    Window(
        DynamicMedia("image"),
        Url(
            Const("1 месяц подписки за 199 руб."),
            url=Format("{url}/payment/create?chat_id={chat_id}&month=1"),
            id="subscribe_1"
        ),
        Url(
            Const("3 месяца подписки за 499 руб."),
            url=Format("{url}/payment/create?chat_id={chat_id}&month=3"),
            id="subscribe_2"
        ),
        Url(
            Const("6 месяцев подписки за 899 руб."),
            url=Format("{url}/payment/create?chat_id={chat_id}&month=6"),
            id="subscribe_3"
        ),
        Url(
            Const("1 год подписки за 1699 руб."),
            url=Format("{url}/payment/create?chat_id={chat_id}&month=12"),
            id="subscribe_4"
        ),
        # Button(
        #     Const("Отмена подписки"),
        #     id="to_get_reports_menu",
        #     on_click=None,
        #     when=None # если подписан, показывать кнопку
        # ),
        Button(
            Const("Назад"),
            id="to_main_menu",
            on_click=to_main_menu
        ),
        state=PaymentsSG.menu,
        getter=getter_payment_menu
    ),
    Window(
        DynamicMedia("image"),
        Const("Оплата подписки не прошла. Попробуйте снова и возвращайтесь"),
        Button(
            Const("К управлению подпиской"),
            id="to_handle_payments",
            on_click=to_payments_menu,
        ),
        Button(
            Const("Главное меню"),
            id="to_main_menu",
            on_click=to_main_menu
        ),
        state=PaymentsSG.expirated,
        getter=getter_payment_fail
    ),
    Window(
        DynamicMedia("image"),
        Button(
            Const("Главное меню"),
            id="to_main_menu",
            on_click=to_main_menu
        ),
        state=PaymentsSG.success,
        getter=getter_payment_success
    ),
    Window(
        DynamicMedia("image"),
        Button(
            Const("К управлению подпиской"),
            id="to_handle_payments",
            on_click=to_payments_menu,
        ),
        state=PaymentsSG.fail,
        getter=getter_payment_fail
    ),
)