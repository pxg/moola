import datetime

from moola.core import _dates_in_month


def test_dates_in_month_correct_number():
    assert len(_dates_in_month(2016, 2)) == 29


def test_dates_in_month_datetime_object():
    assert isinstance(_dates_in_month(2016, 2)[0], datetime.date) == True


def test_dates_in_month_first_date_correct():
    assert _dates_in_month(2016, 2)[0] == datetime.date(2016, 2, 1)


def test_dates_in_month_last_date_correct():
    assert _dates_in_month(2016, 2)[-1] == datetime.date(2016, 2, 29)
