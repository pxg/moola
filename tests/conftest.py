import pytest
from mock import Mock


def pytest_addoption(parser):
    parser.addoption("--runslow", action="store_true", help="run slow tests")


@pytest.fixture
def spreadsheet():
    transaction_data = [
        ["day", "amount", "description"],
        [2, -9.99, "Netflix"],
        [3, -5.00, "Spotfiy"],
    ]
    worksheet = Mock()
    worksheet.get_all_values = Mock(return_value=transaction_data)
    spreadsheet = Mock()
    spreadsheet.worksheet = Mock(return_value=worksheet)
    return spreadsheet


@pytest.fixture
def spreadsheet_dirty_data():
    transaction_data = [["day", "amount", "description"], [2, "-£1,499.99", "Rent"]]
    worksheet = Mock()
    worksheet.get_all_values = Mock(return_value=transaction_data)
    spreadsheet = Mock()
    spreadsheet.worksheet = Mock(return_value=worksheet)
    return spreadsheet
