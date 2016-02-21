from calendar import monthrange
from datetime import datetime
from collections import namedtuple


def create_sheet_for_month():
    """
    Prompt user for required values then create Google spreadsheet with amounts
    for month
    """
    pass


# TOOD: rename get daily_balances for month
def get_amounts_for_month(year, month, start_balance, end_balance):
    daily_balances = []
    Balance = namedtuple('Balance', 'date amount')
    # TODO: break into function
    num_days = monthrange(year, month)[1]

    for day in range(1, num_days + 1):
        date = datetime(year, month, day)
        date_balance = Balance(date, 2500)
        daily_balances.append(date_balance)
    return daily_balances
