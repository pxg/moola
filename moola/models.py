from money import Money as BaseMoney
from .utils import clean_amount


class Money(BaseMoney):

    def __init__(self, amount, *args, **kwargs):
        """
        Call the super class constructor with the currency set to pounds
        """
        super().__init__(amount, currency='GBP', **kwargs)

    @property
    def rounded_amount(self):
        """
        Helper method so we don't need to keep casting to decimal. Makes tests
        easier to read.
        """
        amount = round(self.amount, 2)
        return int(amount * 100) / 100


class Transaction:

    def __init__(self, day, amount, description):
        self.amount = Money(clean_amount(amount))
        self.day = int(day)
        self.description = description

    def __repr__(self):
        return '<Transaction object ({}, {}, {})>'.format(
            self.day, self.amount, self.description)
