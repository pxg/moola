from calendar import monthrange
from datetime import datetime
from collections import namedtuple


def create_sheet_for_month():
    """
    Prompt user for required values then create Google spreadsheet with amounts
    for month
    """
    pass


# TODO: functional move to core
def calc_daily_balances_for_month(year, month, start_balance, end_balance):
    # Convert balance to pence
    start_balance = start_balance * 100
    end_balance = end_balance * 100

    daily_balances = []
    days_range = get_day_range_for_month(year, month)
    monthly_spend = start_balance - end_balance
    daily_spend = calc_daily_spending_amount(monthly_spend, len(days_range))

    Balance = namedtuple('Balance', 'date balance')
    daily_balance = start_balance

    for day in days_range:
        date = datetime(year, month, day)
        # Convert back to pounds here
        date_balance = Balance(date, int(daily_balance) / 100)
        daily_balances.append(date_balance)
        daily_balance -= daily_spend
    return daily_balances


# TODO: functional move to core
def calc_daily_spending_amount(monthly_spend_pence, num_days):
    # TODO: research best way to deal with representing currencies in Python
    return monthly_spend_pence / num_days


# TODO: functional move to core
def get_day_range_for_month(year, month):
    """
    Get range for days in a given month
    """
    num_days = monthrange(year, month)[1]
    return range(1, num_days + 1)
