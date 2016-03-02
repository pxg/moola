from money import Money as BaseMoney


class Money(BaseMoney):

    def __init__(self, *args, **kwargs):
        """
        Call the super class constructor with the currency set to pounds
        """
        super().__init__(*(args[0], 'GBP'), **kwargs)

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
        self.day = int(day)
        self.amount = Money(amount)
        self.description = description

    def __repr__(self):
        return '<Transaction object ({}, {}, {})>'.format(
            self.day, self.amount, self.description)
