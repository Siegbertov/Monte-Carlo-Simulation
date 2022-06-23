from .card import Card
from .action import ActionSpace
from .hand import Hand
from .deck import Deck


class Person:
    GOAL = 21

    def __init__(self, threshold=17, strategy=None):
        self.threshold = threshold
        if strategy is None or strategy == "threshold":
            self.strategy = "threshold"
        elif strategy == "always_split":
            self.strategy = strategy
        else:
            raise Exception("Unknown strategy: try {'threshold', 'always_split'}")

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

    def make_decision(self) -> tuple:
        dec = []
        if self.strategy == "threshold":
            for hand in self.hands:
                if hand.best_score >= self.threshold:
                    dec.append(ActionSpace.STAND)
                else:
                    dec.append(ActionSpace.HIT)

        elif self.strategy == "always_split":
            for hand in self.hands:
                if ActionSpace.SPLIT in hand.possible_actions:
                    dec.append(ActionSpace.SPLIT)
                elif hand.best_score >= self.threshold:
                    dec.append(ActionSpace.STAND)
                else:
                    dec.append(ActionSpace.HIT)
        return dec, True if len(set(dec)) == 1 and dec[0] == ActionSpace.STAND else False

    def play(self, deck: Deck):
        if self.strategy == "threshold":
            while not self.is_stand:
                decisions, self.is_stand = self.make_decision()
                hands = self.hands
                new_hands = []

                for i, decision in enumerate(decisions):
                    if decision == ActionSpace.HIT:
                        new_hand = hands[i].hit(deck)
                        new_hands.append(new_hand)
                    elif decision == ActionSpace.STAND:
                        new_hand = hands[i].stand()
                        new_hands.append(new_hand)
                self.hands = new_hands
        elif self.strategy == "always_split":
            while not self.is_stand:
                decisions, self.is_stand = self.make_decision()
                hands = self.hands
                new_hands = []

                for i, decision in enumerate(decisions):
                    if decision == ActionSpace.SPLIT:
                        new_hand = hands[i].split(deck)
                        new_hands.append(new_hand[0])
                        new_hands.append(new_hand[1])
                    elif decision == ActionSpace.HIT:
                        new_hand = hands[i].hit(deck)
                        new_hands.append(new_hand)
                    elif decision == ActionSpace.STAND:
                        new_hand = hands[i].stand()
                        new_hands.append(new_hand)
                self.hands = new_hands
