from moola.core import _transactions_total
from moola.models import Transaction


def test_transactions_total_no_transactions():
    assert _transactions_total([]) == 0


def test_transactions_total_one_transaction():
    transactions = [Transaction(2, -9.99, "Nexflix")]

    total = _transactions_total(transactions)

    assert total.rounded_amount == -9.99


def test_transactions_total_two_transactions():
    transactions = [Transaction(2, -9.99, "Nexflix"), Transaction(2, -5.00, "Spotify")]

    total = _transactions_total(transactions)

    assert total.rounded_amount == -14.99
