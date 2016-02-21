from datetime import datetime

from moola.shell import get_amounts_for_month


def test_get_amounts_for_month_amount_for_each_day():
    amounts = get_amounts_for_month(
        year=2016,
        month=1,
        start_balance=2500,
        end_balance=500)
    assert len(amounts) == 31


def test_get_amounts_for_month_amount_for_each_day_leap_year():
    amounts = get_amounts_for_month(
        year=2016,
        month=2,
        start_balance=2500,
        end_balance=500)
    assert len(amounts) == 29


def test_get_amounts_for_month_first_item_correct_date():
    amounts = get_amounts_for_month(
        year=2016,
        month=2,
        start_balance=2500,
        end_balance=500)
    assert amounts[0].date == datetime(2016, 2, 1)


def test_get_amounts_for_month_last_item_correct_date():
    amounts = get_amounts_for_month(
        year=2016,
        month=2,
        start_balance=2500,
        end_balance=500)
    assert amounts[-1].date == datetime(2016, 2, 29)


def test_get_amounts_for_month_first_item_correct_balance():
    amounts = get_amounts_for_month(
        year=2016,
        month=2,
        start_balance=2500,
        end_balance=500)
    assert amounts[0].balance == 2500
