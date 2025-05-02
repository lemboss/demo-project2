import sentry_sdk
from sentry_sdk.integrations.asyncio import AsyncioIntegration
from .config import settings

def init_sentry():
    sentry_sdk.init(
        dsn=settings.sentry_dsn,
        send_default_pii=True,
        integrations=[
            AsyncioIntegration(),
        ],
    )