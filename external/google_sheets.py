import logging
import asyncio
from datetime import datetime
from config.config import settings
import gspread_asyncio
from google.oauth2.service_account import Credentials

logger = logging.getLogger(__name__)
                
class SpreadSheets:
    client = gspread_asyncio.AsyncioGspreadClientManager(lambda: Credentials.from_service_account_file(
        settings.gs.cred_file_path, 
        scopes=[
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
    ))
    _lock = asyncio.Lock()
    _is_authorized = False 

    @classmethod
    async def authorize(cls):
        if cls._is_authorized == False:
            a = await cls.client.authorize()
            cls.ss = await a.open_by_key(settings.gs.ss_id)
            logger.info("Авторизация с Google прошла успешно")
            cls._is_authorized = True
            cls.worksheet = await cls.ss.worksheet("Лист1")
                
    async def get_values(self):
        rows = await SpreadSheets.worksheet.get_all_values()
        rows = rows[1:]
        for r in rows:
            r[0] = datetime.strptime(r[0], '%d.%m.%Y')
        rows.sort(key=lambda x: x[0])
        return rows

    async def write_values(self, data):
        await SpreadSheets.worksheet.append_rows(data)