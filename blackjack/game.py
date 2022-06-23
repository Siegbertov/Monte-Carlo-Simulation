from .table import Table
from .champion import ChampionSpace


class Game:
    GOAL = 21

    def __init__(self, player_strategy=None, dealer_threshold=17, player_threshold=17):
        self.table = Table(player_strategy=player_strategy, dealer_threshold=dealer_threshold, player_threshold=player_threshold)

        self.win = 0
        self.draw = 0
        self.lose = 0

    def show(self):
        print(f"WIN: {self.win}")
        print(f"DRAW: {self.draw}")
        print(f"LOSE: {self.lose}")

    def reset(self):
        self.table.reset()

    def play(self):
        self.table.play()

        self._check()

    def show_table(self):
        self.table.show()

    def _check(self):
        results = self.table.who_win()
        for result in results:
            if result == ChampionSpace.PLAYER:
                self.win += 1
            elif result == ChampionSpace.DRAW:
                self.draw += 1
            elif result == ChampionSpace.DEALER:
                self.lose += 1

    def get_not_losing(self):
        return (self.win + self.draw) / (self.win + self.draw + self.lose)
