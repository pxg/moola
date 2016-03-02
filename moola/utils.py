import calendar
from datetime import datetime


def get_spreadsheet_name(year, month):
    return '{} {}'.format(calendar.month_name[month], year)


def months_names():
    return ['Jan', 'Feb', 'March']


def current_month_number():
    return datetime.now().month


def current_year():
    return datetime.now().year
