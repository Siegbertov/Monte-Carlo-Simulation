from card import Card
from player import Player
from dealer import Dealer
from random import shuffle


class Table:
    POSSIBLE_SUITS_U = ['♠', '♥', '♦', '♣']
    POSSIBLE_RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.main_player = Player()
        self.main_dealer = Dealer()
        self.deck = []
        self.create_deck()

    def create_deck(self):
        for s in self.POSSIBLE_SUITS_U:
            for r in self.POSSIBLE_RANKS:
                self.deck.append(Card(s, r))
        self._shuffle_deck()

    def _shuffle_deck(self):
        shuffle(self.deck)


