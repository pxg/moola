from calendar import monthrange
from datetime import datetime
from collections import namedtuple


def calc_daily_balances_for_month(year, month, start_balance, end_balance):
    # Convert balance to pence
    start_balance = start_balance * 100
    end_balance = end_balance * 100

    num_days = get_number_of_days_in_month(year, month)
    monthly_spend = start_balance - end_balance
    daily_spend = calc_daily_spending_amount(monthly_spend, num_days)

    balances = [
        calc_balance(day, daily_spend, start_balance) for day in range(num_days)]
    daily_balances = [
        format_balance(year, month, day, balance) for day, balance in enumerate(balances)]
    return daily_balances


def calc_balance(day, daily_spend, start_balance):
    if day > 0:
        return start_balance - (daily_spend * day)
    return start_balance


def format_balance(year, month, day, balance):
    Balance = namedtuple('Balance', 'date balance')
    date = datetime(year, month, day + 1)
    return Balance(date, int(balance) / 100)


def calc_daily_spending_amount(monthly_spend_pence, num_days):
    # TODO: research best way to deal with representing currencies in Python
    return monthly_spend_pence / num_days


def get_number_of_days_in_month(year, month):
    return monthrange(year, month)[1]


# TODO: remove this function
def get_day_range_for_month(year, month):
    """
    Get range for days in a given month
    """
    num_days = monthrange(year, month)[1]
    return range(1, num_days + 1)
