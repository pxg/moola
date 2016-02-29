from datetime import datetime
from decimal import Decimal

from moola.core import (
    Money,
    Transaction,
    calc_daily_balances_for_month,
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
    assert amounts[0].balance == Decimal('2500')


def test_calc_daily_balances_for_month_second_item_correct_balance():
    amounts = calc_daily_balances_for_month(
        year=2016,
        month=2,
        start_balance=2500,
        end_balance=500)
    assert amounts[1].balance == Decimal('2431.03')


def test_calc_daily_balances_for_month_last_item_correct_balance():
    amounts = calc_daily_balances_for_month(
        year=2016,
        month=2,
        start_balance=2500,
        end_balance=500)
    assert amounts[-1].balance == Decimal('568.97')


def test_calc_daily_balances_correct_balance_with_one_transaction():
    transactions = [Transaction(2, -9.99, 'Nexflix')]

    amounts = calc_daily_balances_for_month(
        year=2016,
        month=2,
        start_balance=2909.99,  # 100 spend a day
        end_balance=0,
        transactions=transactions)
    assert amounts[1].balance == Decimal('2800')


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
    assert amounts[1].balance == Decimal('2800')


def test_get_transactions_total_no_transactions():
    assert get_transactions_total([]) == Money(0, 'GBP')


def test_get_transactions_total_one_transaction():
    transactions = [Transaction(2, -9.99, 'Nexflix')]
    total = get_transactions_total(transactions)
    assert total.rounded_amount == -9.99


def test_get_transactions_total_two_transactions():
    transactions = [
        Transaction(2, -9.99, 'Nexflix'),
        Transaction(2, -5.00, 'Spotify')]
    total = get_transactions_total(transactions)
    assert total.rounded_amount == -14.99


def test_calc_transactions_up_to_day_no_transactions():
    assert calc_transactions_up_to_day(2, []) == 0


def test_calc_transactions_up_to_day_one_transaction():
    transactions = [Transaction(2, -9.99, 'Nexflix')]
    amount = calc_transactions_up_to_day(2, transactions)
    assert amount.rounded_amount == -9.99


def test_calc_transactions_up_to_day_two_transactions_different_days():
    transactions = [
        Transaction(1, -9.99, 'Nexflix'),
        Transaction(2, -5.00, 'Spotify')]
    amount = calc_transactions_up_to_day(2, transactions)
    assert amount.rounded_amount == -14.99


def test_calc_transactions_up_to_day_transaction_after_day():
    transactions = [
        Transaction(2, -9.99, 'Nexflix'),
        Transaction(3, -5.00, 'Spotify')]
    amount = calc_transactions_up_to_day(2, transactions)
    assert amount.rounded_amount == -9.99


def test_money_class_addition():
    total = Money(14.99, 'GBP') + Money(5.00, 'GBP')
    assert total.rounded_amount == 19.99


def test_money_class_rounded_amount():
    a = Money(14.99, 'GBP')
    assert a.rounded_amount == 14.99


def test_money_class_rounded_amount_addition():
    total = Money(14.99, 'GBP') + Money(5.00, 'GBP')
    assert total.rounded_amount == 19.99
