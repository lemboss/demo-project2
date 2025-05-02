from service.async_requests import AsyncRequests
import json
import asyncio
from config.config import settings
from service.user_data import UserData
import logging
import aiofiles 
from datetime import datetime
logger = logging.getLogger(__name__)

class WBDetalization: 
    URI_STATISTIC = "https://statistics-api.wildberries.ru"
    URI_REPORT_DETALIZATION = "/api/v5/supplier/reportDetailByPeriod"
    URI_PING = "/ping"
    
    def __init__(self, token: str):
        self.headers = {
            "Authorization": token
        }
    async def request_test_token(self) -> bool:
        url = WBDetalization.URI_STATISTIC + WBDetalization.URI_PING
        resp = json.loads(await AsyncRequests.get(url, headers=self.headers))

        if "Status" in resp:
            logger.info(f"+Уровень детализации валиден")
            return True
        logger.info(f"-Уровень детализации невалиден")
        return False
        
    async def handle_data(self, data: list):
        """
        sa_name
        ppvz_for_pay
        rrd_id
        """

        return list(map(lambda x: {
            "report_id": x["realizationreport_id"],
            "date_from": x["date_from"],
            "article": x["sa_name"].lower(), 
            "ppvz": x["ppvz_for_pay"] + x["additional_payment"], 
            "fines": x["delivery_rub"] + x["penalty"] + x["storage_fee"] + x["deduction"] + x["acceptance"],
            "rrd_id": x["rrd_id"],
            'doc_type_name': x["doc_type_name"],
            "supplier_oper_name": x["supplier_oper_name"],
            'report_type': x["report_type"],
            "retail_amount": x["retail_amount"]
        }, data))
        
    async def request_get_statistic(self, dateFrom, dateTo, rrd_id, limit):
        params = {
            "dateFrom": dateFrom,
            "dateTo": dateTo,
            "limit": limit,
            "rrdid": rrd_id
        }
        
        url = WBDetalization.URI_STATISTIC + WBDetalization.URI_REPORT_DETALIZATION
        resp = json.loads(await AsyncRequests.get(url, params=params, headers=self.headers))
        return resp
    
    async def get_report_detalization(self, dateFrom, dateTo, limit: int = 100_000):
        rrd_id = 0
        report = []
        rows = await self.request_get_statistic(dateFrom, dateTo, rrd_id, limit)
        rrd_id = rows[-1]['rrd_id'] if isinstance(rows, list) and rows else rrd_id
        if isinstance(rows, list):
            rows = await self.handle_data(rows) 
            report += rows
        while rows:
            try:
                rows = await self.request_get_statistic(dateFrom, dateTo, rrd_id, limit)
                rrd_id = rows[-1]['rrd_id'] if isinstance(rows, list) and rows else rrd_id
                if isinstance(rows, list):
                    rows = await self.handle_data(rows)
                    report += rows
            except:
                continue
        return report
    
    async def aio_get_report_detalization(self, dateFrom, dateTo, limit: int = 100_000):
        start = datetime.now()
        async with aiofiles.open("123.json", mode='w') as file: 
            rrd_id = 0
            rows = await self.request_get_statistic(dateFrom, dateTo, rrd_id, limit)
            rrd_id = rows[-1]['rrd_id'] if isinstance(rows, list) and rows else rrd_id
            if isinstance(rows, list) and len(rows) > 0:
                rows = await self.handle_data(rows) 
                await file.write(json.dumps(rows) + '\n')
            await asyncio.sleep(3)
            counter = 1
            while rows:
                try:
                    rows = await self.request_get_statistic(dateFrom, dateTo, rrd_id, limit)
                    rrd_id = rows[-1]['rrd_id'] if isinstance(rows, list) and rows else rrd_id
                    if isinstance(rows, list) and len(rows) > 0:
                        rows = await self.handle_data(rows)
                        await file.write(json.dumps(rows) + '\n')
                        counter += 1
                    await asyncio.sleep(3)
                except:
                    continue
        end = datetime.now() - start
        logger.info(f"Время скачивания отчета детализации: {end}")
        logger.info(f"Количество запросов: {counter}")