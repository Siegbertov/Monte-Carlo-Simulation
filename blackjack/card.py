from typing import NamedTuple


class Card(NamedTuple):
    suit: str
    rank: str

    def get_score(self):
        if self.rank == "A":
            return 1, 11
        elif self.rank in ["K", "Q", "J"]:
            return 10
        else:
            return int(self.rank)
