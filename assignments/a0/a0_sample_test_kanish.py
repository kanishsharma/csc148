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


def complex_election_setup() -> Election:
    """"Set up a complex election with 5 ridings and 4 parties"""
    e = Election(date(2002, 2, 8))
    e.update_results('r1', 'ndp', 1234)
    e.update_results('r1', 'lib', 1345)
    e.update_results('r1', 'pc', 1456)
    e.update_results('r1', 'green', 3431)

    e.update_results('r2', 'ndp', 123)
    e.update_results('r2', 'lib', 134)
    e.update_results('r2', 'pc', 145)
    e.update_results('r2', 'green', 100)

    e.update_results('r3', 'ndp', 10)
    e.update_results('r3', 'lib', 20)
    e.update_results('r3', 'pc', 30)
    e.update_results('r3', 'green', 0)

    e.update_results('r4', 'ndp', 0)
    e.update_results('r4', 'lib', 134)
    e.update_results('r4', 'pc', 0)
    e.update_results('r4', 'green', 100)

    e.update_results('r5', 'ndp', 20)
    e.update_results('r5', 'lib', 40)
    e.update_results('r5', 'pc', 60)
    e.update_results('r5', 'green', 80)

    e.update_results('r6', 'ndp', 0)
    e.update_results('r6', 'lib', 0)
    e.update_results('r6', 'pc', 0)
    e.update_results('r6', 'green', 80)

    e.update_results('r7', 'ndp', 0)
    e.update_results('r7', 'lib', 0)
    e.update_results('r7', 'pc', 0)
    e.update_results('r7', 'green', 0)

    return e


def simple_jurisdiction_setup() -> Jurisdiction:
    """Set up a simple Jurisdiction with a single Election and one result."""
    j = Jurisdiction('Canada')
    res1 = StringIO(SHORT_FILE_CONTENTS)
    j.read_results(2000, 1, 2, res1)
    return j


def complex_jurisdiction_setup() -> Jurisdiction:
    """Set up a complex Jurisdiction with multiple elections and results"""
    j = Jurisdiction('Canada')
    e = Election(date(2002, 2, 8))
    e.update_results('r1', 'ndp', 1234)
    e.update_results('r1', 'lib', 1345)
    e.update_results('r1', 'pc', 1456)
    e.update_results('r1', 'green', 3431)
    e.update_results('r2', 'ndp', 123)
    e.update_results('r2', 'lib', 134)
    e.update_results('r2', 'pc', 145)
    e.update_results('r2', 'green', 100)
    j._elections[date(2002, 2, 8)] = e

    e1 = Election(date(2003, 2, 8))
    e1.update_results('r3', 'ndp', 10)
    e1.update_results('r3', 'lib', 20)
    e1.update_results('r3', 'pc', 30)
    e1.update_results('r3', 'green', 0)
    e1.update_results('r4', 'ndp', 0)
    e1.update_results('r4', 'lib', 134)
    e1.update_results('r4', 'pc', 0)
    e1.update_results('r4', 'green', 100)
    j._elections[date(2003, 2, 8)] = e1

    e2 = Election(date(2004, 2, 8))
    e2.update_results('r5', 'ndp', 20)
    e2.update_results('r5', 'lib', 40)
    e2.update_results('r5', 'pc', 60)
    e2.update_results('r5', 'green', 80)
    e2.update_results('r6', 'ndp', 0)
    e2.update_results('r6', 'lib', 0)
    e2.update_results('r6', 'pc', 0)
    e2.update_results('r6', 'green', 80)
    e2.update_results('r7', 'ndp', 0)
    e2.update_results('r7', 'lib', 0)
    e2.update_results('r7', 'pc', 0)
    e2.update_results('r7', 'green', 0)
    j._elections[date(2004, 2, 8)] = e2

    return j


def test_simple_election_ridings_recorded() -> None:
    """Test Election.ridings_recorded with a simple Election."""
    e = simple_election_setup()
    assert e.ridings_recorded() == ['r1', 'r2']


def test_ridings_recorded_complex() -> None:
    """Test Election.ridings_recorded with a complex Election"""
    e = complex_election_setup()
    assert e.ridings_recorded() == ['r1', 'r2', 'r3', 'r4', 'r5', 'r6']


def test_simple_election_results_for() -> None:
    """Test Election.results_for with a simple Election."""
    e = simple_election_setup()
    assert e.results_for('r1', 'ndp') == 1234


def test_simple_election_riding_winners() -> None:
    """Test Election.riding_winners with a simple Election."""
    e = simple_election_setup()
    assert e.riding_winners('r1') == ['pc']


def test_complex_election_riding_winners() -> None:
    """Test Election.riding_winners with a complex Election."""
    e = complex_election_setup()
    assert e.riding_winners('r1') == ['green'] and e.riding_winners('r2') == \
        ['pc'] and e.riding_winners('r3') == ['pc'] and e.riding_winners('r4') \
        == ['lib'] and e.riding_winners('r5') == ['green'] and \
        e.riding_winners('r6') == ['green']


def test_tied_riding_winners() -> None:
    """Test Election.riding_winners where multiple parties are tied initially"""
    e = Election(date(2008, 2, 8))
    e.update_results('r1', 'ndp', 1)
    e.update_results('r1', 'lib', 1)
    e.update_results('r1', 'pc', 2)
    e.update_results('r1', 'green', 2)

    assert e.riding_winners('r1') == ['pc', 'green']


def test_simple_election_popular_vote() -> None:
    """Test Election.popular_vote with a simple Election."""
    e = simple_election_setup()
    assert e.popular_vote() == {'ndp': 1534, 'lib': 1545, 'pc': 1556}


def test_simple_election_party_seats() -> None:
    """Test Election.party_seats with a simple Election."""
    e = simple_election_setup()
    assert e.party_seats() == {'ndp': 1, 'lib': 0, 'pc': 1}


def test_complex_election_party_seats() -> None:
    """Test Election.party_seats with a complex Election"""
    e = complex_election_setup()
    assert e.party_seats() == {'ndp': 0, 'lib': 1, 'pc': 2, 'green': 3}


def test_complex_election_election_winners() -> None:
    """Test Election.election_winners with a complex election """
    e = complex_election_setup()
    assert e.election_winners() == ['green']


def test_tied_election_winners() -> None:
    """Test Election.election_winners with a tied set of winners"""
    e = Election(date(2002, 2, 8))
    e.update_results('r1', 'ndp', 1234)
    e.update_results('r1', 'lib', 1345)
    e.update_results('r1', 'pc', 1456)
    e.update_results('r1', 'green', 3431)

    e.update_results('r2', 'ndp', 123)
    e.update_results('r2', 'lib', 134)
    e.update_results('r2', 'pc', 145)
    e.update_results('r2', 'green', 100)

    assert e.election_winners() == ['pc', 'green']


def test_one_party_one_riding_read_results() -> None:
    """Test Election.read_results with a file with a single line."""
    file = StringIO(SHORT_FILE_CONTENTS)
    e = Election(date(2012, 10, 30))
    e.read_results(file)
    assert e.popular_vote() == {'Liberal': 113}


def test_simple_jurisdiction_party_wins() -> None:
    """Test Jurisdiction.party_wins with a file with a single line. """
    j = simple_jurisdiction_setup()
    assert j.party_wins('Liberal') == [date(2000, 1, 2)]


def test_complex_jurisdiction_party_wins() -> None:
    """Test Jurisdiction.party_wins with a complex file"""
    j = complex_jurisdiction_setup()
    assert j.party_wins('green') == [date(2002, 2, 8), date(2004, 2, 8)]


def test_simple_jurisdiction_party_history() -> None:
    """Test Jurisdiction.party_history with a file with a single line."""
    j = simple_jurisdiction_setup()
    assert j.party_history('Liberal') == {date(2000, 1, 2): 1.0}


def test_complex_jurisdiction_party_history() -> None:
    """Test Jurisdiction.party_history with a complex file"""
    j = complex_jurisdiction_setup()
    assert j.party_history('green') == {date(2002, 2, 8): 0.4431475903614458,
                                        date(2003, 2, 8): 0.3401360544217687,
                                        date(2004, 2, 8): 0.5714285714285714}


def test_simple_jurisdiction_riding_changes() -> None:
    """Test Jurisdiction.riding_changes with two Elections."""
    j = simple_jurisdiction_setup()
    res2 = open('data/toronto-stpauls.csv')
    j.read_results(2004, 5, 15, res2)
    res2.close()
    assert j.riding_changes() == [({"St. Paul's"}, {"Toronto--St. Paul's"})]


def test_one_election_jurisdiction_riding_changes() -> None:
    """Test Jurisdiction.riding_changes with only one election """
    j = Jurisdiction('Canada')
    e = Election(date(2008, 2, 16))
    e.update_results('r1', 'ndp', 10)
    j._elections[date(2008, 2, 16)] = e
    assert j.riding_changes() == []


if __name__ == '__main__':
    import pytest
    pytest.main(['a0_sample_test_kanish.py'])
