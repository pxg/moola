import json

import click
import gspread
import sys
from click import Choice
from gspread.exceptions import WorksheetNotFound
from oauth2client.client import SignedJwtAssertionCredentials

from .core import daily_balances_for_month, Transaction
from .utils import (
    current_month_number,
    current_year,
    get_spreadsheet_name,
    months_names)


@click.command()
@click.option(
    '--year', default=current_year(), prompt='Year to use')
@click.option(
    '--month', default=current_month_number(), prompt='Number of month to use',
    type=Choice(months_names()))
def create_sheet_for_month(year, month):
    """
    Prompt user for required values then create Google spreadsheet with amounts
    for month
    """
    # year, month, start, end = _prompt_user_for_inputs()
    print(year)
    print(month)
    # TODO: add start/end balances
    # TODO: change month into month_number. utils
    sys.exit()

    spreadsheet = _get_google_spreadsheet()
    transactions = _get_monthly_transactions(spreadsheet)

    balances = daily_balances_for_month(
        year,
        month,
        start,
        end,
        transactions)

    _write_balances_to_spreadsheet(spreadsheet, balances, year, month)


# TODO: tests
def _prompt_user_for_inputs():
    # TODO: prompt user for month, year, start and end balance
    # TODO: can this be tested easily
    # return 2016, 3, 2500, 500
    return 2016, 3, 1345.22 + 100 - 12.12, -654.78


def _get_monthly_transactions(spreadsheet):
    """
    Get monthly transactions from Google spreadsheet
    """
    print('Reading transactions data')
    worksheet = spreadsheet.worksheet('transactions')
    transaction_data_with_headers = worksheet.get_all_values()
    transaction_data = transaction_data_with_headers[1:]
    return [Transaction(*row) for row in transaction_data]


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
    return gc.open('Money')


# TODO: tests. Consider splitting or returning cell values first
def _write_balances_to_spreadsheet(spreadsheet, balances, year, month):
    name = get_spreadsheet_name(year, month)
    print('Worksheet name {}'.format(name))
    try:
        worksheet = spreadsheet.worksheet(name)
    except WorksheetNotFound:
        print('Not found creating worksheet')
        # TODO: can we make it the most recent spreadsheet on the tabs?
        worksheet = spreadsheet.add_worksheet(title=name, rows='32', cols='7')

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
