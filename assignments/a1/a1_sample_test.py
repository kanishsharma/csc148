"""CSC148 Assignment 1: Sample tests

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
from typing import Set, Tuple, List


from a1 import *

# A string representing a simple 4 by 4 game board.
# We use this in one of the tests below. You can use it in your own testing, but
# you do not have to.
SIMPLE_BOARD_STRING = 'P-B-\n-BRB\n--BB\n-C--'
COMPLEX_BOARD_STRING = '-P-B-O\n-R-@O\n-----\nR-COR'

def simple_board_setup() -> GameBoard:
    """Set up a simple game board"""
    b = GameBoard(4, 4)
    b.setup_from_grid(SIMPLE_BOARD_STRING)
    return b


def complex_board_setup() -> GameBoard:
    """Set up a complex game board"""
    b = GameBoard(5, 4)
    b.setup_from_grid(COMPLEX_BOARD_STRING)
    return b 

def complex_bin_setup() -> GameBoard:
    """Set up 10x10 board with a lot of bins"""
    b = GameBoard(10,10)
    bin_coords = {
        (0,1), (0,2), (0,3), 
        (1,0), (1,1), (1,3), (1,4), (1,5), 
        (2,1), (2,2), (2,5),
        (3,0), (3,2), (3,5),
        (4,0), (4,1), (4,3), (4,5),
        (5,1), (5,5),
        (6,3), (6,4), (6,5), (6,6),
        (7,2), (7,5), (7,6),
        (8,3), (8,4), (8,5)
    }
    for (y, x) in bin_coords:
        RecyclingBin(b, x, y)
    return b


"""
Tests for GameBoard.place_character
"""

def test_simple_place_character() -> None:
    """Test GameBoard.place_character by placing a single Raccoon."""
    b = GameBoard(3, 2)
    r = Raccoon(b, 1, 1)
    assert b.at(1, 1)[0] == r  # requires GameBoard.at be implemented to work

def test_complex_place_character() -> None:
    """Test GameBoard.place_character on multiple characters, with two on the same tile"""
    b = GameBoard(4, 3)
    r1 = Raccoon(b, 1, 1)
    r2 = Raccoon(b, 2, 2)
    r3 = Raccoon(b, 2, 2)
    r4 = Raccoon(b, 3, 2)
    assert b.at(1,1)[0] == r1
    assert r2 in b.at(2, 2)
    assert r3 in b.at(2,2)
    assert b.at(3, 2)[0] == r4
    #Arguably not a test case for r2 and r3 because there's a precondition - should change to amend that movement
    
def test_multiple_bin_place_character() -> None:
    """Test Gameboard.place_character for garbage bin and raccoon characters"""
    b = GameBoard(4, 4)
    g1 = GarbageCan(b, 1, 1, False)
    g2 = GarbageCan(b, 1, 2, False)
    r1 = Raccoon(b, 1, 1)
    r2 = Raccoon(b, 1, 2)
    assert b.at(1,1)[0] == g1 and b.at(1,1)[1] == r1 and b.at(1, 2)[0] == g2 and b.at(1, 2)[1] == r2
    
"""
Tests for GameBoard.at
"""

def test_simple_at() -> None:
    """Test GameBoard.at on docstring example"""
    b = GameBoard(3, 2)
    r = Raccoon(b, 1, 1)
    assert b.at(1, 1)[0] == r
    p = Player(b, 0, 1)
    assert b.at(0, 1)[0] == p

def test_no_at() -> None:
    """Test GameBoard.at where there are no items on the board"""
    b = GameBoard(2, 2)
    assert b.at(1, 1) == []

def test_out_of_bounds_at() -> None:
    """Test GameBoard.at where the coordinates are out of bounds"""
    b = GameBoard(1, 1)
    assert b.at(2, 3) == []



"""
Tests for GameBoard.to_grid()
"""

def test_simple_grid() -> None:
    """Tests GameBoard.to_grid() for a simple setup"""
    b = GameBoard(2, 2)
    p = Player(b, 0, 0)
    r = Raccoon(b, 1, 0)
    bin = GarbageCan(b, 1, 1, False)
    assert b.to_grid() == [['P', 'R'], ['-', 'O']]

def test_complex_grid() -> None:
    """Tests GameBoard.to_grid() with more characters and a larger board"""
    b = GameBoard(5, 4)
    p = Player(b, 1, 0)
    s = SmartRaccoon(b, 1, 1)
    r = Raccoon(b, 3, 2)
    g = GarbageCan(b, 3, 2, False)
    g1 = GarbageCan(b, 4, 3, False)
    assert b.to_grid() == [['-', 'P', '-', '-', '-'],['-', 'S', '-', '-', '-' ],['-', '-', '-', '@', '-'],['-', '-', '-', '-', 'O']]

"""
Tests for GameBoard.__str__
"""

def test_simple_str() -> None:
    """Test GameBoard.__str__ for the simple board in SIMPLE_BOARD_STRING."""
    b = simple_board_setup()
    assert str(b) == 'P-B-\n-BRB\n--BB\n-C--'

"""
Tests for GameBoard.check_game_end
"""

def test_simple_check_game_end() -> None:
    """Test GameBoard.check_game_end on the docstring example"""
    b = GameBoard(3, 2)
    Raccoon(b, 1, 0)
    Player(b, 0, 0)
    RecyclingBin(b, 1, 1)
    assert b.check_game_end() is None
    assert not b.ended
    RecyclingBin(b, 2, 0)
    score = b.check_game_end()
    assert b.ended
    assert score == 11  # will only pass this last one when done Task 5.

def test_complex_check_game_end() -> None:
    """Test GameBoard.check_game_end on complex bin board"""
    b = complex_bin_setup()
    Raccoon(b, 2, 1)
    Raccoon(b, 1, 3)
    Raccoon(b, 3, 7)
    assert b.check_game_end() is None
    assert not b.ended
    Raccoon(b, 4, 7)
    assert b.check_game_end() == 64
    assert b.ended
    r1 = Raccoon(b, 2, 4)
    # Raccoon(b, 6, 5)
    g1 = GarbageCan(b, 2, 5, True)
    assert not r1.check_trapped()
    assert b.check_game_end() is None
    assert not b.ended
    g1.locked = False
    assert b.check_game_end() is None
    assert not b.ended
    Raccoon(b, 2, 5).inside_can = True
    assert r1.check_trapped()
    assert b.check_game_end() == 74
    assert b.ended

def test_empty_board_check_game_end() -> None:
    """Test GameBoard.check_game_end on a board with no raccoons"""
    b = GameBoard(5,5)
    assert b.check_game_end() == 0
    assert b.ended
    RecyclingBin(b,1,1)
    RecyclingBin(b,1,2)
    RecyclingBin(b,1,3)
    RecyclingBin(b,4,4)
    assert b.check_game_end() == 3
    assert b.ended

def test_single_square_check_game_end() -> None:
    b = GameBoard(1,1)
    assert b.check_game_end() == 0
    assert b.ended
    Raccoon(b, 0, 0)
    assert b.check_game_end() == 10
    assert b.ended

    b = GameBoard(1,1)
    RecyclingBin(b, 0, 0)
    assert b.check_game_end() == 1
    assert b.ended

def test_encircled_raccoon_check_game_end() -> None:
    """Test GameBoard.check_game_end on board with raccoons surrounded by other raccoons encircled by recycling bins"""
    b = GameBoard(5,5)
    r1 = Raccoon(b, 2, 2)

    Raccoon(b, 2, 1)
    Raccoon(b, 3, 2)
    Raccoon(b, 2, 3)
    Raccoon(b, 1, 2)
    assert r1.check_trapped()
    RecyclingBin(b, 2, 0)
    RecyclingBin(b, 3, 1)
    RecyclingBin(b, 4, 2)
    RecyclingBin(b, 3, 3)
    RecyclingBin(b, 2, 4)
    RecyclingBin(b, 1, 3)
    RecyclingBin(b, 0, 2)
    RecyclingBin(b, 1, 1)
    assert b.check_game_end() == 51
    GarbageCan(b, 2, 2, False)
    r1.inside_can = True
    assert r1.inside_can
    assert not r1.check_trapped()
    assert b.check_game_end() == 41

def test_more_encircled_raccoon_check_game_end() -> None:
    """Test GameBoard.check_game_end on board with raccoons surrounded by other raccoons encircled by raccoons in recycling bins"""
    b = GameBoard(5,5)
    r1 = Raccoon(b, 2, 2)

    Raccoon(b, 2, 1)
    Raccoon(b, 3, 2)
    Raccoon(b, 2, 3)
    Raccoon(b, 1, 2)
    assert r1.check_trapped()
    GarbageCan(b, 2, 0, False)
    GarbageCan(b, 3, 1, False)
    GarbageCan(b, 4, 2, False)
    GarbageCan(b, 3, 3, False)
    GarbageCan(b, 2, 4, False)
    GarbageCan(b, 1, 3, False)
    GarbageCan(b, 0, 2, False)
    GarbageCan(b, 1, 1, False)
    Raccoon(b, 2, 0).inside_can = True
    Raccoon(b, 3, 1).inside_can = True
    Raccoon(b, 4, 2).inside_can = True
    Raccoon(b, 3, 3).inside_can = True
    Raccoon(b, 2, 4).inside_can = True
    Raccoon(b, 1, 3).inside_can = True
    Raccoon(b, 0, 2).inside_can = True
    Raccoon(b, 1, 1).inside_can = True
    assert b.check_game_end() == 50
    GarbageCan(b, 2, 2, False)
    r1.inside_can = True
    assert not r1.check_trapped()
    assert b.check_game_end() == 40

def test_raccoon_filled_check_game_end() -> None:
    """Test GameBoard.check_game_end on board filled with raccoons"""
    b = GameBoard(2,2)
    Raccoon(b, 0, 0)
    Raccoon(b, 0, 1)
    Raccoon(b, 1, 0)
    assert b.check_game_end() is None
    Raccoon(b, 1, 1)
    assert b.check_game_end() == 40

def test_raccoon_in_cans_filled_check_game_end() -> None:
    """Test GameBoard.check_game_end on board filled with raccoons, with all of the being in cans"""
    for i in range(1, 10):
        b = GameBoard(i, i)
        for x in range(i):
            for y in range(i):
                Raccoon(b, x, y)
        assert b.check_game_end() == 10 * (i ** 2)
    for i in range(1, 10):
        b = GameBoard(i, i)
        for x in range(i):
            for y in range(i):
                Raccoon(b, x, y).inside_can = True
                GarbageCan(b, x, y, False)
        assert b.check_game_end() == 0

def test_raccoon_with_open_cans_check_game_end() -> None:
    """Test GameBoard.check_game_end on board with Raccoon surrounded by lockedgarbagecans"""
    b = GameBoard(3,3)
    Raccoon(b, 1, 1)
    GarbageCan(b, 1, 0, True)
    GarbageCan(b, 0, 1, True)
    GarbageCan(b, 2, 1, True)
    GarbageCan(b, 1, 2, True)
    print(b)
    assert b.check_game_end() is None
    Raccoon(b, 1, 0).inside_can = True
    Raccoon(b, 0, 1).inside_can = True
    Raccoon(b, 2, 1).inside_can = True
    assert b.check_game_end() is None
    Raccoon(b, 1, 2).inside_can = True
    assert b.check_game_end() == 10

def test_raccoon_with_every_character() -> None:
    """Test GameBoard.check_game_end on raccoons next to every type of character"""
    b = GameBoard(2, 1)
    r = Raccoon(b, 0, 0)
    assert not r.check_trapped() 
    assert b.check_game_end() is None

    b = GameBoard(2, 1)
    r = Raccoon(b, 0, 0)
    RecyclingBin(b, 1, 0)
    assert r.check_trapped() 
    assert b.check_game_end() == 11

    b = GameBoard(2, 1)
    r = Raccoon(b, 0, 0)
    Player(b, 1, 0)
    assert r.check_trapped() 
    assert b.check_game_end() == 10

    b = GameBoard(2, 1)
    r = Raccoon(b, 0, 0)
    Raccoon(b, 1, 0)
    assert r.check_trapped() 
    assert b.check_game_end() == 20

    b = GameBoard(2, 1)
    r = Raccoon(b, 0, 0)
    SmartRaccoon(b, 1, 0)
    assert r.check_trapped() 
    assert b.check_game_end() == 20

    b = GameBoard(2, 1)
    r = Raccoon(b, 0, 0)
    GarbageCan(b, 1, 0, True)
    assert not r.check_trapped() 
    assert b.check_game_end() is None


"""
Tests for GameBoard.adjacent_bin_score
"""

def test_simple_adjacent_bin_score() -> None:
    """Test GameBoard.adjacent_bin_score on the docstring example"""
    b = GameBoard(3, 3)
    RecyclingBin(b, 1, 1)
    RecyclingBin(b, 0, 0)
    RecyclingBin(b, 2, 2)
    assert b.adjacent_bin_score() == 1
    RecyclingBin(b, 2, 1)
    assert b.adjacent_bin_score() == 3
    RecyclingBin(b, 0, 1)
    assert b.adjacent_bin_score() == 5

def test_simple_board_adjacent_bin_score() -> None:
    b = simple_board_setup()
    assert b.adjacent_bin_score() == 3

def test_complex_board_adjacent_bin_score() -> None:
    b = complex_bin_setup()
    Raccoon(b, 2, 1)
    Raccoon(b, 2, 4)
    GarbageCan(b, 6, 1, False)
    GarbageCan(b, 6, 2, False)
    Raccoon(b, 6, 2)
    assert b.adjacent_bin_score() == 24

def test_empty_board_adjacent_bin_score() -> None:
    """Test GameBoard.adjacent_bin_score on a board with no bins"""
    b = GameBoard(4,4)
    Raccoon(b, 1, 1)
    assert b.adjacent_bin_score() == 0

def test_full_board_adjacent_bin_score() -> None:
    """Test GameBoard.adjacent_bin_score on a board full with bins"""
    b = GameBoard(4,4)
    for i in range(4):
        for j in range(4):
            RecyclingBin(b, i, j)
    assert b.adjacent_bin_score() == 16

def test_circular_cluster_adjacent_bin_score() -> None:
    """Test GameBoard.adjacent_bin_score on a board with a loop cluster"""
    b = GameBoard(10,10)
    for i in range(4,7):
        for j in range(3, 6):
            if i != 5 or j != 4:
                RecyclingBin(b, i, j)
    assert b.adjacent_bin_score() == 8

def test_block_cluster_adjacent_bin_score() -> None:
    """Test GameBoard.adjacent_bin_score various boards with a nxm block cluster of bins"""
    for n in range(1,8):
        for m in range(1, 8):
            b = GameBoard(10, 10)
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    RecyclingBin(b, i, j)
            assert b.adjacent_bin_score() == n * m

def test_singleton_bins_adjacent_bin_score() -> None:
    """Test GameBoard.adjacent_bin_score on board where every even square has a bin"""
    b = GameBoard(10,10)
    for i in range(10):
        for j in range(10):
            if i % 2 == 0 and j % 2 == 0:
                RecyclingBin(b, i, j)
    assert b.adjacent_bin_score() == 1

def test_random_arrangement_adjacent_bin_score() -> None:
    """Test GameBoard.adjacent_bin_score on board with a pregenerated bin arrangement"""
    b = complex_bin_setup()
    assert b.adjacent_bin_score() == 24

def test_equal_blocks() -> None:
    """Test GameBoard.adjacent_bin_score on board where multiple clusters of the same size"""
    b = GameBoard(10,10)
    bin_coords = {
        (1,1), (1,2), (2,2), (3,2), (4,2),
        (0,6), (1,6), (2,6), (3,6), (4,6),
        (10,0), (10,1), (10,2), (10,3), (10,4)
    }
    for (y, x) in bin_coords:
        RecyclingBin(b, x, y)
    assert b.adjacent_bin_score() == 5

# Tests for GameBoard._count_adjacent
def helper_count_from_all_heads(b: Set[Tuple[int]], expected: int, _: GameBoard) -> bool:
    """Helper function that runs _count_adjacent on every bin in b where b contains one
    contiguous bin cluster
    """
    for square in b:
        if _._count_adjacent(square, b.difference({square})) != expected:
            return False
    return True

def test_simple_count_adjacent() -> None:
    """Test GameBoard._count_adjacent with basic, 1d array examples"""
    _ = GameBoard(10, 1)
    b = {(0,1), (0,2), (0,3), (0, 5)}
    assert _._count_adjacent((0,1), b.difference({(0,1)})) == 3
    assert _._count_adjacent((0,2), b.difference({(0,2)})) == 3
    assert _._count_adjacent((0,3), b.difference({(0,3)})) == 3
    assert _._count_adjacent((0,5), b.difference({(0,5)})) == 1

def test_circular_count_adjacent() -> None:
    """Test GameBoard._count_adjacent on a board with a circular arrangement of bins"""
    _ = GameBoard(3, 3)
    b = set([(i, j) for j in range(3) for i in range(3)]).difference({(1,1)})
    expected = 8
    assert _._count_adjacent((0,0), b.difference({(0,0)})) == expected
    assert helper_count_from_all_heads(b, expected, _)

def test_solid_block_count_adjacent() -> None:
    """Test GameBoard._count_adjacent on a nxn cluster of bins"""
    _ = GameBoard(10,10)
    for i in range(1, 10):
        b = set([(x, y) for y in range(i) for x in range(i)])
        assert (0,0) in b
        expected = i ** 2
        assert len(b) == expected
        assert _._count_adjacent((0,0), b.difference({(0,0)})) == expected
        assert helper_count_from_all_heads(b, expected, _)

def test_random_arrangement_count_adjacent() -> None:
    """Test Gameboard._count_adjacent on a variety of arbitrary bin arrangements"""
    _ = GameBoard(10,10)
    b1 = {
        (0,1), (0,2), (0,3), 
        (1,0), (1,1), (1,3), (1,4), (1,5), 
        (2,1), (2,2), (2,5),
        (3,0), (3,2), (3,5),
        (4,0), (4,1), (4,3), (4,5),
        (5,1), (5,5),
        (6,3), (6,4), (6,5), (6,6),
        (7,2), (7,5), (7,6),
        (8,3), (8,4), (8,5)
    }
    assert _._count_adjacent((0,1), b1-{(0,1)}) == 24
    assert _._count_adjacent((8,3), b1-{(8,3)}) == 24
    assert _._count_adjacent((6,3), b1-{(6,3)}) == 24
    assert _._count_adjacent((3,2), b1-{(3,2)}) == 24

    assert _._count_adjacent((4,1), b1-{(4,1)}) == 4
    assert _._count_adjacent((4,0), b1-{(4,0)}) == 4
    assert _._count_adjacent((4,3), b1-{(4,3)}) == 1
    assert _._count_adjacent((7,2), b1-{(7,2)}) == 1

"""
Tests for Player.move
"""

def test_simple_player_move() -> None:
    """Test Player.move on docstring example."""
    b = GameBoard(4, 2)
    p = Player(b, 0, 0)
    assert not p.move(UP)
    assert p.move(DOWN)
    assert b.at(0, 1) == [p]
    RecyclingBin(b, 1, 1)
    assert p.move(RIGHT)
    assert b.at(1, 1) == [p]

def test_move_against_boundary_player_move() -> None:
    """Test Player.move on a player attempting to move outside the board"""
    b = GameBoard(2, 2)
    p = Player(b, 0, 0)
    assert not p.move(UP) and not p.move(LEFT)
    assert p.move(RIGHT)
    assert b.at(1, 0)
    assert not p.move(RIGHT)

def test_move_against_unmoveable_player_move() -> None:
    """Test Player.move on every type of unmoveable character"""
    b = GameBoard(5, 1)
    p = Player(b, 0, 0)
    x = Raccoon(b, 2, 0)
    assert p.move(RIGHT)
    assert not p.move(RIGHT)
    assert b.at(2, 0) == [x]

    b = GameBoard(5, 1)
    p = Player(b, 0, 0)
    x = SmartRaccoon(b, 2, 0)
    assert p.move(RIGHT)
    assert not p.move(RIGHT)
    assert b.at(2, 0) == [x]

    b = GameBoard(5, 1)
    p = Player(b, 0, 0)
    x = GarbageCan(b, 2, 0, True)
    assert p.move(RIGHT)
    assert not p.move(RIGHT)
    assert b.at(2, 0) == [x]

    b = GameBoard(5, 1)
    p = Player(b, 0, 0)
    x1 = GarbageCan(b, 2, 0, True)
    x2 = Raccoon(b, 2, 0)
    x2.inside_can = True
    assert p.move(RIGHT)
    assert not p.move(RIGHT)
    assert b.at(2, 0) == [x1, x2]

    b = GameBoard(5, 1)
    p = Player(b, 0, 0)
    x1 = GarbageCan(b, 2, 0, False)
    x2 = Raccoon(b, 2, 0)
    x2.inside_can = True
    assert p.move(RIGHT)
    assert not p.move(RIGHT)
    assert b.at(2, 0) == [x1, x2]

def test_garbage_can_close_player_move() -> None:
    """Test Player.move to lock a garbage bin"""
    b = GameBoard(5, 1)
    p = Player(b, 0, 0)
    x = GarbageCan(b, 2, 0, False)
    assert not x.locked
    assert p.move(RIGHT)
    assert p.move(RIGHT)
    assert b.at(2, 0) == [x]
    assert b.at(1, 0) == [p]
    assert x.locked
    assert not p.move(RIGHT)

def test_simple_linear_recycling_bin_player_move() -> None:
    """Test Player.move by attempting to push a single bin"""
    b = GameBoard(5, 1)
    p = Player(b, 0, 0)
    x = RecyclingBin(b, 2, 0)
    assert p.move(RIGHT)
    assert p.move(RIGHT)
    assert b.at(2, 0) == [p]
    assert b.at(3, 0) == [x]
    assert p.move(RIGHT)
    assert b.at(3, 0) == [p]
    assert b.at(4, 0) == [x]
    print(b)
    assert not p.move(RIGHT)
    assert b.at(3, 0) == [p]
    assert b.at(4, 0) == [x]
    for _ in range(10):
        assert not p.move(RIGHT)
        assert b.at(3, 0) == [p]
        assert b.at(4, 0) == [x]

def test_complex_linear_recycling_bin_player_move() -> None:
    """Test Player.move on a more complicated linear bin arrangement"""
    b = GameBoard(11, 1)
    p = Player(b, 0, 0)
    x1 = RecyclingBin(b, 2, 0)
    x2 = RecyclingBin(b, 3, 0)
    x3 = RecyclingBin(b, 5, 0)
    x4 = RecyclingBin(b, 6, 0)
    x5 = RecyclingBin(b, 8, 0)
    assert b.__str__() == 'P-BB-BB-B--'

    assert p.move(RIGHT)
    assert b.__str__() == '-PBB-BB-B--'
    assert b.at(1, 0) == [p]

    assert p.move(RIGHT)
    assert b.__str__() == '--PBBBB-B--'
    assert b.at(2, 0) == [p]
    assert b.at(3, 0) == [x1]
    assert b.at(4, 0) == [x2]

    assert p.move(RIGHT)
    assert b.__str__() == '---PBBBBB--'
    assert b.at(3, 0) == [p]
    assert b.at(4, 0) == [x1]
    assert b.at(5, 0) == [x2]
    assert b.at(6, 0) == [x3]
    assert b.at(7, 0) == [x4]
    assert b.at(8, 0) == [x5]
    assert b.at(9, 0) == []
    assert b.at(10, 0) == []

    assert p.move(RIGHT)
    assert b.__str__() == '----PBBBBB-'
    assert b.at(4, 0) == [p]
    assert b.at(5, 0) == [x1]
    assert b.at(6, 0) == [x2]
    assert b.at(7, 0) == [x3]
    assert b.at(8, 0) == [x4]
    assert b.at(9, 0) == [x5]
    assert b.at(10, 0) == []
    assert x3.x, x3.y == (7, 0)

    assert p.move(RIGHT)
    assert b.__str__() == '-----PBBBBB'
    assert b.at(5, 0) == [p]
    assert b.at(6, 0) == [x1]
    assert b.at(7, 0) == [x2]
    assert b.at(8, 0) == [x3]
    assert b.at(9, 0) == [x4]
    assert b.at(10, 0) == [x5]

    assert not p.move(RIGHT)
    assert p.move(LEFT)
    assert p.move(RIGHT)
    assert not p.move(RIGHT)




"""
Tests for RecyclingBin.move
"""

def test_simple_recyclingbin_move() -> None:
    """Test RecyclingBin.move on docstring example."""
    b = GameBoard(4, 2)
    rb = RecyclingBin(b, 0, 0)
    assert not rb.move(UP)
    assert rb.move(DOWN)
    assert b.at(0, 1) == [rb]

def test_singleton_recyclingbin_move() -> None:
    """Test RecyclingBin.move on recycling bin in 1x1 board"""
    b = GameBoard(1,1)
    rb = RecyclingBin(b, 0, 0)
    for d in DIRECTIONS:
        assert not rb.move(d)
    assert b.at(0,0) == [rb]

def test_board_filled_recyclingbin_move() -> None:
    """Test RecyclingBin.move on board filled with recycling bins"""
    b = GameBoard(2,2)
    rb1 = RecyclingBin(b, 0, 0)
    rb2 = RecyclingBin(b, 1, 0)
    rb3 = RecyclingBin(b, 0, 1)
    rb4 = RecyclingBin(b, 1, 1)
    for d in DIRECTIONS:
        assert not rb1.move(d)
        assert not rb2.move(d)
        assert not rb3.move(d)
        assert not rb4.move(d)

def test_bin_blocked_recyclingbin_move() -> None:
    """Test RecyclingBin.move on bins blocked by moveable character"""
    b = GameBoard(5, 1)
    rb1 = RecyclingBin(b, 0, 0)
    rb2 = RecyclingBin(b, 1, 0)
    Raccoon(b, 2, 0)
    assert b.__str__() == 'BBR--'
    assert not rb1.move(RIGHT)
    assert b.__str__() == 'BBR--'
    assert b.at(0, 0) == [rb1]
    assert b.at(1, 0) == [rb2]

    b = GameBoard(5, 1)
    rb1 = RecyclingBin(b, 0, 0)
    rb2 = RecyclingBin(b, 1, 0)
    GarbageCan(b, 2, 0, False)
    assert b.__str__() == 'BBO--'
    assert not rb1.move(RIGHT)
    assert b.__str__() == 'BBO--'
    assert b.at(0, 0) == [rb1]
    assert b.at(1, 0) == [rb2]

    b = GameBoard(5, 1)
    rb1 = RecyclingBin(b, 0, 0)
    rb2 = RecyclingBin(b, 1, 0)
    Player(b, 2, 0)
    assert b.__str__() == 'BBP--'
    assert not rb1.move(RIGHT)
    assert b.__str__() == 'BBP--'
    assert b.at(0, 0) == [rb1]
    assert b.at(1, 0) == [rb2]

    b = GameBoard(5, 1)
    rb1 = RecyclingBin(b, 0, 0)
    rb2 = RecyclingBin(b, 1, 0)
    RecyclingBin(b, 2, 0)
    assert b.__str__() == 'BBB--'
    assert rb1.move(RIGHT)
    assert b.__str__() == '-BBB-'
    assert b.at(1, 0) == [rb1]
    assert b.at(2, 0) == [rb2]
    assert rb1.move(RIGHT)
    assert b.__str__() == '--BBB'
    assert not rb1.move(RIGHT)
    assert b.__str__() == '--BBB'


    

    
    



"""
Tests for Raccoon.check_trapped
"""

def test_simple_raccoon_check_trapped() -> None:
    """Test Raccoon.check_trapped on docstring example."""
    b = GameBoard(3, 3)
    r = Raccoon(b, 2, 1)
    Raccoon(b, 2, 2)
    Player(b, 2, 0)
    assert not r.check_trapped()
    RecyclingBin(b, 1, 1)
    assert r.check_trapped()

"""
Tests for Raccoon.move
"""

def test_simple_raccoon_move() -> None:
    """Test Raccoon.move on docstring example."""
    b = GameBoard(4, 2)
    r = Raccoon(b, 0, 0)
    assert not r.move(UP)
    assert r.move(DOWN)
    assert b.at(0, 1) == [r]
    g = GarbageCan(b, 1, 1, True)
    assert r.move(RIGHT)
    assert (r.x, r.y) == (0, 1)  # Raccoon didn't change its position
    assert not g.locked  # Raccoon unlocked the garbage can!
    assert r.move(RIGHT)
    assert r.inside_can
    assert len(b.at(1, 1)) == 2  # Raccoon and GarbageCan are both at (1, 1)!

def test_blocking_characters_raccoon_move() -> None:
    """Test Raccoon.move towards every blocking character"""
    # Player
    b = GameBoard(5, 1)
    r = Raccoon(b, 0, 0)
    assert r.move(RIGHT)
    assert b.at(1, 0) == [r]
    Player(b, 2, 0)
    assert not r.move(RIGHT)
    assert b.at(1, 0) == [r]

    # RecyclingBin
    b = GameBoard(5, 1)
    r = Raccoon(b, 1, 0)
    RecyclingBin(b, 2, 0)
    assert not r.move(RIGHT)
    assert b.at(1, 0) == [r]

    # Raccoon
    b = GameBoard(5, 1)
    r = Raccoon(b, 1, 0)
    Raccoon(b, 2, 0)
    assert not r.move(RIGHT)
    assert b.at(1, 0) == [r]

    # SmartRaccoon
    b = GameBoard(5, 1)
    r = Raccoon(b, 1, 0)
    SmartRaccoon(b, 2, 0)
    assert not r.move(RIGHT)
    assert b.at(1, 0) == [r]

def test_raccoon_entering_open_can_raccoon_move() -> None:
    """Test Raccoon.move on raccoon entering an open garbage can"""
    b = GameBoard(5, 1)
    r = Raccoon(b, 1, 0)
    g = GarbageCan(b, 2, 0, False)
    assert r.move(RIGHT)
    assert b.at(1, 0) == []
    assert b.at(2, 0) == [r, g]
    assert r.inside_can 
    for d in DIRECTIONS:
        assert not r.move(d)
        assert b.at(2, 0) == [r, g]

def test_raccoon_entering_locked_can_raccoon_move() -> None:
    """Test Raccoon.move on raccoon entering a locked garbage can"""
    b = GameBoard(5, 1)
    r = Raccoon(b, 1, 0)
    g = GarbageCan(b, 2, 0, True)
    assert g.locked
    assert r.move(RIGHT)
    assert b.at(1, 0) == [r]
    assert b.at(2, 0) == [g]
    assert not r.inside_can
    assert not g.locked

    assert r.move(RIGHT)
    assert b.at(2, 0) == [r, g]
    assert r.inside_can

    for d in DIRECTIONS:
        assert not r.move(d)
        assert b.at(2, 0) == [r, g]

def test_single_square_raccoon_move() -> None:
    """Test Raccoon.move on a raccoon on a 1x1 board"""
    b = GameBoard(1, 1)
    r = Raccoon(b, 0, 0)
    for d in DIRECTIONS:
        assert not r.move(d)
        assert r.x == 0 and r.y == 0
        assert b.at(0, 0) == [r]



"""
Tests for Raccoon.take_turn
"""

def test_simple_raccoon_take_turn() -> None:
    """Test Raccoon.take_turn on docstring example."""
    b = GameBoard(3, 4)
    r1 = Raccoon(b, 0, 0)
    r1.take_turn()
    assert (r1.x, r1.y) in [(0, 1), (1, 0)]
    r2 = Raccoon(b, 2, 1)
    RecyclingBin(b, 2, 0)
    RecyclingBin(b, 1, 1)
    RecyclingBin(b, 2, 2)
    r2.take_turn()  # Raccoon is trapped
    assert (r2.x, r2.y) == (2, 1)

def test_raccoon_in_can_raccoon_take_turn() -> None:
    """Test Raccoon.take_turn on a raccoon in a can"""
    b = GameBoard(3, 4)
    g = GarbageCan(b, 2, 0, False)
    r = Raccoon(b, 2, 0)
    r.inside_can = True
    assert b.at(2, 0) == [g, r]
    r.take_turn()
    assert b.at(2, 0) == [g, r]
    assert r.x == 2 and r.y == 0

def test_raccoon_in_1d_corner_raccoon_take_turn() -> None:
    """Test Raccoon.take_turn on a raccoon in a corner of a 1d board"""
    b = GameBoard(5, 1)
    r = Raccoon(b, 0, 0)
    assert b.__str__() == 'R----'
    r.take_turn()
    assert b.__str__() == '-R---'
    assert b.at(0, 0) == []
    assert b.at(1, 0) == [r]
    assert r.x == 1 and r.y == 0

def test_raccoon_in_2d_corner_raccoon_take_turn() -> None:
    """Test Raccoon.take_turn on a raccoon in a corner of a 2d board"""
    for _ in range(100):
        b = GameBoard(3, 3)
        r = Raccoon(b, 0, 0)
        r.take_turn()
        assert (r.x, r.y) in [RIGHT, DOWN]
        assert b.at(0, 0) == []

def test_randomness_raccoon_take_turn() -> None:
    """Test Raccoon.take_turn's randomness using statistic method"""
    dirs = {
        UP: 0,
        DOWN: 0,
        LEFT: 0,
        RIGHT: 0
    }
    for _ in range(10000):
        b = GameBoard(3, 3)
        r = Raccoon(b, 1, 1)
        r.take_turn()
        dirs[(r.x - 1, r.y - 1)] += 1
    for d in dirs:
        assert abs((dirs[d] / 10000) - 0.25) < 0.1

    dirs = {
        UP: 0,
        LEFT: 0,
        RIGHT: 0
    }
    for _ in range(10000):
        b = GameBoard(3, 3)
        r = Raccoon(b, 1, 1)
        RecyclingBin(b, 1, 2)
        r.take_turn()
        dirs[(r.x - 1, r.y - 1)] += 1
    for d in dirs:
        assert abs((dirs[d] / 10000) - 0.333) < 0.1

    dirs = {
        LEFT: 0,
        RIGHT: 0
    }
    for _ in range(10000):
        b = GameBoard(3, 3)
        r = Raccoon(b, 1, 1)
        RecyclingBin(b, 1, 2)
        RecyclingBin(b, 1, 0)
        r.take_turn()
        dirs[(r.x - 1, r.y - 1)] += 1
    for d in dirs:
        assert abs((dirs[d] / 10000) - 0.5) < 0.1

    dirs = {
        RIGHT: 0
    }
    for _ in range(10000):
        b = GameBoard(3, 3)
        r = Raccoon(b, 1, 1)
        RecyclingBin(b, 1, 2)
        RecyclingBin(b, 1, 0)
        RecyclingBin(b, 0, 1)
        r.take_turn()
        dirs[(r.x - 1, r.y - 1)] += 1
    assert dirs[RIGHT] == 10000


"""
Tests for SmartRaccoon.take_turn
"""

def test_simple_smartraccoon_take_turn() -> None:
    """Test SmartRaccoon.take_turn on docstring example."""
    b = GameBoard(8, 1)
    s = SmartRaccoon(b, 4, 0)
    GarbageCan(b, 3, 1, False)
    GarbageCan(b, 0, 0, False)
    GarbageCan(b, 7, 0, False)
    s.take_turn()
    assert s.x == 5
    s.take_turn()
    assert s.x == 6

def test_raccoon_in_can_smartraccoon_take_turn() -> None:
    """Test SmartRaccoon.take_turn on raccoon in garbage can"""
    b = GameBoard(4, 4)
    s = SmartRaccoon(b, 2, 2)
    s.inside_can = True
    g1 = GarbageCan(b, 2, 2, False)
    assert b.at(2, 2) == [s, g1]
    s.take_turn()
    assert b.at(2, 2) == [s, g1]
    assert s.x == 2 and s.y == 2

    g2 = GarbageCan(b, 2, 1, False)
    s.take_turn()
    assert b.at(2, 2) == [s, g1]
    assert s.x == 2 and s.y == 2

def test_raccoon_towards_can_smartraccoon_take_turn() -> None:
    """Test SmartRaccoon.take_turn on raccoon moving towards a can"""
    b = GameBoard(100, 100)
    s = SmartRaccoon(b, 20, 20)
    g = GarbageCan(b, 99, 20, False)
    prev_x, prev_y = s.x, s.y
    for _ in range(79):
        s.take_turn()
        assert (s.x - prev_x, s.y - prev_y) == RIGHT
        prev_x, prev_y = s.x, s.y
    assert (s.x, s.y) == (99, 20)
    assert s.inside_can

    b = GameBoard(100, 100)
    s = SmartRaccoon(b, 20, 20)
    g = GarbageCan(b, 99, 20, True)
    prev_x, prev_y = s.x, s.y
    for _ in range(78):
        s.take_turn()
        assert (s.x - prev_x, s.y - prev_y) == RIGHT
        prev_x, prev_y = s.x, s.y
    assert (s.x, s.y) == (98, 20)
    assert not s.inside_can

    assert g.locked
    s.take_turn()
    assert (s.x, s.y) == (98, 20)
    assert not g.locked

    s.take_turn()
    assert (s.x, s.y) == (99, 20)
    assert s.inside_can

"""
Tests for GameBoard.give_turns
"""

def test_simple_give_turns() -> None:
    """Test GameBoard.give_turns on docstring example."""
    b = GameBoard(4, 3)
    p = Player(b, 0, 0)
    r = Raccoon(b, 1, 1)
    for _ in range(RACCOON_TURN_FREQUENCY - 1):
        b.give_turns()
    assert b.turns == RACCOON_TURN_FREQUENCY - 1
    assert (r.x, r.y) == (1, 1)  # Raccoon hasn't had a turn yet
    assert (p.x, p.y) == (0, 0)  # Player hasn't had any inputs
    p.record_event(RIGHT)
    b.give_turns()
    assert (r.x, r.y) != (1, 1)  # Raccoon has had a turn!
    assert (p.x, p.y) == (1, 0)  # Player moved right!


if __name__ == '__main__':
    import pytest

    pytest.main(['a1_sample_test.py'])
