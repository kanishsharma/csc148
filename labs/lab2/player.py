from __future__ import annotations
from typing import List




class Player:
    """
    A player class that stores information about the player name and the history
    of the last 100 scores achieved in the game

    === Attributes ===
    name: the name of the player
    : the history of the last 100 scores they've achieved

    === Sample Usage ===

    >>> jim = Player('Jim')
    >>> jim.games_played
    []
    >>> jim.play_game(10)
    >>> jim.games_played
    [10]

    >>> betty = Player('Betty', [10, 15, 20, 25, 30])
    >>> betty.games_played
    [10, 15, 20, 25, 30]
    >>> betty.score_average()
    20
    >>> betty.score_average(3)
    15
    >>> betty.top_score()
    30
    """
    #Attribute Types:
    name: str
    games_played: List[int]

    def __init__(self, name: str, game_list: List[int] = []):
        """ Initalise a new Player

        >>> daniel = Player('Daniel')
        >>> daniel.name
        'Daniel'
        >>> daniel.games_played
        []

        >>> robert = Player('Robert', [10, 15, 20, 25, 30])
        >>> robert.name
        'Robert'
        >>> robert.games_played
        [10, 15, 20, 25, 30]
        """
        self.name = name
        self.games_played = game_list

    def play_game(self, score: int):
        """Add a score to games_played for the Player

        >>> chad = Player('Chad')
        >>> chad.games_played
        []
        >>> chad.play_game(10)
        >>> chad.games_played
        [10]
        """
        self.games_played.append(score)

    def score_average(self, n: int = 0):
        """Return the average score of a specific number of games n

        Precondition: n >= len(self.games_played) and n is positive

        >>> butt = Player('Butt', [1, 2, 3, 4, 5])
        >>> butt.score_average()
        3

        >>> monica = Player('Monica', [2, 4, 6, 8, 10])
        >>> monica.score_average(3)
        4
        """
        if n == 0:
            n = len(self.games_played)

        summed_list = self.games_played[:n]
        sum_list = sum(summed_list)
        return sum_list // n

    def top_score(self):
        """Return the top score of all games played

        >>> adam = Player('Adam', [10, 20, 30, 40, 50, 60, 99999])
        >>> adam.top_score()
        99999
        """
        return max(self.games_played)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

