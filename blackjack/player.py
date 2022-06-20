from .person import Person
# from card import Card


class Player(Person):
    def __init__(self, threshold=17):
        super().__init__(threshold)

    # def make_decision(self, visible_card: Card):
        # TODO implement make_decision() based on high-performance strategy that you can find in google
    #     pass
