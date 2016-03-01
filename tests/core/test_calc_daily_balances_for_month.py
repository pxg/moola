from datetime import date
from decimal import Decimal

from moola.core import Transaction, calc_daily_balances_for_month


def test_calc_daily_balances_for_month_number_of_days():
    amounts = calc_daily_balances_for_month(
        year=2016,
        month=1,
        start_balance=2500,
        end_balance=500)

    assert len(amounts) == 31


def test_calc_daily_balances_for_month_number_of_days_leap_year():
    amounts = calc_daily_balances_for_month(
        year=2016,
        month=2,
        start_balance=2500,
        end_balance=500)

    assert len(amounts) == 29


def test_calc_daily_balances_for_month_first_item_correct_date():
    amounts = calc_daily_balances_for_month(
        year=2016,
        month=2,
        start_balance=2500,
        end_balance=500)

    assert amounts[0].date == date(2016, 2, 1)


def test_calc_daily_balances_for_month_last_item_correct_date():
    amounts = calc_daily_balances_for_month(
        year=2016,
        month=2,
        start_balance=2500,
        end_balance=500)

    # TODO: can we remove the zeros?
    assert amounts[-1].date == date(2016, 2, 29)


def test_calc_daily_balances_for_month_first_item_correct_balance():
    amounts = calc_daily_balances_for_month(
        year=2016,
        month=2,
        start_balance=2500,
        end_balance=500)

    assert amounts[0].balance == 2500


def test_calc_daily_balances_for_month_second_item_correct_balance():
    amounts = calc_daily_balances_for_month(
        year=2016,
        month=2,
        start_balance=2500,
        end_balance=500)

    assert amounts[1].balance == 2431.03


def test_calc_daily_balances_for_month_last_item_correct_balance():
    amounts = calc_daily_balances_for_month(
        year=2016,
        month=2,
        start_balance=2500,
        end_balance=500)

    assert amounts[-1].balance == 568.97


def test_calc_daily_balances_correct_balance_with_one_transaction():
    transactions = [Transaction(2, -9.99, 'Nexflix')]

    amounts = calc_daily_balances_for_month(
        year=2016,
        month=2,
        start_balance=2909.99,  # 100 spend a day
        end_balance=0,
        transactions=transactions)

    assert amounts[1].balance == 2800


def test_calc_daily_balances_correct_balance_with_two_transactions():
    transactions = [
        Transaction(1, -5.00, 'Spotify'),
        Transaction(1, -9.99, 'Nexflix')]

    amounts = calc_daily_balances_for_month(
        year=2016,
        month=2,
        start_balance=2914.99,  # 100 spend a day
        end_balance=0,
        transactions=transactions)

    assert amounts[1].balance == 2800
