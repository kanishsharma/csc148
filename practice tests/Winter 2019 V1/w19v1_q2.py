from typing import Dict

class Party:
    """A class that represents a political party with a name and a leader.
    There are also donors that can

    === Attributes ===
    party_name: the name of the party
    party_leader: the name of the leader of the party
    party_donations: the total number of donations this party has recieved
    donor_list: a record of all the donor number and their contributions
    """
    # Attribute Types
    party_name: str
    party_leader: str
    party_donations: float
    donor_list: dict[int] = float

    def __init__(self, name, leader) -> None:
        """Initialise a new party
        """
        self.party_name = name
        self.party_leader = leader
        self.party_donations = 0.0
        self.donor_list = {}

    def record_donation(self, donor_number: int, value: float) -> None:
        self.party_donations += value
        if donor_number not in self.donor_list:
            self.donor_list[donor_number] = value
        else:
            self.donor_list[donor_number] += value

    def donations_of(self, donor_number: int) -> float:
        if donor_number not in self.donor_list:
            return 0.0
        else:
            return self.donor_list[donor_number]

    def total_donations(self) -> float:
        return self.party_donations
