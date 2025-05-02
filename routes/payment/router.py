from fastapi import APIRouter, Request
from datetime import datetime
from typing import Literal
from fastapi.responses import RedirectResponse
from external.tbank import TBankCash
from database.models.payment.dao import PaymentDAO
from datetime import datetime, timedelta
from .schemas import SPaymentStatus
from .funcs import switch_dialog, stack_time
from tgbot.dialogs.payments.states import PaymentsSG
import logging
from config.config import settings
from tgbot.logic import Scenario
import asyncio
from tgbot.dialogs.payments.states import PaymentsSG

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix = "/payment",
    tags=["Подписка"]
)

@router.get("/create")
async def payment(chat_id: int, month: Literal["1", "3", "6", "12"], request: Request):
    match month:
        case "1":
            amount = 199
        case "3":
            amount = 499
        case "6":
            amount = 899
        case "12":
            amount = 1699
    sub = await PaymentDAO.find_last(chat_id == chat_id)
    id = sub.id + 1
    order_id = f"{id}-{chat_id}-{month}"
    responce = await TBankCash.create_payment(amount, order_id)
    if responce:
        ...
    else:
        ...

@router.post("/update_status")
async def success_payment(payment: SPaymentStatus, request: Request):
    order_id_splitted = payment.OrderId.split("-")
    chat_id = int(order_id_splitted[1])
    logger.info(f"Получен status {str(payment)}")
    ...
    return "OK"
        