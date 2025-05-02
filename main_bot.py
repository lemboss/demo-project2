import logging
import asyncio
from config.config import settings
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs
from config.aiogram_storage import storage
from config.sentry_settings import init_sentry

from tgbot.dialogs.handlers import start_router
from tgbot.dialogs.menu.dialogs import menu_dialog
from tgbot.dialogs.show_report.dialogs import show_report_dialog
from tgbot.dialogs.set_token.dialogs import set_api_token_dialog
from tgbot.dialogs.get_reports.dialogs import get_reports_dialog
from tgbot.dialogs.update_data.dialogs import update_data_menu_dialog
from tgbot.dialogs.set_marketfile.dialogs import set_marketfile_dialog
from tgbot.dialogs.set_expences.dialogs import set_expences_dialog
from tgbot.dialogs.show_capitalization.dialogs import show_capitalization_dialog
from tgbot.dialogs.payments.dialogs import payments_dialog
from tgbot.dialogs.preview.dialogs import preview_dialog

from tgbot.middlewares.subscription_middleware import SubscriptionMiddleware
from tgbot.middlewares.addition_new_user_middleware import AddNewUserMiddleware

from service.async_requests import AsyncRequests
from service.security import PassEncryptor
from utils.processes_executor import executor as _
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from routes.payment.router import router as payment_router

bot = Bot(token=settings.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=storage)

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await AsyncRequests.initialize_session()
    await PassEncryptor.initialize()
    init_sentry()
    start_router.message.middleware(AddNewUserMiddleware())
    
    show_capitalization_dialog.callback_query.middleware(SubscriptionMiddleware())
    show_report_dialog.callback_query.middleware(SubscriptionMiddleware())
    get_reports_dialog.callback_query.middleware(SubscriptionMiddleware())
    dp.include_router(start_router)
    dp.include_router(set_api_token_dialog)
    dp.include_router(get_reports_dialog)
    dp.include_router(update_data_menu_dialog)
    dp.include_router(menu_dialog)
    dp.include_router(set_marketfile_dialog)
    dp.include_router(show_report_dialog)
    dp.include_router(set_expences_dialog)
    dp.include_router(show_capitalization_dialog)
    dp.include_router(payments_dialog)
    dp.include_router(preview_dialog)
    app.state.bg = setup_dialogs(dp)
    app.state.bot = bot
    webhook_url = settings.tg_bot.webhook_url 

    await bot.set_webhook(
        url=webhook_url,
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True
    )
    logging.info(f"Webhook set to {webhook_url}")
    yield
    await bot.delete_webhook()
    await AsyncRequests.close_session()

app = FastAPI(lifespan=lifespan)
app.include_router(payment_router)

@app.post("/webhook")
async def webhook(request: Request) -> None:
    logging.info("Received webhook request")
    update = await request.json()
    asyncio.create_task(dp.feed_raw_update(bot, update))
    logging.info("Update processed")