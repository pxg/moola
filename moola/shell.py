import json

import gspread
from oauth2client.client import SignedJwtAssertionCredentials

from moola.core import daily_balances_for_month, Transaction


def create_sheet_for_month():
    """
    Prompt user for required values then create Google spreadsheet with amounts
    for month
    """
    year, month, start, end = _prompt_user_for_inputs()
    transactions = _get_monthly_transactions()
    balances = daily_balances_for_month(
        year,
        month,
        start,
        end,
        transactions)
    _write_balances_to_spreadsheet(balances)


def _get_monthly_transactions():
    """
    Get monthly transactions from persistent storage
    """
    # TODO: add real transactions here
    # TODO: read from spreadsheet
    return [
        Transaction(2, -9.99, 'Netflix'),
        Transaction(3, -5.00, 'Spotify')]


def _prompt_user_for_inputs():
    # TODO: prompt user for month, year, start and end balance
    # TODO: can this be tested easily
    return 2016, 2, 2500, 200


def _write_balances_to_spreadsheet(balances):
    print('Connecting to Google Docs ...')
    json_key = json.load(open('credentials.json'))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(
        json_key['client_email'],
        json_key['private_key'].encode(),
        scope)
    # Connect to Google docs
    gc = gspread.authorize(credentials)
    print(gc)
    sh = gc.open('Money dev')
    print(sh)
    wks = sh.get_worksheet(0)
    print(wks)

    # Open a worksheet from spreadsheet with one shot
    # url = 'https://docs.google.com/spreadsheets/d/1yBMA3l0aU66Sf7d3zwQ4VnqONKR-pd0XCfF-p3x28s0/edit#gid=459459683'
    # # wks = gc.open(url).sheet1
    # wks = gc.open('Money Dev').sheet1
    wks.update_acell('B2', 'blah blah')
    # # Fetch a cell range
    # cell_list = wks.range('A1:B7')

    # TODO: Create sheet if it doesn't exist
    # TODO: Write data
    print('Spreadsheet updated')
    print('TODO: print URL here')

# TODO: call from init? I'd like to call command line with "moola"
if __name__ == '__main__':
    create_sheet_for_month()
