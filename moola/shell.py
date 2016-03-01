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

    spreadsheet = _get_google_spreadsheet()
    transactions = _get_monthly_transactions(spreadsheet)

    balances = daily_balances_for_month(
        year,
        month,
        start,
        end,
        transactions)

    _write_balances_to_spreadsheet(spreadsheet, balances)


def _prompt_user_for_inputs():
    # TODO: prompt user for month, year, start and end balance
    # TODO: can this be tested easily
    return 2016, 2, 2500, 500


def _get_monthly_transactions(spreadsheet):
    """
    Get monthly transactions from Google spreadsheet.
    """
    print('Reading transactions data')
    worksheet = spreadsheet.worksheet('transactions')
    transaction_data = worksheet.get_all_values()
    no_headers = slice(1, len(transaction_data))
    return [Transaction(*row) for row in transaction_data[no_headers]]


def _get_google_spreadsheet():
    print('Connecting to Google Docs')
    # TODO: open relative to this file
    json_key = json.load(open('./moola/credentials.json'))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(
        json_key['client_email'],
        json_key['private_key'].encode(),
        scope)
    gc = gspread.authorize(credentials)
    return gc.open('Money dev')


def _write_balances_to_spreadsheet(spreadsheet, balances):
    # TODO1: use month name to look-up the spreadsheet
    # TODO2: create sheet if it doesn't exist
    worksheet = spreadsheet.get_worksheet(0)

    cell_list = worksheet.range('A1:A{0}'.format(len(balances) + 1))
    for index, cell in enumerate(cell_list):
        if index == 0:
            cell.value = 'Date'
        else:
            cell.value = balances[index - 1].date
    print('Writing date cells')
    worksheet.update_cells(cell_list)

    cell_list = worksheet.range('B1:B{0}'.format(len(balances) + 1))
    for index, cell in enumerate(cell_list):
        if index == 0:
            cell.value = 'Total Aim'
        else:
            cell.value = balances[index - 1].amount
    print('Writing amount cells')
    worksheet.update_cells(cell_list)
    # TODO: can we write just once?

    url = 'https://docs.google.com/spreadsheets/d/{0}/edit'.format(
        spreadsheet.id)
    print('Spreadsheet updated {0}'.format(url))


# TODO: call from init? I'd like to call command line with "moola"
if __name__ == '__main__':
    create_sheet_for_month()
