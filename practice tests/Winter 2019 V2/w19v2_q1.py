from typing import List, Dict



class Riding:
    """An election riding

    === Attributes ===
    r_name: the name of the riding
    voter_list: a dictionary of all the voters and whether they voted or not
    """
    # Attribute Types
    r_name: str
    voter_list: dict[int] = bool

    def __init__(self, name: str) -> None:
        """Initialise an instance of the Riding class """
        self.r_name = name
        self.voter_list = {}

    def add_voters(self, voters: list[int]) -> None:
        """Add voters to the voter_list for a given riding"""
        for item in voters:
            if item not in self.voter_list:
                self.voter_list[item] = True

    def can_vote(self, voter: int) -> bool:
        """Determine whether a given voter can vote or not"""
        if voter not in self.voter_list:
            return False
        else:
            return self.voter_list[voter]

    def voted(self, voter: int) -> None:
        """Record a vote by the given voter number"""
        self.voter_list[voter] = False

        


