from calendar import Calendar
from collections import namedtuple

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
    # Cast types to money
    start_balance = Money(start_balance)
    end_balance = Money(end_balance)

    dates = get_days_in_month(year, month)
    monthly_spend = _monthly_spend(start_balance, end_balance, transactions)
    daily_spend = monthly_spend / len(dates)

    balances = []
    Balance = namedtuple('Balance', 'date balance')
    for date in dates:
        transaction_amount = calc_transactions_up_to_day(
            date.day,
            transactions)
        balance = calc_balance(
            date.day,
            daily_spend,
            start_balance,
            transaction_amount)
        balances.append(Balance(date, balance.rounded_amount))
    return balances


def _monthly_spend(start_balance, end_balance, transactions=[]):
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


def get_days_in_month(year, month):
    calendar = Calendar()
    dates = calendar.itermonthdates(year, month)
    return [date for date in dates if date.month == month]
