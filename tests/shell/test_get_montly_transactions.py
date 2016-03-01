from mock import Mock

from moola.shell import experiment, experiment2
# from moola.core import Transaction, Money


def test_experiemnt():
    spreadsheet = Mock()
    spreadsheet.worksheet = Mock(return_value=[3, ])

    assert isinstance(experiment(spreadsheet), list) == True
    assert experiment(spreadsheet) == [3, ]


def test_experiment2():
    worksheet = Mock()
    worksheet.get_all_values = Mock(return_value=[3, ])
    spreadsheet = Mock()
    spreadsheet.worksheet = Mock(return_value=worksheet)

    assert isinstance(experiment2(spreadsheet), list) == True
    assert experiment2(spreadsheet) == [3, ]

# def test_get_monthly_transactions_returns_two_items():
#     assert len(_get_monthly_transactions()) == 2


# def test_get_monthly_transactions_returns_list_of_transactions():
#     assert isinstance(_get_monthly_transactions()[0], Transaction) == True


# def test_get_monthly_transactions_tranaction_day():
#     assert _get_monthly_transactions()[0].day == 2


# def test_get_monthly_transactions_tranaction_amount():
#     transaction = _get_monthly_transactions()[0]

#     assert transaction.amount.rounded_amount == Money(-9.99).rounded_amount


# def test_get_monthly_transactions_tranaction_description():
#     transaction = _get_monthly_transactions()[0]

#     assert transaction.description == 'Netflix'
