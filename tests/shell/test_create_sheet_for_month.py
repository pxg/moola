import pytest

from moola.shell import create_sheet_for_month
from moola.shell.gsheets import delete_worksheet

slow = pytest.mark.skipif(
    not pytest.config.getoption("--runslow"),
    reason="need --runslow option to run"
)


@slow
def test_create_sheet_for_month_success():
    """
    This test is the only one which actually connects to the Google API, do not
    run frequently as API is likely rate limited.
    """
    # Delete existing worksheet before we start
    year = 1984
    month = 1
    delete_worksheet(year, month)

    worksheet = create_sheet_for_month(
        year=year,
        month=month,
        start=2000,
        end=500,
        environment='test')

    # Get data to test
    cells = worksheet.range('A1:B32')
    data_cells = cells[2:]
    date_cells = [cell for cell in data_cells if cell._col == 1]
    amount_cells = [cell for cell in data_cells if cell._col == 2]
    # Test row headings
    assert cells[0].value == 'Date'
    assert cells[1].value == 'Total Aim'
    # Test date cells
    assert len(date_cells) == 31
    assert date_cells[0].value == '1/1/1984'
    assert date_cells[19].value == '1/20/1984'
    assert date_cells[-1].value == '1/31/1984'
    # Test amount cells
    assert amount_cells[0].value == '2610.75'
    assert amount_cells[12].value == '743.18'
    assert amount_cells[-1].value == '512.8'  # TODO: format cells in Gdocs
