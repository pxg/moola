from moola.core import _daily_spend
from moola.models import Transaction, Money


def test_daily_spend_empty_transactinons():
    spend = _daily_spend(
        start_balance=Money(2000),
        end_balance=Money(500),
        transactions=[],
        num_days=29)

    assert spend.rounded_amount == Money(1500 / 29).rounded_amount


def test_daily_spend_one_transactinon():
    spend = _daily_spend(
        start_balance=Money(2000),
        end_balance=Money(500),
        transactions=[Transaction(2, -9.99, 'Nexflix')],
        num_days=29)

    assert spend.rounded_amount == Money((1500 - 9.99) / 29).rounded_amount


def test_daily_spend_two_transactinons():
    transactions = [
        Transaction(1, -5.00, 'Spotify'),
        Transaction(1, -9.99, 'Nexflix')]

    spend = _daily_spend(
        start_balance=Money(2000),
        end_balance=Money(500),
        transactions=transactions,
        num_days=29)

    assert spend.rounded_amount == Money((1500 - 14.99) / 29).rounded_amount
