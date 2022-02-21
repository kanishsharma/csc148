"""Testing: a basic example

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains a few simple unit tests for insert_after.
Note that in order to run this file on your own computer,
you need to have followed our CSC148 Software Guide and installed
all of the Python requirements for the course, including pytest.
"""
from insert import insert_after


def test_insert_after_at_front() -> None:
    """Test insert_after with one occurrence of n1 at the front of lst.
    """
    input_list = [0, 1, 2, 3]
    insert_after(input_list, 0, 99)
    expected = [0, 99, 1, 2, 3]
    assert input_list == expected

def test_insert_after_at_back() -> None:
    """Test insert_after with one occurrence of n1 at the end of the list"""
    input_list = [0, 1, 2, 3]
    input_after(input_list, 3, 99)
    expected = [0, 1, 2, 3, 99]
    assert input_list == expected

def test_


def test_length_list() -> None:
    """Test insert_after to see if the length of the returned list is n1
    values long"""
    input_list = [0, 1, 2, 3, 0]
    length_input = len(input_list)
    insert_after(input_list, 0, 0)
    length_output = len(input_list)
    assert length_output - length_input == 2


# HOMEWORK: Add more test cases to this file to have a more complete test suite.

def test_types() -> None:
    """Test that all the values in the returned list are the same as the ones
    in the original list"""
    input_list = [2, 4, 6, 8, 2]
    insert_after = [input_list, 2, 99]
    flag = False
    for item in input_list:
        if type(item) != int:
            flag = True
    assert flag is False


if __name__ == '__main__':
    import pytest

    pytest.main(['test_insert.py'])
