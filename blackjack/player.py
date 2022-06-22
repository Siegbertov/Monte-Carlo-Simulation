from .person import Person, Deck, ActionSpace  # imported DECK with annotation purposes


class Player(Person):
    def __init__(self, threshold=17, strategy=None):
        super().__init__(threshold=threshold, strategy=strategy)
