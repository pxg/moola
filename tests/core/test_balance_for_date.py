from datetime import date

from moola.core import _balance_for_date, Money, Transaction


def test_balance_for_date_no_transactions():
    balance = _balance_for_date(
        date=date(2016, 2, 2),
        daily_spend=Money(50),
        start_balance=Money(1000),
        transactions=[])

    assert balance == Money(950)


def test_balance_for_date_one_transactions():
    balance = _balance_for_date(
        date=date(2016, 2, 2),
        daily_spend=Money(50),
        start_balance=Money(1000),
        transactions=[Transaction(2, -9.99, 'Nexflix')])

    assert balance.rounded_amount == Money(950 - 9.99).rounded_amount
