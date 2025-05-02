from datetime import datetime, timedelta
from service.handling_data import InputDataHandler
from external.wildberries.wb_detalization import WBDetalization
from config.config import settings
from copy import copy
from service.user_data import UserData
import json
import logging
import aiofiles

logger = logging.getLogger(__name__)

class DetalizationPipeline:
    
    last_month_weeks: list[list]
    
    @classmethod
    def _fields(cls, 
                      missed_articles: list[str] = None, 
                      sum_seller: float = None,
                      sum_wb: float = None,
                      stable_expence: float = None,
                      agg_suppliers = None,
                      article_missed_suppliers = None,
                      sum_retail_amount = None):
        ...
    
    @classmethod
    def _get_wb_sum(cls, wb_data: list[dict], sales, returns):
        ...
    
    @classmethod
    def _get_wb_sum_sync(cls, wb_data: list[dict], sales, returns):
        ...
    
    
    @classmethod
    def _get_missed_items(cls, input_data, sales):
        ...
    
    @classmethod
    def _get_seller_sum(cls, input_data, sales):
        ...
    
    
    @classmethod
    def _aggregate_suppliers(cls, input_data, wb_data):
        ...

    @classmethod
    def _get_sum_retail_amount(cls, wb_data: list):
        report_1 = list(filter(lambda x: x["report_type"] == 1, wb_data))
        sales_1 = list(filter(lambda x: x["supplier_oper_name"] == "Продажа", report_1))
        returns_1 = list(filter(lambda x: x["supplier_oper_name"] == "Возврат", report_1))
        retail_amount_sales = sum(list(map(lambda x: x["retail_amount"], sales_1)))
        retail_amount_returns = sum(list(map(lambda x: x["retail_amount"], returns_1)))
        retail_amount_1 = retail_amount_sales - retail_amount_returns
        
        report_2 = list(filter(lambda x: x["report_type"] == 2, wb_data))
        sales_2 = list(filter(lambda x: x["supplier_oper_name"] == "Продажа", report_2))
        returns_2 = list(filter(lambda x: x["supplier_oper_name"] == "Возврат", report_2))
        retail_amount_sales = sum(list(map(lambda x: x["retail_amount"], sales_2)))
        retail_amount_returns = sum(list(map(lambda x: x["retail_amount"], returns_2)))
        retail_amount_2 = retail_amount_sales - retail_amount_returns
        
        res = retail_amount_1 + retail_amount_2
        return res
            
    @classmethod 
    def matching(cls, wb_data: list, input_data: list) -> dict:
        ...