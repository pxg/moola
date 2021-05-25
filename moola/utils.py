import calendar
from datetime import datetime


def clean_amount(amount):
    """
    Strip potential dodgy characters from amount
    """
    return "".join([c for c in str(amount) if c in "1234567890.-"])


def current_month_number():
    return datetime.now().month


def current_year():
    return datetime.now().year


def current_day():
    return datetime.now().day


def get_worksheet_name(year, month):
    return "{} {}".format(calendar.month_name[month], year)
