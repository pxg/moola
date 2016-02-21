from calendar import monthrange
from datetime import datetime
from collections import namedtuple


def create_sheet_for_month():
    """
    Prompt user for required values then create Google spreadsheet with amounts
    for month
    """
    pass


def calc_daily_balances_for_month(year, month, start_balance, end_balance):
    daily_balances = []
    Balance = namedtuple('Balance', 'date balance')

    for day in get_day_range_for_month(year, month):
        date = datetime(year, month, day)
        date_balance = Balance(date, 2500)
        daily_balances.append(date_balance)
    return daily_balances


def get_day_range_for_month(year, month):
    """
    Get range for days in a given month
    """
    num_days = monthrange(year, month)[1]
    return range(1, num_days + 1)
