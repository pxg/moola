from calendar import monthrange, Calendar
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
    num_days = get_number_of_days_in_month(year, month)
    transactions_total = calc_transactions_total(transactions)
    monthly_spend = start_balance - end_balance + transactions_total
    daily_spend = monthly_spend / num_days

    balances = []
    # TODO: get list of days for for loop new function
    # TODO: add datetime and balance in this function.
    # Remove loop in outer function
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


def calc_transactions_up_to_day(day, transactions):
    """
    Calculate transactions up to the current day of the month
    """
    transaction_period = [t.amount for t in transactions if t.day <= day]
    return calc_transactions_total(transaction_period)


def calc_transactions_total(transactions):
    return sum([transaction.amount for transaction in transactions])


# TODO: needs unit tests
def calc_balance(index, daily_spend, start_balance, transaction_amount):
    return start_balance - (daily_spend * index) + transaction_amount


# TODO: to remove
# TODO: needs unit tests
def format_balance(year, month, index, balance):
    """
    Return balance as a tuple containg the date and the amount in pounds and
    pence.
    """
    Balance = namedtuple('Balance', 'date balance')
    return Balance(datetime(year, month, index + 1), round(balance.amount, 2))


# TODO: needs unit test
def get_number_of_days_in_month(year, month):
    return monthrange(year, month)[1]


def get_days_in_month(year, month):
    calendar = Calendar()
    dates = calendar.itermonthdates(year, month)
    return [date for date in dates if date.month == month]
