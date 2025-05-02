from service.async_requests import AsyncRequests
import json
import asyncio
import logging
from config.config import settings
from .enum import WBCapitalizationEnum

logger = logging.getLogger(__name__)

class WBCapitalization:
    URI_ANALYTICS = "https://seller-analytics-api.wildberries.ru"
    URI_WAREHOUSE_REMAINS = "/api/v1/warehouse_remains"
    URI_CHECK_STATUS_DOWNLOADING = "/api/v1/warehouse_remains/tasks/{task_id}/status"
    URI_DOWNLOAD_REMAINS = "/api/v1/warehouse_remains/tasks/{task_id}/download"
    URI_PING = "/ping"
    
    def __init__(self, token: str, task_id: str = None):
        self.token = token
        self.task_id = task_id

        self.headers = {
            "Authorization": token
        }
        
        self.params_warehouse_remains = {
            "groupBySa": "true",
            "groupBySubject": "true"
        }
        
    async def request_test_token(self) -> bool:
        url = WBCapitalization.URI_ANALYTICS + WBCapitalization.URI_PING
        resp = json.loads(await AsyncRequests.get(url, headers=self.headers))
        if "Status" in resp:
            logger.info(f"+Уровень аналитики валиден")
            return True
        logger.info(f"-Уровень аналитики невалиден")
        return False
        
    async def create_report(self):
        """
        {
            "data": {
                "taskId": "c277432f-379c-4b25-8c49-02564c519538"
            }
        }
        """
        url = WBCapitalization.URI_ANALYTICS + WBCapitalization.URI_WAREHOUSE_REMAINS
        count = 10
        for i in range(count):
            ...
            
        logger.warning(f"Отчет создать не удалось")
        
    async def check_status_downloading(self):
        """
        {
            "data": {
                "id": "c277432f-379c-4b25-8c49-02564c519538",
                "status": "done"
            }
        }
        """
        url = WBCapitalization.URI_ANALYTICS + WBCapitalization.URI_CHECK_STATUS_DOWNLOADING.format(task_id=self.task_id)
        for _ in range(5):
            ...
            
        return False
        
    async def download_remains(self) -> list[dict]:
        url = WBCapitalization.URI_ANALYTICS + WBCapitalization.URI_DOWNLOAD_REMAINS.format(task_id=self.task_id)
        count = 5
        for i in range(count):
            ...
            

        logger.warning(f'Отчет скачать не удалось, task_id={self.task_id}')