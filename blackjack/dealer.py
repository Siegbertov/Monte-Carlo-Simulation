from person import Person


class Dealer(Person):
    def __init__(self, threshold=17):
        super().__init__(threshold)

    def get_visible_card(self):
        """return first card from its hand"""
        return self.hand[0]
