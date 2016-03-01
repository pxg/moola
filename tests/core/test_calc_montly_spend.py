from moola.core import _calc_monthly_spend, Money, Transaction


def test_calc_monthly_spend_just_balances():
    start_balance = Money(2500)
    end_balance = Money(500)

    assert _calc_monthly_spend(start_balance, end_balance) == Money(2000)


def test_calc_monthly_spend_decimal_balances():
    start_balance = Money(2500.99)
    end_balance = Money(500.99)

    monthly_spend = _calc_monthly_spend(start_balance, end_balance)

    # Rounded amounts needed for decimals to match exactly
    assert monthly_spend.rounded_amount == Money(2000).rounded_amount


def test_calc_monthly_spend_with_transaction():
    start_balance = Money(2500)
    end_balance = Money(500)
    transactions = [Transaction(2, -50, 'Broadband')]

    monthly_spend = _calc_monthly_spend(
        start_balance,
        end_balance,
        transactions)

    assert monthly_spend == Money(1950)


def test_calc_monthly_spend_with_decimal_transactions():
    start_balance = Money(2500)
    end_balance = Money(500)
    transactions = [
        Transaction(2, -9.99, 'Nexflix'),
        Transaction(2, -5.00, 'Spotify')]

    monthly_spend = _calc_monthly_spend(
        start_balance,
        end_balance,
        transactions)

    # Rounded amounts needed for decimals to match exactly
    assert monthly_spend.rounded_amount == Money(1985.01).rounded_amount
