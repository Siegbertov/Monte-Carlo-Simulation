from .card import Card
from random import shuffle


class Deck:
    POSSIBLE_SUITS_U = ['♠', '♥', '♦', '♣']
    POSSIBLE_RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.cards = []
        self._create()
        self._shuffle()

    def reset(self):
        self.cards = []
        self._create()
        self._shuffle()

    def pop_one_card(self):
        return self.cards.pop()

    def __len__(self):
        return self.cards.__len__()

    def _create(self):
        for s in self.POSSIBLE_SUITS_U:
            for r in self.POSSIBLE_RANKS:
                self.cards.append(Card(s, r))

    def _shuffle(self):
        shuffle(self.cards)
