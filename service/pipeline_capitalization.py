import json
from service.user_data import UserData
from external.wildberries.wb_capitalization import WBCapitalization
from service.handling_data import InputDataHandler
import asyncio
import logging

logger = logging.getLogger(__name__)

class CapitalizationPipeline:
    
    @classmethod
    def _fields(cls, 
            task_id: str = None,
            missed_articles: list[str] = None, 
            count_remains: int = None,
            sum_to_client: float = None,
            sum_from_client: float = None,
            sum_in_warehouse: float = None,
            sum_remains: float = None
    ):
        ...
    
    @classmethod
    async def _get_missed_items(cls, input_data, remains):
        ...
    
    @classmethod
    async def _get_sum_remains(cls, input_data, remains):
        ...
    
    @classmethod
    async def matching(cls, chat_id: int, task_id: str = None):
        ...
        

        
        
        

        
        
        