from collections import namedtuple
from datetime import date
from mock import Mock

from moola.shell import _populate_cells
from moola.models import Money


def test_populate_cells_no_balances_correct_length():
    cells = [Mock(), Mock()]

    populated_cells = _populate_cells(cells, [])

    assert len(populated_cells) == 2


def test_populate_cells_no_balances_correct_headers():
    cells = [Mock(), Mock()]

    populated_cells = _populate_cells(cells, [])

    assert populated_cells[0].value == 'Date'
    assert populated_cells[1].value == 'Total Aim'


def test_populate_cells_one_balance_correct_length():
    cells = [Mock() for x in range(4)]
    Balance = namedtuple('Balance', 'date amount')
    balances = [Balance(date(2016, 3, 1), Money(500))]

    populated_cells = _populate_cells(cells, balances)

    assert len(populated_cells) == 4


def test_populate_cells_one_balance_correct_values():
    cells = [Mock() for x in range(4)]
    Balance = namedtuple('Balance', 'date amount')
    balances = [Balance(date(2016, 3, 1), Money(500))]

    populated_cells = _populate_cells(cells, balances)

    assert populated_cells[2].value == date(2016, 3, 1)
    assert populated_cells[3].value == Money(500)


def test_populate_cells_two_balances_correct_length():
    cells = [Mock() for x in range(6)]
    Balance = namedtuple('Balance', 'date amount')
    balances = [
        Balance(date(2016, 3, 1), Money(500)),
        Balance(date(2016, 3, 2), Money(450))]

    populated_cells = _populate_cells(cells, balances)

    assert len(populated_cells) == 6


def test_populate_cells_two_balances_correct_values():
    cells = [Mock() for x in range(6)]
    Balance = namedtuple('Balance', 'date amount')
    balances = [
        Balance(date(2016, 3, 1), Money(500)),
        Balance(date(2016, 3, 2), Money(450))]

    populated_cells = _populate_cells(cells, balances)

    assert populated_cells[2].value == date(2016, 3, 1)
    assert populated_cells[3].value == Money(500)
    assert populated_cells[4].value == date(2016, 3, 2)
    assert populated_cells[5].value == Money(450)
