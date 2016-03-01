from moola.core import Money


def test_money_class_addition():
    total = Money(14.99) + Money(5.00)

    assert total.rounded_amount == 19.99


def test_money_class_rounded_amount():
    a = Money(14.99)

    assert a.rounded_amount == 14.99


def test_money_class_rounded_amount_addition():
    total = Money(14.99) + Money(5.00)

    assert total.rounded_amount == 19.99
