from card import Card
from player import Player
from dealer import Dealer
from random import shuffle
from action import ActionSpace


class Table:
    POSSIBLE_SUITS_U = ['♠', '♥', '♦', '♣']
    POSSIBLE_RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.main_player = Player()
        self.main_dealer = Dealer()

        self.deck = []
        self.create_deck()
        self.start()

    def create_deck(self):
        for s in self.POSSIBLE_SUITS_U:
            for r in self.POSSIBLE_RANKS:
                self.deck.append(Card(s, r))
        self._shuffle_deck()

    def reset(self):
        self.main_player = Player()
        self.main_dealer = Dealer()

        self.deck = []
        self.create_deck()
        self.start()

    def _shuffle_deck(self):
        shuffle(self.deck)

    def _give_card(self, who):
        who.take(self.deck.pop())
        who.count_score_space()

    def start(self):
        for _ in range(2):
            self._give_card(self.main_player)
            self._give_card(self.main_dealer)

    def who_win(self):
        # TODO implement who_wins
        pass

    def play(self):
        # PLAYER TAKES ACTIONS
        while not self.main_player.is_stand:
            decision = self.main_player.make_decision(self.main_dealer.get_visible_card())
            if decision == ActionSpace.HIT:
                self._give_card(self.main_player)
            elif decision == ActionSpace.STAND:
                self.main_player.is_stand = True

        # DEALER TAKES ACTIONS
        while not self.main_dealer.is_stand:
            decision = self.main_dealer.make_decision()
            if decision == ActionSpace.HIT:
                self._give_card(self.main_dealer)
            elif decision == ActionSpace.STAND:
                self.main_dealer.is_stand = True


def main():
    t = Table()
    t.play()

    t.main_player.show()
    t.main_dealer.show()


if __name__ == "__main__":
    main()
