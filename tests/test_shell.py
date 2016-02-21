from datetime import datetime

from moola.shell import (
    calc_daily_balances_for_month,
    calc_daily_spending_amount)


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
    assert amounts[0].balance == 2500


def test_calc_daily_balances_for_month_second_item_correct_balance():
    amounts = calc_daily_balances_for_month(
        year=2016,
        month=2,
        start_balance=2500,
        end_balance=500)
    assert amounts[1].balance == 2431.03


def test_calc_daily_balances_for_month_last_item_correct_balance():
    amounts = calc_daily_balances_for_month(
        year=2016,
        month=2,
        start_balance=2500,
        end_balance=500)
    assert amounts[-1].balance == 568.96


def test_calc_daily_spending_amount():
    assert calc_daily_spending_amount(200000, 29) == 6896.551724137931
