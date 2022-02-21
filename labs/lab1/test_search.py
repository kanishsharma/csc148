"""CSC148 Lab 1

=== CSC148 Winter 2021 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module illustrates a simple unit test for our binary_search function.
"""
from search import binary_search


def test_search() -> None:
    """Simple test for binary_search."""
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 5) == 1


def test_single_item_list() -> None:
    """Test binary_search on a list with a single item"""
    assert binary_search([1], 2) == -1


def test_empty_list() -> None:
    """Test binary_search on an empty list"""
    assert binary_search([], 1) == -1


def test_second_half_list() -> None:
    """Test that binary_search ignores the second half of the list when t > mid
    """
    assert binary_search([1, 2, 3, 4, 5], 4) == 3

def test_near_middle_list() -> None:
    """Test that binary_search """





if __name__ == '__main__':
    import pytest

    pytest.main(['test_search.py'])
