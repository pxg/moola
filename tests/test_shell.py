from moola.shell import get_amounts_for_month


def test_get_amounts_for_month_amount_for_each_day():
    amounts = get_amounts_for_month(year=2016, month=1)
    assert len(amounts) == 31


def test_get_amounts_for_month_amount_for_each_day_leap_year():
    amounts = get_amounts_for_month(year=2016, month=2)
    assert len(amounts) == 29
