from calendar import monthrange
from datetime import datetime
from collections import namedtuple


def calc_daily_balances_for_month(year, month, start_balance, end_balance):
    """
    Wrapper function which converts amounts to pence, calls the actual logic
    then formats the return
    """
    balances = _calc_daily_balances_for_month(
        year, month, start_balance * 100, end_balance * 100)
    formatted_balances = []
    for index, balance in enumerate(balances):
        formatted_balances.append(format_balance(year, month, index, balance))
    return formatted_balances


def _calc_daily_balances_for_month(year, month, start_balance, end_balance):
    num_days = get_number_of_days_in_month(year, month)
    monthly_spend = start_balance - end_balance
    daily_spend = calc_daily_spending_amount(monthly_spend, num_days)

    balances = []
    for day in range(num_days):
        balances.append(calc_balance(day, daily_spend, start_balance))
    return balances


def get_transactions_total(transactions):
    total = 0
    for transaction in transactions:
        total += transaction.amount * 100
    return total


def calc_balance(index, daily_spend, start_balance):
    return start_balance - (daily_spend * index)


def format_balance(year, month, index, balance):
    """
    Return balance as a tuple containg the date and the amount in pounds
    """
    Balance = namedtuple('Balance', 'date balance')
    return Balance(datetime(year, month, index + 1), int(balance) / 100)


def calc_daily_spending_amount(monthly_spend_pence, num_days):
    # TODO: research best way to deal with representing currencies in Python
    return monthly_spend_pence / num_days


def get_number_of_days_in_month(year, month):
    return monthrange(year, month)[1]
