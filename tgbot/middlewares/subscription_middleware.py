from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from service.user_data import UserData
from datetime import datetime

from ..dialogs.payments.states import PaymentsSG


class SubscriptionMiddleware(BaseMiddleware):
    
    async def can_view(self, chat_id):
        a = await UserData.get_payment(chat_id)
        if not a: return False 
        now = datetime.now()
        if now > a.expiration_at:
            return False
        else:
            return True
    
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        chat_id = data["event_context"].chat.id
        can_view = await self.can_view(chat_id)
        if can_view:
            result = await handler(event, data)
            return result
        else:
            manager = data["dialog_manager"]
            sd = manager.start_data
            await data["dialog_manager"].start(PaymentsSG.expirated, data=sd)