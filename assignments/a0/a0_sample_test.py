"""CSC148 Assignment 0: Sample tests

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Assignment 0.

Warning: This is an extremely incomplete set of tests! Add your own tests
to be confident that your code is correct.

Note: this file is to only help you; you will not submit it when you hand in
the assignment.

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) University of Toronto
"""
from datetime import date
from io import StringIO
from elections import Election, Jurisdiction

# A string representing one election result.
# StringIO will take the string below and make an object that we can pass to
# method read_results just like we would pass an open file to it.
# We use this in our testing below. You can use it in your own testing, but
# you do not have to.
SHORT_FILE_CONTENTS = 'header\n' + \
                      ','.join(['35090', '"St. Paul\'s"', '"St. Paul\'s"',
                                '" 1"', '"Toronto"', 'N', 'N', '""', '1',
                                '367', '"Bennett"', '""', '"Carolyn"',
                                '"Liberal"', '"Liberal"', 'Y', 'Y', '113'])


def simple_election_setup() -> Election:
    """Set up a simple Election with two ridings and three parties"""
    e = Election(date(2000, 2, 8))
    e.update_results('r1', 'ndp', 1234)
    e.update_results('r1', 'lib', 1345)
    e.update_results('r1', 'pc', 1456)

    e.update_results('r2', 'ndp', 300)
    e.update_results('r2', 'lib', 200)
    e.update_results('r2', 'pc', 100)

    return e


def simple_jurisdiction_setup() -> Jurisdiction:
    """Set up a simple Jurisdiction with a single Election and one result."""
    j = Jurisdiction('Canada')
    res1 = StringIO(SHORT_FILE_CONTENTS)
    j.read_results(2000, 1, 2, res1)
    return j

"""
Tests for Election.ridings_recorded
"""

def test_simple_election_ridings_recorded() -> None:
    """Test Election.ridings_recorded with a simple Election."""
    e = simple_election_setup()
    assert e.ridings_recorded() == ['r1', 'r2']

def test_empty_election_ridings_recorded() -> None:
    """Test Election.ridings_recorded with empty election"""
    e = Election(date(2020, 1, 1))
    assert e.ridings_recorded() == []

"""
Tests for Election.update_results
"""
def test_adding_update_results() -> None:
    """Test Election.update_results by adding ridings and parties that didn't exists"""
    e = Election(date(2020, 1, 1))
    assert e.ridings_recorded() == []
    e.update_results('r1', 'pc', 100)
    assert e.ridings_recorded() == ['r1']
    e.update_results('r1', 'ndp', 200)
    assert e.ridings_recorded() == ['r1']
    e.update_results('r2', 'ndp', 10)
    assert e.ridings_recorded() == ['r1', 'r2']

def test_adding_zero_votes() -> None:
    """Test Election.update_results by adding party with zero votes despite precondition"""
    e = Election(date(2020, 1, 1))
    e.update_results('r1', 'ndp', 0)
    assert e.ridings_recorded() == []
    assert e._parties == []
    assert e._ridings == []

"""
Tests for Election.read_results
"""
def test_one_party_one_riding_read_results() -> None:
    """Test Election.read_results with a file with a single line."""
    file = StringIO(SHORT_FILE_CONTENTS)
    e = Election(date(2012, 10, 30))
    e.read_results(file)
    assert e.popular_vote() == {'Liberal': 113}


def test_adding_new_riding_read_results() -> None:
    """Test Election.read_results by adding a new riding"""
    content = 'header\n' + \
                      ','.join(['35090', '"St. Paul\'s"', '"St. Paul\'s"',
                                '" 1"', '"Toronto"', 'N', 'N', '""', '1',
                                '367', '"Bennett"', '""', '"Carolyn"',
                                '"Liberal"', '"Liberal"', 'Y', 'Y', '113'])
    e = Election(date(2020, 1, 1))
    e.read_results(StringIO(content))
    assert e.ridings_recorded() == ['St. Paul\'s']
    assert e._parties == ['Liberal']
    assert e.popular_vote() == {'Liberal': 113}


def test_adding_zero_votes_read_results() -> None:
    """Test Election.read_results by reading a row with zero votes"""
    content = 'header\n' + \
                      ','.join(['35090', '"St. Paul\'s"', '"St. Paul\'s"',
                                '" 1"', '"Toronto"', 'N', 'N', '""', '1',
                                '367', '"Bennett"', '""', '"Carolyn"',
                                '"Liberal"', '"Liberal"', 'Y', 'Y', '0'])
    e = Election(date(2020, 1, 1))
    e.read_results(StringIO(content))
    assert e.ridings_recorded() == []
    assert e._parties == []


def test_adding_multiple_party_votes_read_results() -> None:
    """Test Election.read_results by updating the same party"""
    content1 = 'header\n' + \
                      ','.join(['35090', '"St. Paul\'s"', '"St. Paul\'s"',
                                '" 1"', '"Toronto"', 'N', 'N', '""', '1',
                                '367', '"Bennett"', '""', '"Carolyn"',
                                '"Liberal"', '"Liberal"', 'Y', 'Y', '10'])
    content2 = 'header\n' + \
                      ','.join(['35090', '"St. Paul\'s"', '"St. Paul\'s"',
                                '" 1"', '"Toronto"', 'N', 'N', '""', '1',
                                '367', '"Bennett"', '""', '"Carolyn"',
                                '"Liberal"', '"Liberal"', 'Y', 'Y', '20'])

    e = Election(date(2020, 1, 1))
    e.read_results(StringIO(content1))
    e.read_results(StringIO(content2))
    assert e.ridings_recorded() == ['St. Paul\'s']
    assert e._parties == ['Liberal']
    assert e.results_for('St. Paul\'s', 'Liberal') == 30

"""
Tests for Election.results_for
"""
def test_simple_election_results_for() -> None:
    """Test Election.results_for with a simple Election."""
    e = simple_election_setup()
    assert e.results_for('r1', 'ndp') == 1234

def test_empty_election_results_for() -> None:
    """Test Election.results_for with empty election"""
    e = Election(date(2020, 1, 1))
    assert e.results_for('r1', 'ndp') == None

def test_no_party_in_riding_results_for() -> None:
    """Test Election.results_for with a riding with votes but none from the party in question"""
    e = Election(date(2020, 1, 1))
    e.update_results('r1', 'ndp', 10)
    assert e.results_for('r1', 'pc') == None

"""
Tests for Election.riding_winners
"""

def test_simple_election_riding_winners() -> None:
    """Test Election.riding_winners with a simple Election."""
    e = simple_election_setup()
    assert e.riding_winners('r1') == ['pc']

def test_all_tied_riding_winners() -> None:
    """Test Election.riding_winners with all parties being tied in votes"""
    e = Election(date(2020, 1, 1))
    e.update_results('r1', 'lib', 50)
    e.update_results('r1', 'ndp', 50)
    e.update_results('r1', 'pc', 50)
    assert e.riding_winners('r1') == ['lib', 'ndp', 'pc']

def test_tie_riding_winners() -> None:
    """Test Election.riding_winners with two parties being tied in votes"""
    e = Election(date(2020, 1, 1))
    e.update_results('r1', 'lib', 100)
    e.update_results('r1', 'ndp', 100)
    e.update_results('r1', 'pc', 50)
    assert e.riding_winners('r1') == ['lib', 'ndp']

def test_one_party_riding_winners() -> None:
    """Test Election.riding_winners with only one party in the riding"""
    e = Election(date(2020, 1, 1))
    e.update_results('r1', 'lib', 100)
    assert e.riding_winners('r1') == ['lib']


"""
Tests for Election.popular_vote
"""

def test_simple_election_popular_vote() -> None:
    """Test Election.popular_vote with a simple Election."""
    e = simple_election_setup()
    assert e.popular_vote() == {'ndp': 1534, 'lib': 1545, 'pc': 1556}

def test_party_with_no_votes() -> None:
    """Test Election.popular_vote by adding a party with zero votes"""
    e = simple_election_setup()
    e.update_results('r1', 'abc', 0)
    assert e.popular_vote() == {'ndp': 1534, 'lib': 1545, 'pc': 1556}

"""
Tests for Election.party_seats
"""
def test_simple_election_party_seats() -> None:
    """Test Election.party_seats with a simple Election."""
    e = simple_election_setup()
    assert e.party_seats() == {'ndp': 1, 'lib': 0, 'pc': 1}

def test_riding_with_multiple_winners_party_seats() -> None:
    """Test Election.party_seats with a riding where there were multiple winners"""
    e = Election(date(2020, 1, 1))
    e.update_results('r1', 'ndp', 100)
    e.update_results('r1', 'lib', 100)
    e.update_results('r1', 'pc', 50)

    e.update_results('r2', 'ndp', 100)
    assert e.party_seats() == {'ndp': 1, 'lib': 0, 'pc': 0}

def test_election_with_no_winners_party_seats() -> None:
    """Test Election.party_seats with ridings where there are no winners"""
    e = Election(date(2020, 1, 1))
    e.update_results('r1', 'ndp', 100)
    e.update_results('r1', 'lib', 100)

    e.update_results('r2', 'pc', 100)
    e.update_results('r2', 'ndp', 100)
    assert e.party_seats() == {'ndp': 0, 'lib': 0, 'pc': 0}

def test_added_party_zero_votes_party_seats() -> None:
    """Test Election.party_seats after adding party with zero votes"""
    e = Election(date(2020, 1, 1))
    e.update_results('r1', 'ndp', 100)
    e.update_results('r1', 'lib', 1)
    e.update_results('r1', 'pc', 0)
    assert e.party_seats() == {'ndp': 1, 'lib': 0}

def test_empty_party_seats() -> None:
    """Test Election.election_winners with empty election"""
    e = Election(date(2020, 1, 1))
    assert e.party_seats() == {}

"""
Tests for Election.election_winners
"""
def test_simple_election_winners() -> None:
    """Test Election.election_winners with simple election"""
    e = simple_election_setup()
    assert e.election_winners() == ['ndp', 'pc']

# def test_no_winners_election_winners() -> None:
#     """Test Election.election_winners with election where no seats were held by any party"""
#     e = Election(date(2020, 1, 1))
#     e.update_results('r1', 'ndp', 100)
#     e.update_results('r1', 'lib', 100)

#     e.update_results('r2', 'pc', 100)
#     e.update_results('r2', 'ndp', 100)
#     assert e.election_winners() == ['ndp', 'lib', 'pc']

# def test_empty_election_winners() -> None:
#     """Test Election.election_winners with empty election"""
#     e = Election(date(2020, 1, 1))
#     assert e.election_winners() == []





def test_simple_jurisdiction_party_wins() -> None:
    """Test Jurisdiction.party_wins with a file with a single line. """
    j = simple_jurisdiction_setup()
    assert j.party_wins('Liberal') == [date(2000, 1, 2)]


def test_simple_jurisdiction_party_history() -> None:
    """Test Jurisdiction.party_history with a file with a single line."""
    j = simple_jurisdiction_setup()
    assert j.party_history('Liberal') == {date(2000, 1, 2): 1.0}


def test_simple_jurisdiction_riding_changes() -> None:
    """Test Jurisdiction.riding_changes with two Elections."""
    j = simple_jurisdiction_setup()
    res2 = open('data/toronto-stpauls.csv')
    j.read_results(2004, 5, 15, res2)
    res2.close()
    assert j.riding_changes() == [({"St. Paul's"}, {"Toronto--St. Paul's"})]


def test_one_riding_riding_changes() -> None:
    """Test Jurisdiction.riding_changes with only one election"""
    j = Jurisdiction('Canada')
    e = Election(date(2020, 1, 1))

    e.update_results('r1', 'ndp', 10)
    j._elections = {date(2020, 1, 1): e}
    assert j.riding_changes() == []


if __name__ == '__main__':
    import pytest
    pytest.main(['a0_sample_test.py'])
