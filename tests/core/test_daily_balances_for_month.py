from datetime import date

from moola.core import daily_balances_for_month
from moola.models import Transaction


def test_daily_balances_for_month_number_of_days():
    amounts = daily_balances_for_month(year=2016, month=1, start=2500, end=500)

    assert len(amounts) == 31


def test_daily_balances_for_month_number_of_days_leap_year():
    amounts = daily_balances_for_month(year=2016, month=2, start=2500, end=500)

    assert len(amounts) == 29


def test_daily_balances_for_month_first_item_correct_date():
    amounts = daily_balances_for_month(year=2016, month=2, start=2500, end=500)

    assert amounts[0].date == date(2016, 2, 1)


def test_daily_balances_for_month_last_item_correct_date():
    amounts = daily_balances_for_month(year=2016, month=2, start=2500, end=500)

    assert amounts[-1].date == date(2016, 2, 29)


def test_daily_balances_for_month_first_item_correct_balance():
    balances = daily_balances_for_month(
        year=2016, month=2, start=2500, end=500)

    assert balances[0].amount == 2500


def test_daily_balances_for_month_second_item_correct_balance():
    balances = daily_balances_for_month(
        year=2016, month=2, start=2500, end=500)

    assert balances[1].amount == 2431.03


def test_daily_balances_for_month_last_item_correct_balance():
    balances = daily_balances_for_month(
        year=2016, month=2, start=2500, end=500)

    assert balances[-1].amount == 568.97


def test_daily_balances_correct_balance_with_one_transaction():
    transactions = [Transaction(2, -9.99, 'Nexflix')]

    balances = daily_balances_for_month(
        year=2016,
        month=2,
        start=2909.99,  # 100 spend a day
        end=0,
        transactions=transactions)

    assert balances[1].amount == 2800


def test_daily_balances_correct_balance_with_two_transactions():
    transactions = [
        Transaction(1, -5.00, 'Spotify'),
        Transaction(1, -9.99, 'Nexflix')]

    balances = daily_balances_for_month(
        year=2016,
        month=2,
        start=2914.99,  # 100 spend a day
        end=0,
        transactions=transactions)

    assert balances[1].amount == 2800
