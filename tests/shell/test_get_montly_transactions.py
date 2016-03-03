from moola.shell import _get_monthly_transactions
from moola.models import Transaction, Money


def test_get_monthly_transactions_returns_list(spreadsheet):
    assert isinstance(_get_monthly_transactions(spreadsheet), list) == True


def test_get_monthly_transactions_returns_two_items(spreadsheet):
    assert len(_get_monthly_transactions(spreadsheet)) == 2


def test_get_monthly_transactions_returns_list_of_transactions(spreadsheet):
    transaction = _get_monthly_transactions(spreadsheet)[0]

    assert isinstance(transaction, Transaction) == True


def test_get_monthly_transactions_transaction_day(spreadsheet):
    assert _get_monthly_transactions(spreadsheet)[0].day == 2


def test_get_monthly_transactions_transaction_amount(spreadsheet):
    transaction = _get_monthly_transactions(spreadsheet)[0]

    assert transaction.amount.rounded_amount == Money(-9.99).rounded_amount


def test_get_monthly_transactions_transaction_description(spreadsheet):
    transaction = _get_monthly_transactions(spreadsheet)[0]

    assert transaction.description == 'Netflix'


def test_get_monthly_transactions_transaction_dirty_amount(
        spreadsheet_dirty_data):
    transaction = _get_monthly_transactions(spreadsheet_dirty_data)[0]

    assert transaction.amount.rounded_amount == Money(-1499.99).rounded_amount
