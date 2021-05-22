import json

import gspread
from gspread.exceptions import WorksheetNotFound
from oauth2client.client import SignedJwtAssertionCredentials

from ..models import Transaction
from ..utils import (
    current_day,
    current_month_number,
    current_year,
    get_worksheet_name)


def delete_worksheet(year, month):
    """
    Function just used by end to end test to make sure we're writing to a fresh
    worksheet
    """
    spreadsheet = _get_google_spreadsheet('Money test')
    try:
        worksheet = spreadsheet.worksheet(get_worksheet_name(year, month))
        spreadsheet.del_worksheet(worksheet)
    except WorksheetNotFound:
        pass


def _print_spreadsheet_url(spreadsheet):
    url = 'https://docs.google.com/spreadsheets/d/{0}/edit'.format(
        spreadsheet.id)
    print('Spreadsheet updated {0}'.format(url))


def _get_monthly_transactions(spreadsheet):
    """
    Get monthly transactions from Google spreadsheet
    """
    print('Reading transactions data')
    worksheet = spreadsheet.worksheet('transactions')
    transaction_data_with_headers = worksheet.get_all_values()
    transaction_data = transaction_data_with_headers[1:]
    return [Transaction(*row) for row in transaction_data]


def _get_google_spreadsheet(name):
    print('Connecting to Google Docs')
    json_key = json.load(open('./moola/credentials.json'))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(
        json_key['client_email'],
        json_key['private_key'].encode(),
        scope)
    gc = gspread.authorize(credentials)
    return gc.open(name)


def _write_balances_to_spreadsheet(spreadsheet, balances, year, month):
    """
    Create the worksheet if it doesn't exist then update it's values.
    """
    name = get_worksheet_name(year, month)
    print('Worksheet name {}'.format(name))
    try:
        worksheet = spreadsheet.worksheet(name)
    except WorksheetNotFound:
        print('Not found creating worksheet')
        # TODO: can we make it the most recent spreadsheet on the tabs?
        worksheet = spreadsheet.add_worksheet(title=name, rows='32', cols='7')

    cells = worksheet.range('A1:B{0}'.format(len(balances) + 1))
    worksheet.update_cells(_set_cells(cells, balances))
    return worksheet


def _write_monzo_balances_to_spreadsheet(spreadsheet, balance):
    """
    Write today's Monzo balance to the correct sheet and cell in Google Sheets
    """
    name = get_worksheet_name(current_year(), current_month_number())
    print('Worksheet name {}'.format(name))
    # TODO: error catching in case worksheet doesn't exist
    worksheet = spreadsheet.worksheet(name)
    worksheet.update_acell('B{}'.format(current_day() + 1), balance / 100)


def _set_cells(cells, balances):
    """
    Populate cells with headers and values from balances
    """
    set_cells = []
    set_cells.append(_next_cell_set_value('Date', cells))
    set_cells.append(_next_cell_set_value('Total Aim', cells))

    for balance in balances:
        set_cells.append(_next_cell_set_value(balance.date, cells))
        set_cells.append(_next_cell_set_value(balance.amount, cells))
    return set_cells


def _next_cell_set_value(value, cells):
    """
    Get the next cells to populate set it's value and return
    """
    cell = cells.pop(0)
    cell.value = value
    return cell
