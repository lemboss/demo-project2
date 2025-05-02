import logging
import asyncio
from config.config import settings
from external.google_sheets import SpreadSheets
from analytics.analytics_handler import AnalyticsHandler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

logger = logging.getLogger(__name__)

async def main():
    await SpreadSheets.authorize()
    scheduler = AsyncIOScheduler(timezone=settings.date.tz)
    scheduler.add_job(AnalyticsHandler.upload_spreadsheets, CronTrigger(hour=4, minute=0))
    scheduler.start()
    await AnalyticsHandler.upload_spreadsheets()
    logger.info("Аналитика запущена")
    while True:
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(main())