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
    return 2016, 2, 2500, 500


def _write_balances_to_spreadsheet(balances):
    # TODO: move connecting code to different function
    print('Connecting to Google Docs ...')
    # TODO: open relative to this file
    json_key = json.load(open('./moola/credentials.json'))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(
        json_key['client_email'],
        json_key['private_key'].encode(),
        scope)
    # Connect to Google docs and open worksheet
    gc = gspread.authorize(credentials)
    sh = gc.open('Money dev')
    # TODO: create sheet if it doesn't exist
    wks = sh.get_worksheet(0)

    # Add header rows
    wks.update_acell('A1', 'Date')
    wks.update_acell('B1', 'Predicted Balance')
    index = 1

    for balance in balances:
        index += 1
        date_cell = 'A{}'.format(index)
        balance_cell = 'B{}'.format(index)
        # TODO: can we upate in bulk? Will likely be faster
        wks.update_acell(date_cell, balance.date)
        wks.update_acell(balance_cell, balance.amount)

    # TODO: can we set formating on the cells?

    print('Spreadsheet updated')
    print('TODO: print URL here')

# TODO: call from init? I'd like to call command line with "moola"
if __name__ == '__main__':
    create_sheet_for_month()
