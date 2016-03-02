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
        Helper method so we don't need to keep casting to decimal. Makes tests
        easier to read.
        """
        amount = round(self.amount, 2)
        return int(amount * 100) / 100


class Transaction:

    def __init__(self, day, amount, description):
        self.day = int(day)
        self.amount = Money(amount)
        self.description = description

    def __repr__(self):
        return '<Transaction object ({}, {}, {})>'.format(
            self.day, self.amount, self.description)


def daily_balances_for_month(year, month, start, end, transactions=[]):
    """
    Get the predicted daily balance for each day of the month based on start
    balance end balance and a given number of financial transactions.
    """
    start_balance = Money(start)
    end_balance = Money(end)
    dates = _dates_in_month(year, month)
    daily_spend = _daily_spend(
        start_balance,
        end_balance,
        transactions,
        num_days=len(dates))
    print('Daily spend £{}'.format(daily_spend))

    month_balances = []

    Balance = namedtuple('Balance', 'date amount')
    for date in dates:
        balance = _balance_for_date(
            date,
            daily_spend,
            start_balance,
            transactions)
        month_balances.append(Balance(date, balance.rounded_amount))
    return month_balances


def _balance_for_date(date, daily_spend, start_balance, transactions):
    """
    Get predicted balance for date given
    """
    transaction_amount = _transactions_up_to_day(date.day, transactions)
    return start_balance - (daily_spend * (date.day - 1)) + transaction_amount


def _daily_spend(start_balance, end_balance, transactions, num_days):
    """
    Predicted amount that can be spent each month once transactions have been
    taken into account
    """
    monthly_spend = _monthly_spend(start_balance, end_balance, transactions)
    return monthly_spend / num_days


def _dates_in_month(year, month):
    """
    Returns a list of date objects for each date in the month
    """
    calendar = Calendar()
    dates = calendar.itermonthdates(year, month)
    return [date for date in dates if date.month == month]


def _monthly_spend(start_balance, end_balance, transactions=[]):
    """
    Predicted amount that can be spent each month once transactions have been
    taken into account
    """
    transactions_total = _transactions_total(transactions)
    return start_balance - end_balance + transactions_total


def _transactions_total(transactions):
    """
    Sum of transaction amounts
    """
    return sum([transaction.amount for transaction in transactions])


def _transactions_up_to_day(day, transactions):
    """
    Calculate sum of transactions up to the current day of the month
    """
    transaction_period = [t.amount for t in transactions if t.day <= day]
    return _transactions_total(transaction_period)
