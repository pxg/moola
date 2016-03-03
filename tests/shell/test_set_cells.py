from collections import namedtuple
from datetime import date
from mock import Mock

from moola.shell import _next_cell_set_value, _set_cells
from moola.models import Money


def test_next_cell_set_value_removes_item_from_cells():
    cells = [Mock()]

    _next_cell_set_value('asdf', cells)

    assert len(cells) == 0


def test_next_cell_set_value_sets_correct_cell_value():
    cells = [Mock()]

    cell = _next_cell_set_value('asdf', cells)

    assert cell.value == 'asdf'


def test_set_cells_no_balances_correct_length():
    cells = [Mock(), Mock()]

    set_cells = _set_cells(cells, [])

    assert len(set_cells) == 2


def test_set_cells_no_balances_correct_headers():
    cells = [Mock(), Mock()]

    set_cells = _set_cells(cells, [])

    assert set_cells[0].value == 'Date'
    assert set_cells[1].value == 'Total Aim'


def test_set_cells_one_balance_correct_length():
    cells = [Mock() for x in range(4)]
    Balance = namedtuple('Balance', 'date amount')
    balances = [Balance(date(2016, 3, 1), Money(500))]

    set_cells = _set_cells(cells, balances)

    assert len(set_cells) == 4


def test_set_cells_one_balance_correct_values():
    cells = [Mock() for x in range(4)]
    Balance = namedtuple('Balance', 'date amount')
    balances = [Balance(date(2016, 3, 1), Money(500))]

    set_cells = _set_cells(cells, balances)

    assert set_cells[2].value == date(2016, 3, 1)
    assert set_cells[3].value == Money(500)


def test_set_cells_two_balances_correct_length():
    cells = [Mock() for x in range(6)]
    Balance = namedtuple('Balance', 'date amount')
    balances = [
        Balance(date(2016, 3, 1), Money(500)),
        Balance(date(2016, 3, 2), Money(450))]

    set_cells = _set_cells(cells, balances)

    assert len(set_cells) == 6


def test_set_cells_two_balances_correct_values():
    cells = [Mock() for x in range(6)]
    Balance = namedtuple('Balance', 'date amount')
    balances = [
        Balance(date(2016, 3, 1), Money(500)),
        Balance(date(2016, 3, 2), Money(450))]

    set_cells = _set_cells(cells, balances)

    assert set_cells[2].value == date(2016, 3, 1)
    assert set_cells[3].value == Money(500)
    assert set_cells[4].value == date(2016, 3, 2)
    assert set_cells[5].value == Money(450)
