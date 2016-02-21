from moola.shell import get_amounts_for_month


def test_get_amounts_for_month_amount_for_each_day():
    amounts = get_amounts_for_month(month=2, year=2017)
    assert len(amounts) == 29


# def test_get_amounts_for_month_amount_for_each_day_leap_year():
#     amounts = get_amounts_for_month(month=1, year=2017)
#     assert len(amounts) == 31
