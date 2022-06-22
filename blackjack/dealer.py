from .person import Person, Deck, ActionSpace


class Dealer(Person):
    def __init__(self, threshold=17, strategy=None):
        super().__init__(threshold=threshold, strategy=strategy)

    def get_visible_card(self):
        """return first card from its hand"""
        return self.hands[0][0]
