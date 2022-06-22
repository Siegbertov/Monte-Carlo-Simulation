from .card import Card
from .action import ActionSpace
from .hand import Hand
from .deck import Deck


class Person:
    GOAL = 21

    def __init__(self, threshold=17, strategy=None):
        self.threshold = threshold
        if strategy is None:
            self.strategy = "threshold"
        else:
            self.strategy = strategy

        self.current_focus = 0
        self.hands = [Hand()]
        self.is_stand = False

    def reset(self):
        self.hands = [Hand()]
        self.is_stand = False

    def take(self, card: Card, num_of_hand=0):
        for h_index, hand in enumerate(self.hands):
            if h_index == num_of_hand:
                hand.put(card)

    def show(self):
        for hand in self.hands:
            hand.show()

    def __len__(self):
        return self.hands.__len__()

    def __getitem__(self, item):
        return self.hands[item]

    def _is_all_no_split(self):
        res = True
        for hand in self.hands:
            if ActionSpace.SPLIT in hand.possible_actions:
                res = False
                break
        return res

    def step(self, action: ActionSpace, deck: Deck):
        pass

    def make_decision(self) -> list:
        """decision based on threshold"""
        dec = []
        for hand in self.hands:
            if hand.best_score >= self.threshold:
                dec.append(ActionSpace.STAND)
            else:
                dec.append(ActionSpace.HIT)
        return dec

    def play(self, deck: Deck):
        pass

