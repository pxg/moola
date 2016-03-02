from moola.utils import get_spreadsheet_name


def test_get_spreadsheet_name_feb():
    assert get_spreadsheet_name(2016, 2) == 'February 2016'


def test_get_spreadsheet_name_july():
    assert get_spreadsheet_name(1983, 7) == 'July 1983'
