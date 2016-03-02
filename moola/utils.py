import calendar


def get_spreadsheet_name(year, month):
    return '{} {}'.format(calendar.month_name[month], year)
