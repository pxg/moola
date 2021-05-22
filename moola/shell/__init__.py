import os

import click

from .monzo import _get_current_balance
from .gsheets import (
    _get_google_spreadsheet,
    _get_monthly_transactions,
    _print_spreadsheet_url,
    _write_balances_to_spreadsheet,
    _write_monzo_balances_to_spreadsheet)
from ..core import daily_balances_for_month
from ..utils import (
    current_month_number,
    current_year)


@click.command()
@click.option(
    '--environment',
    default='production',
    prompt='Spreadsheet to use',
    type=click.Choice(['development', 'test', 'production']))
@click.option(
    '--year',
    default=current_year(),
    prompt='Year to use')
@click.option(
    '--month',
    default=current_month_number(),
    prompt='Number of month to use (1=Jan, 2=Feb, etc)',
    type=click.IntRange(1, 12))
@click.option('--start', default=2500.00, prompt='Start Balance')
@click.option('--end', default=500.00, prompt='End Balance')
def create_sheet_for_month(year, month, start, end, environment):
    """
    Prompt user for required values then create Google spreadsheet with amounts
    for month
    """
    # TODO: validate year values here, could be any integer
    if environment == 'production':
        name = 'Money 2021'
    elif environment == 'test':
        name = 'Money test'
    else:
        name = 'Money dev'

    spreadsheet = _get_google_spreadsheet(name)
    transactions = _get_monthly_transactions(spreadsheet)

    balances = daily_balances_for_month(
        year,
        month,
        start,
        end,
        transactions)

    worksheet = _write_balances_to_spreadsheet(
        spreadsheet,
        balances,
        year,
        month)
    _print_spreadsheet_url(spreadsheet)
    return worksheet


def get_monzo_balance():
    """
    Get balance from Monzo and write to Google Sheet
    """
    balance = _get_current_balance(
        account_id=os.environ.get('MONZO_ACCOUNT_ID'),
        access_token=os.environ.get('MONZO_ACCESS_TOKEN'))
    spreadsheet = _get_google_spreadsheet('Money 2021')
    _write_monzo_balances_to_spreadsheet(spreadsheet, balance)
    _print_spreadsheet_url(spreadsheet)
