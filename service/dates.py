from datetime import datetime, timedelta, date
from config.config import settings

def get_dates_last_week() -> tuple[str, str]:
    today = datetime.today()
    weekday = today.weekday()
    days_since_last_sunday = weekday + 1
    last_sunday = today - timedelta(days=days_since_last_sunday)
    last_monday = last_sunday - timedelta(days=6)
    return last_monday.date().strftime(settings.date.format_tg), last_sunday.date().strftime(settings.date.format_tg)

def weeks_last_month(date_from: str, date_to: str):
    """
    4 недели порознь и 4 последние недели в 1 обьекте
    """     
    weeks = [(0, date_from, date_to)]
    early_week = date_from
    last_day = date_to
    for i in range(1, 4):
        date_from = (datetime.strptime(date_from, settings.date.format_tg) - timedelta(days=7)).strftime(settings.date.format_tg)
        date_to = (datetime.strptime(date_to, settings.date.format_tg) - timedelta(days=7)).strftime(settings.date.format_tg)
        weeks.append([i, date_from, date_to])
        early_week = date_from
    weeks.append([4, early_week, last_day])
    weeks.append([5, None, None])
    return weeks

def set_custom_date(dates: dict, date_from: str, date_to: str):
    """
    date Y-m-d
    """
    
    dates["weeks"][-1][1] = datetime.strptime(date_from, settings.date.format_wb).strftime(settings.date.format_tg)
    dates["weeks"][-1][2] = datetime.strptime(date_to, settings.date.format_wb).strftime(settings.date.format_tg)
    
def get_last_sunday():
        today = datetime.today()
        weekday = today.weekday()
        days_since_last_sunday = weekday + 1
        last_sunday = today - timedelta(days=days_since_last_sunday)
        return last_sunday.date()
    
def get_dates():
    date_from, date_to = get_dates_last_week()
    weeks = weeks_last_month(date_from, date_to)
    return {"weeks": weeks}