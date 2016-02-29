import pytest

from collections import namedtuple
from datetime import datetime

from moola.core import (
    calc_daily_balances_for_month,
    calc_daily_spending_amount,
    calc_transactions_up_to_day,
    get_transactions_total)


def test_calc_daily_balances_for_month_amount_for_each_day():
    amounts = calc_daily_balances_for_month(
        year=2016,
        month=1,
        start_balance=2500,
        end_balance=500)
    assert len(amounts) == 31


def test_calc_daily_balances_for_month_amount_for_each_day_leap_year():
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
    assert amounts[0].date == datetime(2016, 2, 1)


def test_calc_daily_balances_for_month_last_item_correct_date():
    amounts = calc_daily_balances_for_month(
        year=2016,
        month=2,
        start_balance=2500,
        end_balance=500)
    assert amounts[-1].date == datetime(2016, 2, 29)


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
    assert amounts[-1].balance == 568.96


def test_calc_daily_spending_amount():
    assert calc_daily_spending_amount(200000, 29) == 6896.551724137931


def test_calc_daily_balances_correct_balance_with_one_transaction():
    # TODO: pull named Tuple from actual code
    # TODO: use class instead of named tuple
    Transaction = namedtuple('Transaction', 'day amount description')
    transactions = [Transaction(2, -9.99, 'Nexflix')]

    amounts = calc_daily_balances_for_month(
        year=2016,
        month=2,
        start_balance=2909.99,  # 100 spend a day
        end_balance=0,
        transactions=transactions)
    assert amounts[1].balance == 2800


def test_calc_daily_balances_correct_balance_with_two_transactions():
    # TODO: pull named Tuple from actual code
    # TODO: use class instead of named tuple
    Transaction = namedtuple('Transaction', 'day amount description')
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


def test_get_transactions_total_no_transactions():
    assert get_transactions_total([]) == 0


def test_get_transactions_total_one_transaction():
    Transaction = namedtuple('Transaction', 'day amount description')
    transactions = [Transaction(2, -9.99, 'Nexflix')]
    assert get_transactions_total(transactions) == -9.99


def test_get_transactions_total_two_transactions():
    Transaction = namedtuple('Transaction', 'day amount description')
    transactions = [
        Transaction(2, -9.99, 'Nexflix'),
        Transaction(2, -5.00, 'Spotify')]
    assert get_transactions_total(transactions) == -14.99


def test_calc_transactions_up_to_day_no_transactions():
    assert calc_transactions_up_to_day(2, []) == 0


def test_calc_transactions_up_to_day_one_transaction():
    Transaction = namedtuple('Transaction', 'day amount description')
    transactions = [Transaction(2, -9.99, 'Nexflix')]
    assert calc_transactions_up_to_day(2, transactions) == -9.99


def test_calc_transactions_up_to_day_two_transactions_different_days():
    Transaction = namedtuple('Transaction', 'day amount description')
    transactions = [
        Transaction(1, -9.99, 'Nexflix'),
        Transaction(2, -5.00, 'Spotify')]
    assert calc_transactions_up_to_day(2, transactions) == -14.99


def test_calc_transactions_up_to_day_transaction_after_day():
    Transaction = namedtuple('Transaction', 'day amount description')
    transactions = [
        Transaction(2, -9.99, 'Nexflix'),
        Transaction(3, -5.00, 'Spotify')]
    assert calc_transactions_up_to_day(2, transactions) == -9.99
