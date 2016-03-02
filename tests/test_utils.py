from datetime import datetime
from mock import patch

from moola.utils import get_spreadsheet_name, current_month_number


def test_get_spreadsheet_name_feb():
    assert get_spreadsheet_name(2016, 2) == 'February 2016'


def test_get_spreadsheet_name_july():
    assert get_spreadsheet_name(1983, 7) == 'July 1983'


def test_get_current_month():
    with patch('moola.utils.datetime') as mock_datetime:
        mock_datetime.now.return_value = datetime(2016, 2, 2, 15, 36)
        assert current_month_number() == 2
