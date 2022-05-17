from typing import Tuple, Set

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [LEFT, UP, RIGHT, DOWN]


def count_adjacent(head: Tuple[int], b: Set[Tuple[int]]) -> int:
    if all([(head[0] + x, head[1] + y) not in b for (y, x) in DIRECTIONS]):
        # base case: no more adjacent uncounted bins
        return 1
    else:
        count = 1
        # get list of uncounted bins adjacent to the head bin
        adj_bins = [(head[0] + x, head[1] + y) 
            for (y, x) in DIRECTIONS 
            if (head[0] + x, head[1] + y) in b
        ]
        # remove these bins from the board to indicate them as counted
        for bin in adj_bins:
            b.remove(bin)
        # recursively count adjacent bins for each adjacent bin
        for bin in adj_bins:
            count += count_adjacent(bin, b)
        return count


def get_adjacent(head: Tuple[int], b: Set[Tuple[int]]) -> int:
    return count_adjacent(head, b.difference({head}))

    
def get_max_adjacent(b):
    adjacent_bins = []
    b = b.copy()
    while len(b):
        head = next(iter(b))
        b.remove(head)
        adjacent_bins.append(count_adjacent(head, b))
    return max(adjacent_bins)


def test_get_adjacent_all_heads(b: Set[Tuple[int]], expected: int) -> bool:
    for square in b:
        if get_adjacent(square, b) != expected:
            return False
    return True


if __name__ == "__main__":
    b1 = {(1,1), (1,2), (2,2)}
    b2 = {(0,1), (1,1), (1,0), (1,2)}
    b3 = {(0,1), (0,2), (1,1), (1,2), (2,1), (1,0), (2,2)}
    b4 = set([(i, j) for j in range(4) for i in range(4)])
    b5 = set([(i, j) for j in range(3) for i in range(3)]).difference({(1,1)})

    b6 = {(0,0), (1,1), (2,2)}
    b7 = {(0,0), (0,1), (1,1), (2,2)}
    b8 = {(0,1), (0,2), (1,1), (1,2), (2,1), (1,0), (2,2), (4,4), (4,5), (4,6)}
    b9 = {(0,1), (0,2), (1,1), (4,4), (4,5), (4,6), (4, 7)}

    assert get_adjacent((1,1), b1) == 3
    assert test_get_adjacent_all_heads(b1, 3)
    assert get_adjacent((0,1), b2) == 4
    assert test_get_adjacent_all_heads(b2, 4)
    assert get_adjacent((0,1), b3) == 7
    assert test_get_adjacent_all_heads(b3, 7)
    assert get_adjacent((0,0), b4) == 16
    assert test_get_adjacent_all_heads(b4, 16)
    assert get_adjacent((0,0), b5) == 8
    assert test_get_adjacent_all_heads(b5, 8)

    assert get_adjacent((0,0), b6) == 1
    assert get_adjacent((1,1), b6) == 1
    assert get_adjacent((2,2), b6) == 1

    assert get_adjacent((0,0), b7) == 3
    assert get_adjacent((0,1), b7) == 3
    assert get_adjacent((1,1), b7) == 3
    assert get_adjacent((2,2), b7) == 1

    assert get_max_adjacent(b6) == 1
    assert get_max_adjacent(b7) == 3
    assert get_max_adjacent(b8) == 7
    assert get_max_adjacent(b9) == 4