from moola.core import (
    Transaction,
    calc_transactions_total)


def test_calc_transactions_total_no_transactions():
    assert calc_transactions_total([]) == 0


def test_calc_transactions_total_one_transaction():
    transactions = [Transaction(2, -9.99, 'Nexflix')]

    total = calc_transactions_total(transactions)

    assert total.rounded_amount == -9.99


def test_calc_transactions_total_two_transactions():
    transactions = [
        Transaction(2, -9.99, 'Nexflix'),
        Transaction(2, -5.00, 'Spotify')]

    total = calc_transactions_total(transactions)

    assert total.rounded_amount == -14.99
