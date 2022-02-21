"""Prep 2 Synthesize Sample Tests

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: David Liu, Diane Horton, and Sophia Huynh

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 David Liu, Diane Horton, and Sophia Huynh

=== Module Description ===
This module contains sample tests for Prep 2.
Complete the TODO in this file.
There is also a task inside prep2.py.
Make sure to look at that file and complete the TODO there as well.

We suggest you also add your own tests to practice writing tests and
to be confident your code is correct.

When writing a test case, make sure you create a new function, with its
name starting with "test_". For example:

def test_my_test_case():
    # Your test here

All test cases must have different names (i.e. you cannot have two tests
named test_my_test_case).
"""
from hypothesis import given
from hypothesis.strategies import integers
from prep2 import Spinner, Tweet
from datetime import date


################################################################################
# Part 3
# In this part, you will be fixing a bug within a provided test.
################################################################################
def test_buggy_consecutive_spins() -> None:
    """Test consecutive spins of your Spinner class.
    This test case has a bug in it."""

    s = Spinner(6)  # Do not change this line
    s.spin(2)  # Do not change this line
    expected_value1 = 2
    assert s.position == expected_value1  # Do not change this line
    s.spin(2)  # Do not change this line
    expected_value2 = 4
    assert s.position == expected_value2  # Do not change this line


################################################################################
# Sample test cases below
#
# Use the below test cases as an example for writing your own test cases,
# and as a start to testing your prep2.py code.
#
# The self-test on MarkUs runs the tests below, along with a few others.
# Make sure you run the self-test after submitting your code!
#
# WARNING: THIS IS CURRENTLY AN EXTREMELY INCOMPLETE SET OF TESTS!
# We will test your code on a much more thorough set of tests!
################################################################################
def test_doctest() -> None:
    """Test the given doctest in the Spinner class docstring."""
    spinner = Spinner(8)

    spinner.spin(4)
    assert spinner.position == 4

    spinner.spin(2)
    assert spinner.position == 6

    spinner.spin(2)
    assert spinner.position == 0


def test_random_spin() -> None:
    """Tests two random spins to ensure they don't go over spinner slot size"""
    spinner = Spinner(6)

    spinner.spin_randomly()
    spinner.spin_randomly()

    assert spinner.position < 6


def test_boundary_spin() -> None:
    """Tests Spinner.spin at the boundary of a spinner's slot size"""

    spinner = Spinner(6)

    spinner.spin(5)
    assert spinner.position == 5

    spinner.spin(1)
    assert spinner.position == 0


def test_greater_slot_value_spin() -> None:
    """Test that a force value greater than the slots in a spinner will return
    the overlapped value of a spinner"""

    spinner = Spinner(6)

    spinner.spin(7)
    assert spinner.position == 1

def test_spin_randomly_in_range_1() -> None:
    """Test that spin_randomly will always return position 0 when asked to spin
    randomly with self.slots = 1"""

    spinner = Spinner(1)

    spinner.spin_randomly()
    assert spinner.position == 0


# This is a hypothesis test; it generates a random integer to use as input,
# so that we don't need to hard-code a specific number of slots in the test.
# For more information on hypothesis (one of the testing libraries we're using),
# please see
# https://www.teach.cs.toronto.edu/~csc148h/winter/notes/testing/hypothesis.html
@given(slots=integers(min_value=1))
def test_new_spinner_position(slots: int) -> None:
    """Test that the position of a new spinner is always 0."""
    spinner = Spinner(slots)
    assert spinner.position == 0


def test_unlike_doctest() -> None:
    """Test the given doctest in the unlike method of Tweet."""
    tweet = Tweet('Sophia', date(2021, 1, 1), 'Happy new year!')
    tweet.like(5)
    assert tweet.likes == 5
    tweet.unlike()
    assert tweet.likes == 4


def test_unlike_near_1() -> None:
    """Test unlike when the value of like is barely greater than 1"""
    tweet = Tweet('John', date(2021, 1, 1), 'New Years Resolution!')
    tweet.like(2)
    assert tweet.likes == 2
    tweet.unlike()
    assert tweet.likes == 1


if __name__ == '__main__':
    import pytest

    pytest.main(['prep2_starter_tests.py'])
