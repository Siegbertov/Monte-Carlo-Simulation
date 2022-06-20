from card import Card


class Person:
    def __init__(self):
        self.hand = []

    def take(self, some_card: Card):
        self.hand.append(some_card)

