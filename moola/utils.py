import calendar
from datetime import datetime


def current_month_number():
    """
    Returns list of strings as click requires this
    """
    return int(datetime.now().month)


def current_year():
    return datetime.now().year


def get_spreadsheet_name(year, month):
    return '{} {}'.format(calendar.month_name[month], year)
