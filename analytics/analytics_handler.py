import logging
import traceback
from datetime import datetime, timedelta, date
from config.config import settings
from external.google_sheets import SpreadSheets
from database.models.user.dao import UserDAO
from database.models.user_moving.dao import UserMovingDAO
from database.models.user_moving.enum import Step
from .model import SpreadSheetRow

logger = logging.getLogger(__name__)

class AnalyticsHandler:
    
    @classmethod
    async def get_count_new_users(cls, yesterday: datetime, today: datetime):
        """Сколько новых пользователей за период"""    
        user = UserDAO.model
        return await UserDAO.get_count(user.created_at > yesterday, user.created_at < today) 

    @classmethod
    async def get_count_moving_users(cls, yesterday: datetime, today: datetime):
        """Сколько активных пользователей за период """
        user_moving = UserMovingDAO.model
        return await UserMovingDAO.get_count_distinct("chat_id", user_moving.created_at > yesterday, user_moving.created_at < today)

    
    @classmethod
    def get_dates_between(cls, start_date: date, end_date: date):
        date_list = []
        current_date = start_date + timedelta(days=1)
        while current_date < end_date:
            date_list.append(current_date)
            current_date += timedelta(days=1)
        
        return date_list

    @classmethod
    async def handle_aggregates(cls, sheet: SpreadSheets, date: datetime, next_date: datetime):
        d = date
        next_d = next_date
        row = SpreadSheetRow(
            date_=d.strftime('%d.%m.%Y'),
            new_users=await cls.get_count_new_users(d, next_d),
            active_users=await cls.get_count_moving_users(d, next_d),
            blocked_users=await cls.get_count_blocked_users(d, next_d),
            scenario_menu=await cls.get_count_scenario_menu(d, next_d),
            scenario_menu_uniqie=await cls.get_unique_scenario_menu(d, next_d),
            scenario_set_token=await cls.get_count_scenario_set_token(d, next_d),
            scenario_set_token_uniqie=await cls.get_unique_scenario_set_token(d, next_d),
            scenario_set_file=await cls.get_count_scenario_set_file(d, next_d),
            scenario_set_file_uniqie=await cls.get_unique_scenario_set_file(d, next_d),
            scenario_choose_week=await cls.get_count_scenario_choose_week(d, next_d),
            scenario_choose_week_uniqie=await cls.get_unique_scenario_choose_week(d, next_d),
            scenario_standart_report=await cls.get_count_scenario_standart_report(d, next_d),
            scenario_standart_report_uniqie=await cls.get_unique_scenario_standart_report(d, next_d),
            scenario_deep_report=await cls.get_count_scenario_deep_report(d, next_d),
            scenario_deep_report_uniqie=await cls.get_unique_scenario_deep_report(d, next_d),
            scenario_missed_supplier_report=await cls.get_count_scenario_missed_s_report(d, next_d),
            scenario_missed_supplier_report_uniqie=await cls.get_unique_scenario_missed_s_report(d, next_d),
            scenario_payment_create=await cls.get_payment_create(d, next_d),
            scenario_payment_success=await cls.get_payment_success(d, next_d),
            scenario_payment_fail=await cls.get_payment_fail(d, next_d)
        )
        await sheet.write_values([list(row.asdict().values())]) 
        
    @classmethod
    async def upload_spreadsheets(cls):
        try:
            ss_agg = SpreadSheets()

            agg_rows = await ss_agg.get_values()

            if len(agg_rows) > 0:
                last_date = agg_rows[-1][0]
                today = datetime.today() - timedelta(days=1)

                dates = cls.get_dates_between(last_date, today)
                for d in dates:
                    next_d = (d + timedelta(days=1)).replace(hour=0, minute=0, second=0)
                    await cls.handle_aggregates(ss_agg, d, next_d)
                logger.info("Таблица Агрегации обновлена")
        except Exception:
            logger.critical(traceback.format_exc())