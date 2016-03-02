from decimal import Decimal

from moola.core import _transactions_up_to_day
from moola.models import Transaction


def test_transactions_up_to_day_no_transactions():
    assert _transactions_up_to_day(2, []) == 0


def test_transactions_up_to_day_one_transaction():
    transactions = [Transaction(2, -9.99, 'Nexflix')]

    amount = _transactions_up_to_day(2, transactions)

    assert round(amount, 2) == Decimal('-9.99')


def test_transactions_up_to_day_two_transactions_different_days():
    transactions = [
        Transaction(1, -9.99, 'Nexflix'),
        Transaction(2, -5.00, 'Spotify')]

    amount = _transactions_up_to_day(2, transactions)

    assert round(amount, 2) == Decimal('-14.99')


def test_transactions_up_to_day_transaction_after_day():
    transactions = [
        Transaction(2, -9.99, 'Nexflix'),
        Transaction(3, -5.00, 'Spotify')]

    amount = _transactions_up_to_day(2, transactions)

    assert round(amount, 2) == Decimal('-9.99')
