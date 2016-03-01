from calendar import Calendar
from collections import namedtuple
from datetime import datetime

from money import Money as BaseMoney


class Money(BaseMoney):

    def __init__(self, *args, **kwargs):
        """
        Class the super class constructor with the currency set to pounds
        """
        super().__init__(*(args[0], 'GBP'), **kwargs)

    @property
    def rounded_amount(self):
        """
        Helper method to make tests easier to read
        """
        amount = round(self.amount, 2)
        return int(amount * 100) / 100


class Transaction:

    def __init__(self, day, amount, description):
        self.day = day
        self.amount = Money(amount)
        self.description = description


def calc_daily_balances_for_month(
        year, month, start_balance, end_balance, transactions=[]):
    balances = _calc_daily_balances_for_month(
        year,
        month,
        Money(start_balance),
        Money(end_balance),
        transactions)

    formatted_balances = []
    for index, balance in enumerate(balances):
        formatted_balances.append(format_balance(year, month, index, balance))
    return formatted_balances


def _calc_daily_balances_for_month(
        year, month, start_balance, end_balance, transactions=[]):
    dates = get_days_in_month(year, month)

    # TODO: calc monthly spend in function which takes transactions
    transactions_total = calc_transactions_total(transactions)
    monthly_spend = start_balance - end_balance + transactions_total

    daily_spend = monthly_spend / len(dates)

    balances = []
    # TODO: add datetime and balance in this function.
    # TODO: move loop in outer function
    for day in dates:
        transaction_amount = calc_transactions_up_to_day(day.day, transactions)
        balance = calc_balance(
            day.day,
            daily_spend,
            start_balance,
            transaction_amount)
        balances.append(balance)
    return balances


def _calc_monthly_spend(start_balance, end_balance, transactions=[]):
    transactions_total = calc_transactions_total(transactions)
    return start_balance - end_balance + transactions_total


def calc_transactions_up_to_day(day, transactions):
    """
    Calculate transactions up to the current day of the month
    """
    transaction_period = [t.amount for t in transactions if t.day <= day]
    return calc_transactions_total(transaction_period)


def calc_transactions_total(transactions):
    return sum([transaction.amount for transaction in transactions])


# TODO: needs unit tests
def calc_balance(day, daily_spend, start_balance, transaction_amount):
    return start_balance - (daily_spend * (day - 1)) + transaction_amount


# TODO: remove when logic is reworked
# TODO: needs unit tests
def format_balance(year, month, index, balance):
    """
    Return balance as a tuple containing the date and the amount in pounds and
    pence.
    """
    Balance = namedtuple('Balance', 'date balance')
    return Balance(datetime(year, month, index + 1), round(balance.amount, 2))


def get_days_in_month(year, month):
    calendar = Calendar()
    dates = calendar.itermonthdates(year, month)
    return [date for date in dates if date.month == month]
