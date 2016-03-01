from moola.shell import _get_monthly_transactions
from moola.core import Transaction, Money


def test_get_monthly_transactions_returns_list():
    assert isinstance(_get_monthly_transactions(), list) == True


def test_get_monthly_transactions_returns_two_items():
    assert len(_get_monthly_transactions()) == 2


def test_get_monthly_transactions_returns_list_of_transactions():
    assert isinstance(_get_monthly_transactions()[0], Transaction) == True


def test_get_monthly_transactions_tranaction_day():
    assert _get_monthly_transactions()[0].day == 2


def test_get_monthly_transactions_tranaction_amount():
    transaction = _get_monthly_transactions()[0]

    assert transaction.amount.rounded_amount == Money(-9.99).rounded_amount


def test_get_monthly_transactions_tranaction_description():
    transaction = _get_monthly_transactions()[0]

    assert transaction.description == 'Netflix'
