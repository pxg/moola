from calendar import monthrange
from datetime import datetime


def create_sheet_for_month():
    """
    Prompt user for required values then create Google spreadsheet with amounts
    for month
    """
    pass


def get_amounts_for_month(year, month, start_balance, end_balance):
    amounts = []
    num_days = monthrange(year, month)[1]
    for day in range(1, num_days + 1):
        date = datetime(year, month, day)
        # TOOD: use named tuple
        amounts.append((date, 2500))
    return amounts
