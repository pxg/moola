from calendar import monthrange


def create_sheet_for_month():
    """
    Prompt user for required values then create Google spreadsheet with amounts
    for month
    """
    pass


def get_amounts_for_month(year, month):
    num_days = monthrange(year, month)[1]
    return list(range(num_days))
