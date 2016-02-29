from calendar import monthrange
from datetime import datetime
from collections import namedtuple


def calc_daily_balances_for_month(
        year, month, start_balance, end_balance, transactions=None):
    """
    Wrapper function which converts amounts to pence, calls the actual logic
    then formats the return
    """
    balances = _calc_daily_balances_for_month(
        year,
        month,
        start_balance * 100,
        end_balance * 100,
        convert_transactions_pence(transactions))

    formatted_balances = []
    for index, balance in enumerate(balances):
        formatted_balances.append(format_balance(year, month, index, balance))
    return formatted_balances


def _calc_daily_balances_for_month(
        year, month, start_balance, end_balance, transactions=None):
    num_days = get_number_of_days_in_month(year, month)
    transactions_total = get_transactions_total(transactions)
    monthly_spend = start_balance - end_balance + transactions_total
    daily_spend = calc_daily_spending_amount(monthly_spend, num_days)

    balances = []
    for index in range(num_days):
        day = index + 1
        transaction_amount = calc_transactions_up_to_day(day, transactions)
        balance = calc_balance(
            index,
            daily_spend,
            start_balance,
            transaction_amount)
        balances.append(balance)
    return balances


# TODO: needs unit tests
def convert_transactions_pence(transactions):
    Transaction = namedtuple('Transaction', 'day amount description')
    if transactions is None:
        return []
    return [
        Transaction(t.day, t.amount * 100, t.description)for t in transactions]


def calc_transactions_up_to_day(day, transactions):
    """
    Calculate transactions up to the current day of the month
    """
    total = 0
    for transaction in transactions:
        if transaction.day <= day:
            total += transaction.amount
    return total


def get_transactions_total(transactions):
    total = 0
    for transaction in transactions:
        total += transaction.amount
    return total


# TODO: needs unit test
def calc_balance(index, daily_spend, start_balance, transaction_amount):
    return start_balance - (daily_spend * index) + transaction_amount


# TODO: needs unit test
def format_balance(year, month, index, balance):
    """
    Return balance as a tuple containg the date and the amount in pounds
    """
    Balance = namedtuple('Balance', 'date balance')
    return Balance(datetime(year, month, index + 1), int(balance) / 100)


def calc_daily_spending_amount(monthly_spend_pence, num_days):
    # TODO: research best way to deal with representing currencies in Python
    return monthly_spend_pence / num_days


# TODO: needs unit test
def get_number_of_days_in_month(year, month):
    return monthrange(year, month)[1]
