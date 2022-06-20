from .table import Table
from .champion import ChampionSpace


class Game:
    def __init__(self, player_threshold=17, dealer_threshold=17):
        self.table = Table(player_threshold, dealer_threshold)

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

        result = self.table.who_won()
        if result == ChampionSpace.PLAYER:
            self.win += 1
        elif result == ChampionSpace.DRAW:
            self.draw += 1
        elif result == ChampionSpace.DEALER:
            self.lose += 1

    def get_not_losing(self):
        return (self.win + self.draw) / (self.win + self.draw + self.lose)


def main():
    new_game = Game(14, 20)
    for _ in range(10_000):
        new_game.play()
        new_game.reset()

    print(new_game.get_not_losing())


if __name__ == "__main__":
    main()
