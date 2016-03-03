from datetime import datetime
from mock import patch

from moola.utils import (
    clean_amount,
    current_month_number,
    current_year,
    get_worksheet_name)


def test_clean_amount_only_decimal_input():
    assert clean_amount(20.99) == '20.99'


def test_clean_amount_only_formatted_input():
    assert clean_amount('-£1,499.99') == '-1499.99'


def test_current_month_number():
    with patch('moola.utils.datetime') as mock_datetime:
        mock_datetime.now.return_value = datetime(2016, 2, 2, 15, 36)
        assert current_month_number() == 2


def test_current_year():
    with patch('moola.utils.datetime') as mock_datetime:
        mock_datetime.now.return_value = datetime(2015, 2, 2, 15, 36)
        assert current_year() == 2015


def test_get_spreadsheet_name_feb():
    assert get_worksheet_name(2016, 2) == 'February 2016'


def test_get_worksheet_name_july():
    assert get_worksheet_name(1983, 7) == 'July 1983'
