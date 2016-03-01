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
        easier to read
        """
        amount = round(self.amount, 2)
        return int(amount * 100) / 100


class Transaction:

    def __init__(self, day, amount, description):
        self.day = day
        self.amount = Money(amount)
        self.description = description


def daily_balances_for_month(year, month, start, end, transactions=[]):
    start_balance = Money(start)
    end_balance = Money(end)
    dates = _dates_in_month(year, month)
    # TODO: Monthly spend only used to calc daily spend so move out
    monthly_spend = _monthly_spend(start_balance, end_balance, transactions)
    daily_spend = monthly_spend / len(dates)

    month_balances = []
    Balance = namedtuple('Balance', 'date balance')
    for date in dates:
        balance = _balance_for_date(
            date,
            daily_spend,
            start_balance,
            transactions)
        month_balances.append(Balance(date, balance.rounded_amount))
    return month_balances


# TODO: write tests
def _daily_spend(start_balance, end_balance, transactions, num_days):
    pass


def _monthly_spend(start_balance, end_balance, transactions=[]):
    """
    Amount that can be spent each month once transactions have been taken into
    account
    """
    transactions_total = _transactions_total(transactions)
    return start_balance - end_balance + transactions_total


def _transactions_up_to_day(day, transactions):
    """
    Calculate transactions up to the current day of the month
    """
    transaction_period = [t.amount for t in transactions if t.day <= day]
    return _transactions_total(transaction_period)


def _transactions_total(transactions):
    """
    Sum total of transaction amounts
    """
    return sum([transaction.amount for transaction in transactions])


# TODO: needs unit tests
def _balance_for_date(date, daily_spend, start_balance, transactions):
    """
    Get predicted balance for date given
    """
    transaction_amount = _transactions_up_to_day(date.day, transactions)
    return start_balance - (daily_spend * (date.day - 1)) + transaction_amount


def _dates_in_month(year, month):
    """
    Returns a list of date objects for each date in the month
    """
    calendar = Calendar()
    dates = calendar.itermonthdates(year, month)
    return [date for date in dates if date.month == month]
